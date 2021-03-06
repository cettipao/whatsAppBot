# Generated by Django 2.2 on 2020-08-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsAppBot', '0003_invitado'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitado',
            name='confirmado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invitado',
            name='nombre',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
