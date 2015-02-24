from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from inventory.models import PurchaseOrder, POLinkPurchase

# Create your views here.
def index(request):
    purchase_orders = PurchaseOrder.objects.all()
    context = {'purchase_orders': purchase_orders}
    '''
    response = ""
    for po in purchase_orders:
        response += po.customer.name + " ("
        items = POLinkPurchase.objects.filter(po=po.id)
        for it in items:
            response += str(it.purchase.quantity) + " " + it.purchase.item.name + ", "
        response += ") <br>"
    '''
    return render(request, 'inventory/index.html', context)

def po(request, PO_id):
    purchase_orders = PurchaseOrder.objects.filter(pk=PO_id)
    context = {'purchase_orders': purchase_orders}
    return render(request, 'inventory/po.html', context)
    #return HttpResponse("You're looking at PO #%s" % PO_id)

