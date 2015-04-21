from django.contrib.auth.models import User
from django.db import models

# TRACE: makes DB to store data

# TRACE: customer table
class Customer(models.Model):
    #ID is created automatically by Django
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    is_vendor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

# TRACE: vendor table
class Vendor(models.Model):
    #ID is created automatically by Django
    business_name = models.CharField(max_length=50)
    contact = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.business_name

# TRACE: item table
class Item(models.Model):
    #ID is created automatically by Django
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    vendor = models.ForeignKey(Vendor)

    def __unicode__(self):
        return self.name + ' (' + self.style + ')'

# TRACE: purchase table
class Purchase(models.Model):
    #ID is created automatically by Django
    quantity = models.IntegerField()
    item = models.ForeignKey(Item)

    def __unicode__(self):
        return self.item.name + ' ' + str(self.quantity)

# TRACE: purchase order table
class PurchaseOrder(models.Model):
    #ID is created automatically by Django
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return '#' + str(self.id) + ' ' + self.customer.name

# TRACE: link table for po table and purchase table
class POLinkPurchase(models.Model):
    #ID is created automatically by Django
    po = models.ForeignKey(PurchaseOrder)
    purchase = models.ForeignKey(Purchase)

    def __unicode__(self):
        return str(self.id)

# TRACE: Allows for registration and logins
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username