# Generated by Django 5.0.6 on 2024-06-22 17:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0023_alter_mailing_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mailing',
            name='finish_send',
            field=models.DateTimeField(verbose_name='Дата и время завершения рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='first_send',
            field=models.DateTimeField(verbose_name='Дата и время отправки'),
        ),
    ]
