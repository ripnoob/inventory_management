# Generated by Django 4.2.4 on 2023-11-21 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('return_cost', models.FloatField()),
                ('is_refill', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('purchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mart.purchase')),
            ],
        ),
    ]