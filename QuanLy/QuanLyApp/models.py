from _ast import mod, Attribute

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models import SET_NULL


class User(AbstractUser):
    pass


class UserRole(models.Model):
    nameRole = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Account(models.Model):
    fullname = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    gender = models.BooleanField()
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    avt = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    active = models.BooleanField()
    role = models.ForeignKey(UserRole,on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    nameCategory = models.CharField(max_length=50)
    att = models.ManyToManyField('Attribute')

    def __str__(self):
        return self.name


class Attribute(models.Model):
    nameAt = models .CharField(max_length=50)
    dataType = models.CharField(max_length=50)
    product = models.ManyToManyField('Product')

    def __str__(self):
        return self.name


class Store(models.Model):
    nameStore = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    active = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    nameProduct = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    status = models.BooleanField()
    quantity = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL,null=True)
    account = models.ForeignKey(Account, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    thumbnail = models.ImageField(upload_to='QuanLyApp/%Y/%m')
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class SearchHistory(models.Model):
    nameProduct = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    namePaymentType = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ShippingType(models.Model):
    nameShippingType = models.CharField(max_length=50)
    priceShippingType = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    shippingAddress = models.CharField(max_length=100)
    shippingFee = models.FloatField()
    note = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    status_pay = models.BooleanField()
    status_review = models.BooleanField()
    status_oder = models.BooleanField()
    account = models.ForeignKey(Account, on_delete=SET_NULL, null=True)
    paymentType = models.ForeignKey(PaymentType, on_delete=SET_NULL,null=True)
    shippingType = models.ForeignKey(ShippingType, on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.name


class OderDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.IntegerField()
    content = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=SET_NULL, null=True)
    store = models.ForeignKey(Store, on_delete=SET_NULL, null=True)
    order = models.ForeignKey(Order,on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    rating = models.IntegerField()
    content = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    reply_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    account = models.ForeignKey(Account, on_delete=SET_NULL, null=True)
    oderDetail = models.ForeignKey(OderDetail, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name