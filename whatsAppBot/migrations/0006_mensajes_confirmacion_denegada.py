# Generated by Django 2.2 on 2020-08-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsAppBot', '0005_mensajes'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajes',
            name='confirmacion_denegada',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
