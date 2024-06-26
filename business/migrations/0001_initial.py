# Generated by Django 4.2.9 on 2024-04-03 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateTimeField(verbose_name='rental date')),
                ('price', models.IntegerField()),
                ('Customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('car_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.car')),
            ],
        ),
    ]
