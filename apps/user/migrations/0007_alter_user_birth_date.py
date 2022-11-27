# Generated by Django 4.1.3 on 2022-11-27 02:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Birth Date'),
        ),
    ]