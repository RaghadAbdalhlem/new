# Generated by Django 5.0.2 on 2024-02-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0040_alter_apartments_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='img',
            field=models.ImageField(upload_to='static/image/'),
        ),
    ]
