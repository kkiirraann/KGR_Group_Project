# Generated by Django 2.2.4 on 2019-08-05 17:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Guest User', max_length=50)),
                ('phone_num', models.IntegerField(default=1234)),
                ('email_id', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='pass1234', max_length=30)),
                ('address', models.CharField(default='Hyderabad', max_length=50)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
                ('order_id', models.CharField(default='', max_length=25)),
            ],
        ),
    ]
