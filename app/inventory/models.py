from django.db import models

class Customer(models.Model):
    #ID is created automatically by Django
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Vendor(models.Model):
    #ID is created automatically by Django
    business_name = models.CharField(max_length=50)
    contact = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.business_name

class Item(models.Model):
    #ID is created automatically by Django
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    vendor = models.ForeignKey(Vendor)

    def __unicode__(self):
        return self.name + ' - ' + self.style

class Purchase(models.Model):
    #ID is created automatically by Django
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()

    def __unicode__(self):
        return self.id

class POLinkPurchase(models.Model):
    #ID is created automatically by Django
    po_number = models.IntegerField()
    purchase = models.ForeignKey(Purchase)

    def __unicode__(self):
        return self.id

class CustomerLinkPO(models.Model):
    #ID is created automatically by Django
    customer = models.ForeignKey(Customer)
    po = models.ForeignKey(POLinkPurchase)

    def __unicode__(self):
        return self.id