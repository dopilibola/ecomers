from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress
from django.contrib import messages

def process_order(request):
    if request.POST:
        # Get Billing Info from the last page 
        payment_form = PaymentForm(request.POST or None)
        #  Get Shipping Session Date
        my_shipping = request.session.get('my_shipping')
        # print(my_shipping)

        # crate shipping address from session info 
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}\n"
        print(shipping_address)        


 

        messages.success(request, "Order Placed!")
        return redirect('home')

    else:
        messages.success(request, "Access Denied")
        return redirect('home')




def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # Create a session with Shipping Info 
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping


        # Check to see if user is logged in 
        if request.user.is_authenticated:
            # get the billing form
            billing_form = PaymentForm()
            return render(request, "billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form })
        else:
            # Not logged in
            # get the billing form
            billing_form = PaymentForm()
            return render(request, "billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form })


            shipping_form = request.POST
            return render(request, "billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        messages.success(request, "Access Dinied")
        return redirect('home')
    

def checkout(request):
    
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        # chakeaut as logged in user
        shipping_user = ShippingAddress.objects.get(id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user )
        return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        # chakeait as guest 
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})

    

def payment_success(request):

    return render(request, "payment_success.html", {})
