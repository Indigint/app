from django.db import models

class Customer(models.Model):
    #ID is created automatically by Django
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class Vendor(models.Model):
    #ID is created automatically by Django
    business_name = models.CharField(max_length=50)
    contact = models.ForeignKey(Customer)

class Item(models.Model):
    #ID is created automatically by Django
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    vendor = models.ForeignKey(Vendor)

class PurchaseOrder(models.Model):
    #ID is created automatically by Django
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()

class CustomerLinkPO(models.Model):
    #ID is created automatically by Django
    customer = models.ForeignKey(Customer)
    po = models.ForeignKey(PurchaseOrder)
