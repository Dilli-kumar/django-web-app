from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'home/product_list.html', {'products': products, 'query': query})

@login_required
def profile(request):
    return render(request, 'home/profile.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    
    # Add product to cart session
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
    else:
        cart[product_id_str] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'image_url': product.image_url
        }
    
    request.session['cart'] = cart
    messages.success(request, f"{product.name} added to cart!")
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'home/cart.html', {'cart': cart, 'total': total})

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    messages.info(request, "Cart cleared.")
    return redirect('view_cart')
