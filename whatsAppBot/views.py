from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse,Message
from .models import Invitado, Mensajes
from .imageGenerator import genImage, deleteImgs


def homeView(request):
    invitados = Invitado.objects.all()
    numHombres = len(Invitado.objects.filter(sexo="H"))
    numMujeres = len(Invitado.objects.filter(sexo="M"))
    return render(request, 'home.html', {'invitados':invitados,'hombres':numHombres,'mujeres':numMujeres})


@twilio_view
def smsView(request):
    try:
        #deleteImgs()
        mensajes = Mensajes.objects.get(id = 1)
        num = request.POST.get('From')
        num = num[9::]
        if len(Invitado.objects.all().filter(numero=num)) == 0:
            if request.POST.get('From') == None:
                r = MessagingResponse()
                r.message("No Number")
                return r
            invitado = Invitado.objects.create(numero=str(num), nombre=request.POST.get('Body'))
            msg = "¿{} *{}*? \n \n -Si \n -No".format(mensajes.confirmacion, request.POST.get('Body'))
        else:
            invitado = Invitado.objects.get(numero = num)
            if invitado.confirmado:
                if invitado.cambio_nombre:
                    invitado.nombre = request.POST.get('Body')
                    invitado.cambio_nombre = False
                    invitado.save()
                    msg = "Nombre cambiado a *{}* exitosamente".format(request.POST.get('Body')) + '\n\n*Nota*: La tarjeta anterior queda invalida\n\n(Ingrese cualquier cosa para ver acciones)'
                    r = MessagingResponse()
                    msg_media = Message()
                    msg_media.body(msg)
                    # Imagen
                    nombreImagen = genImage(invitado.nombre, str(invitado.id))
                    msg_media.media('http://' + request.get_host() + '/static/invitaciones/' + nombreImagen)
                    r.nest(msg_media)
                    # msg_media = r.message(msg)
                    return r
                if request.POST.get('Body') == "1":
                    invitados = []
                    for invitado in Invitado.objects.all():
                        invitados.append(invitado.nombre)
                    invitados.sort()
                    invitados_str = '*Lista de invitados*\n'
                    for i in range(len(invitados)):
                        invitados_str += "{}. {}\n".format((i+1),invitados[i])
                    msg = invitados_str + '\n(Ingrese cualquier cosa para ver acciones)'
                elif request.POST.get('Body') == "2":
                    msg = "Por favor, ingrese su nombre a cambiar:"
                    invitado.cambio_nombre = True
                    invitado.save()
                elif request.POST.get('Body') == "3":
                    invitado.delete()
                    msg = "*Desconfirmacion Exitosa*\n\nVuelva a ingresar su nombre si desea volver a confirmar\n\n{}".format(mensajes.mensaje_final)
                else:
                    msg = "*Acciones Disponibles*\n(Ingrese el numero de accion a realizar) " \
                          "\n \n1. Ver lista de invitados \n2. Cambiar nombre \n3. Desconfirmar asistencia " \
                          "\n\n{}".format(mensajes.mensaje_final)
            else:
                if request.POST.get('Body').lower() == "si" or request.POST.get('Body').lower() == "-si":
                    invitado.confirmado = True
                    invitado.save()
                    msg = mensajes.confirmacion_exitosa + '\n(Ingrese cualquier cosa para ver acciones)'
                    """
                    msg += "\n\n*Acciones Disponibles*\n(Ingrese el numero de accion a realizar) " \
                      "\n \n1. Ver lista de invitados \n2. Cambiar nombre \n3. Desconfirmar asistencia " \
                      "\n\n{}".format(mensajes.mensaje_final)
                    """
                    r = MessagingResponse()
                    msg_media = Message()
                    msg_media.body(msg)
                    #Imagen
                    nombreImagen = genImage(invitado.nombre,str(invitado.id))
                    msg_media.media('http://' + request.get_host() + '/static/invitaciones/' + nombreImagen)
                    r.nest(msg_media)
                    #msg_media = r.message(msg)
                    return r
                elif request.POST.get('Body').lower() == "no" or request.POST.get('Body').lower() == "-no":
                    msg = mensajes.confirmacion_denegada
                    invitado.delete()
                else:
                    msg = "_{}_\n\n¿{} *{}*? \n \n -Si \n -No".format(mensajes.comando_invalido, mensajes.confirmacion,
                                                                  invitado.nombre)


        r = MessagingResponse()
        r.message(msg)
        return r
    except:
        r = MessagingResponse()
        r.message("Lo sentimos, hubo un error.")
        return r

