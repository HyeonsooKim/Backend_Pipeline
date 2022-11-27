# Generated by Django 4.1.3 on 2022-11-26 15:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Birth Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', '남성'), ('Female', '여성')], max_length=6, null=True),
        ),
    ]