from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from product.models import Product
from .forms import RegistrationForm

class RegistrView(CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    succsess_url = reverse_lazy('home')


class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')

# cart views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, 'product/cart/cart_detail.html')
