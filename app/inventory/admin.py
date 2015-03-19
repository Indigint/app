from django.contrib import admin
import inventory.models as inventory

# Customer

# TRACE: Customer Table: Add
# TRACE: Customer Table: Delete
# TRACE: Customer Table: Edit

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'is_vendor']
    fieldsets = [
        ('Name',  {'fields': ['name']}),
        ('Address', {'fields': ['street', 'city', 'zip']}),
        ('Contact', {'fields': ['phone', 'email', 'is_vendor']}),
    ]
    search_fields = ['name', 'zip', 'phone', 'email']
    list_filter = ['name', 'zip']
admin.site.register(inventory.Customer, CustomerAdmin)

# Item

# TRACE: Items Table: Edit Table
# TRACE: Items Table: Add Items
# TRACE: Items Table: Edit Items

class ItemAdmin(admin.ModelAdmin):
    list_display = ['style', 'name', 'quantity', 'vendor']
    fieldsets = [
        ('Info', {'fields': ['name', 'description', 'price']}),
        ('Stock', {'fields': ['style', 'quantity', 'vendor']}),
    ]
    search_fields = ['name', 'style', 'vendor']
    list_filter = ['name', 'price', 'quantity', 'vendor']
admin.site.register(inventory.Item, ItemAdmin)

# Vendor

# TRACE: Vendor Table: Edit
# TRACE: Vendor Table: Add
# TRACE:Vendor Table: Delete

class VendorAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'contact']
    search_fields = ['business_name']
    list_filter = ['business_name']
admin.site.register(inventory.Vendor, VendorAdmin)

# Purchase Order

# TRACE: Purchase Order Table: Edit
# TRACE: Purchase Order Table: Add
# TRACE: Purchase Order Table: Delete

class PurchaseOrderAdmin(admin.ModelAdmin):
    fields = ['customer']
    search_fields = ['customer']
    list_filter = ['customer', 'id']
admin.site.register(inventory.PurchaseOrder, PurchaseOrderAdmin)

# Purchases

# TRACE: Customer Purchases Table: Edit
# TRACE: Customer Purchases Table: Add
# TRACE: Customer Purchases Table: Delete

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']
    search_fields = ['item']
    list_filter = ['item']
admin.site.register(inventory.Purchase, PurchaseAdmin)

# PO Link Purchase

# TRACE: Link Table: PO and Purchase: Edit
# TRACE: Link Table: PO and Purchase: Add
# TRACE: Link Table: PO and Purchase: Delete

admin.site.register(inventory.POLinkPurchase)

# User Profile
#admin.site.register(inventory.UserProfile)



