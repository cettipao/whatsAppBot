# Generated by Django 2.2 on 2020-08-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('whatsAppBot', '0002_delete_talker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]
