# Generated by Django 4.2.1 on 2023-06-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_name_alter_products_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(upload_to='media/%Y/%m/%d/', verbose_name='фотография'),
        ),
    ]
