from django.contrib import admin
import inventory.models as inventory

# Register your models here.

# Customer
#admin.site.register(inventory.Customer)
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',  {'fields': ['name']}),
        ('Address', {'fields': ['street', 'city', 'zip']}),
        ('Contact', {'fields': ['phone', 'email']}),
    ]
    search_fields = ['name', 'zip', 'phone', 'email']
    list_filter = ['name', 'zip']
admin.site.register(inventory.Customer, CustomerAdmin)

# Item
#admin.site.register(inventory.Item)
class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['name', 'description', 'price']}),
        ('Stock', {'fields': ['style', 'quantity', 'vendor']}),
    ]
    search_fields = ['name', 'style', 'vendor']
    list_filter = ['name', 'price', 'quantity', 'vendor']
admin.site.register(inventory.Item, ItemAdmin)

# Vendor
#admin.site.register(inventory.Vendor)
class VendorAdmin(admin.ModelAdmin):
    search_fields = ['business_name']
    list_filter = ['business_name']
admin.site.register(inventory.Vendor, VendorAdmin)

# Purchase Order
class PurchaseOrderAdmin(admin.ModelAdmin):
    fields = ['customer', 'items']
    search_fields = ['customer']
    list_filter = ['customer', 'id']
admin.site.register(inventory.PurchaseOrder, PurchaseOrderAdmin)

admin.site.register(inventory.POLinkPurchase)
admin.site.register(inventory.CustomerLinkPO)
admin.site.register(inventory.Purchase)


