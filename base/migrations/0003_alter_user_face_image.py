# Generated by Django 4.1.5 on 2023-02-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='face_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
