from django.contrib import admin
from .models import Invitado, Mensajes
# Register your models here.

class InvitadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero','sexo']
    fields = ['nombre', 'numero','sexo']
    actions = ['make_hombre','make_mujer']

    def make_hombre(self, request, queryset):
        return queryset.update(sexo='H')
    def make_mujer(self, request, queryset):
        return queryset.update(sexo='M')

admin.site.register(Invitado,InvitadoAdmin)
admin.site.register(Mensajes)