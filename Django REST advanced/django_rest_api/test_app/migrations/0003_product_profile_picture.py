# Generated by Django 3.2.8 on 2021-10-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='profile_picture',
            field=models.ImageField(default='2.jpg', upload_to='Images'),
        ),
    ]
