# Generated by Django 4.2.4 on 2023-11-24 15:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0003_remove_return_is_refill'),
    ]

    operations = [
        migrations.AddField(
            model_name='return',
            name='issue',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]