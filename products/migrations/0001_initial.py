# Generated by Django 3.2.9 on 2021-12-07 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category Title')),
                ('slug', models.SlugField(max_length=55, verbose_name='Category Slug')),
                ('description', models.TextField(blank=True, verbose_name='Category Description')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Category Image')),
                ('is_active', models.BooleanField(verbose_name='Is Active?')),
                ('available_products', models.PositiveIntegerField(default=0, verbose_name='Available Products')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=20, verbose_name='unit')),
                ('SI_Unit', models.BooleanField(verbose_name='is_SI_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Product Title')),
                ('unit', models.CharField(choices=[('Kg', 'Kg'), ('Unit', 'Unit')], max_length=20, verbose_name='Units')),
                ('slug', models.SlugField(max_length=160, verbose_name='Product Slug')),
                ('sku', models.CharField(max_length=255, unique=True, verbose_name='Unique Product ID (SKU)')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('detail_description', models.TextField(blank=True, null=True, verbose_name='Detail Description')),
                ('product_image', models.ImageField(blank=True, default='svg/avatar.svg', null=True, upload_to='', verbose_name='Product Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_active', models.BooleanField(verbose_name='Is Active?')),
                ('is_featured', models.BooleanField(verbose_name='Is Featured?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('available_units', models.PositiveIntegerField(default=1, verbose_name='Available Units')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Product Categoy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-updated_at',),
            },
        ),
    ]
