# Generated by Django 5.2.1 on 2025-06-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0002_alter_category_category_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_logo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
