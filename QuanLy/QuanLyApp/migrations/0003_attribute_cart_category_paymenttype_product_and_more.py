# Generated by Django 4.2.8 on 2023-12-08 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLyApp', '0002_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameAt', models.CharField(max_length=50)),
                ('dataType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCategory', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePaymentType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProduct', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateField()),
                ('update_at', models.DateField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameShippingType', models.CharField(max_length=50)),
                ('priceShippingType', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='account',
            old_name='role_id',
            new_name='role',
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameStore', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('created_at', models.DateField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.account')),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProduct', models.CharField(max_length=50)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.account')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.product')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.store')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.account')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.store')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('att', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.attribute')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.store'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shippingAddress', models.CharField(max_length=100)),
                ('shippingFee', models.FloatField()),
                ('note', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
                ('status_pay', models.BooleanField()),
                ('status_review', models.BooleanField()),
                ('status_oder', models.BooleanField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.account')),
                ('paymentType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.paymenttype')),
                ('shippingType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.shippingtype')),
            ],
        ),
        migrations.CreateModel(
            name='OderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.cart')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.CharField(max_length=100)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.account')),
                ('oderDetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.oderdetail')),
                ('reply_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='QuanLyApp.comment')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.attribute')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.category')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.account'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuanLyApp.product'),
        ),
    ]
