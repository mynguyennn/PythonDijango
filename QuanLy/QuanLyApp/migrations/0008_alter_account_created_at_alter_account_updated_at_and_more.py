# Generated by Django 4.2.8 on 2023-12-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLyApp', '0007_alter_image_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(upload_to='QuanLyApp/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
