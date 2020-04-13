# Generated by Django 3.0.5 on 2020-04-13 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200413_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='follow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='main_app.Profile'),
        ),
        migrations.AlterField(
            model_name='following',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile'),
        ),
    ]
