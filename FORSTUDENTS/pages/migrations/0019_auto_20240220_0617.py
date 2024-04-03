# Generated by Django 3.1.13 on 2024-02-20 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_auto_20240220_0609'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatigoryClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='privatesoftwarclasses',
            name='departmentcours',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pages.catigoryclasses'),
        ),
    ]
