from django.contrib import admin
import inventory.models as inventory

# Register your models here.
admin.site.register(inventory.Customer)
admin.site.register(inventory.Vendor)
admin.site.register(inventory.Item)
admin.site.register(inventory.PurchaseOrder)
admin.site.register(inventory.CustomerLinkPO)
