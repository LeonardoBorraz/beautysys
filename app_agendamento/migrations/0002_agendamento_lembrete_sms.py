# Generated by Django 5.1.6 on 2025-05-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_agendamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='lembrete_sms',
            field=models.BooleanField(default=False),
        ),
    ]
