# Generated by Django 3.1.13 on 2024-02-20 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_auto_20240220_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='area',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pages.area'),
        ),
    ]
