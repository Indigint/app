from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from inventory.models import PurchaseOrder, POLinkPurchase, Customer

# Create your views here.
def index(request):
    return render(request, 'inventory/user_index.html')

def admin_index(request):
    purchase_orders = PurchaseOrder.objects.all()
    context = {'purchase_orders': purchase_orders}
    return render(request, 'inventory/admin_index.html', context)

def po(request, PO_id):
    po1 = PurchaseOrder.objects.get(pk=PO_id)
    customer = po1.customer.name
    items = POLinkPurchase.objects.filter(po=po1.id)
    context = {'items': items, 'customer': customer}
    return render(request, 'inventory/po.html', context)
    #return HttpResponse("You're looking at PO #%s" % PO_id)
