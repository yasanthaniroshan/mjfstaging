# Generated by Django 3.2.9 on 2021-12-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, verbose_name='Company Name')),
                ('number_of_workers', models.SmallIntegerField(default=1, verbose_name='Number of Workers')),
                ('your_position', models.CharField(max_length=100, verbose_name='Your Position')),
            ],
        ),
        migrations.CreateModel(
            name='Curent_user_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_of_users', models.PositiveIntegerField(default=1, verbose_name='Number of Users')),
                ('Number_of_sellers', models.PositiveIntegerField(default=1, verbose_name='Number of Sellers')),
                ('Number_of_buyers', models.PositiveIntegerField(default=1, verbose_name='Number of Buyers')),
                ('Number_of_collectors', models.PositiveIntegerField(default=1, verbose_name='Number of Collectors')),
                ('Number_of_transporters', models.PositiveIntegerField(default=1, verbose_name='Number of Transporters')),
            ],
        ),
    ]