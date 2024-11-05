from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def cart_summary(request):

    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})


def cart_add(request):

    cart = Cart(request)

    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))



        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()
        messages.success(request, ("Product Added To Cart..."))

        # return JsonResponse({'Product Name': product.name})
        return JsonResponse({'qty': cart_quantity})
    return HttpResponse("Invalid request", status=400)






def cart_delete(request):
    cart = Cart(request)
    
    # if request.POST.get('action') == 'POST':
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        messages.success(request, ("delete..."))

        response = JsonResponse({'product':product_id})
        return response
        # return redirect('cart_summary')

    return JsonResponse({'eror': 'Invalid action'}, status=400)






def cart_update(request):
    cart = Cart(request)
    
    # if request.POST.get('action') == 'POST':
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # print(f"Product ID: {product_id}")
        # print(f"Product Quantity: {product_qty}")

        cart.update(product=product_id, quantity=product_qty)
        messages.success(request, ("Your cart hes been update..."))

        response = JsonResponse({'qty':product_qty})
        return response
        # return redirect('cart_summary')
    return JsonResponse({'eror': 'Invalid action'}, status=400)