# Generated by Django 5.0.6 on 2024-07-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_github_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_blocked',
            field=models.BooleanField(default=False, verbose_name='Заблокирован'),
        ),
    ]
