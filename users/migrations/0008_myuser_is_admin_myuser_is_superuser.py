# Generated by Django 5.0.2 on 2024-02-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_myuser_is_admin_remove_myuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
