# Generated by Django 5.0.6 on 2024-07-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_is_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Отчество'),
        ),
    ]
