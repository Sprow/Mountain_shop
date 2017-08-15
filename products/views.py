from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.core import serializers
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product
from products.serializers import ProductSerializer
from products.forms import ProductsForm, DeleteItemFromCartForm, CheckoutForm, SearchForm

from rest_framework.views import APIView
from rest_framework.response import Response

from utils import gen_page_list

# def home_page(request):
#     return render(request, "home.html")


def products(request):
    cart = view_cart(request)
    products = Product.objects.all().order_by("-id")
    form = ProductsForm()
    search_form = SearchForm()
    if request.method == "GET":
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            classification = search_form.cleaned_data['classification']
            keyword = search_form.cleaned_data['keyword']
            price = search_form.cleaned_data['price']
            if not classification:
                classification = 'all'
            if not price:
                price = 'dont care'
            kwargs = {}
            if keyword:
                kwargs['title__icontains'] = keyword
            if classification !='all':
                kwargs['classification'] = classification
            if price !='dont care':
                if price =='<500':
                    kwargs['price__lte'] = 500
                elif price =='500-2000':
                    kwargs['price__gte'] = 500
                    kwargs['price__lte'] = 2000
                elif price =='>2000':
                    kwargs['price__gte'] = 2000
            products = Product.objects.filter(**kwargs)

    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            product_id = request.POST.get("product_id")
            add_item_to_cart(request, product_id=product_id, quantity=quantity)
            return HttpResponseRedirect(reverse("home"))

    paginator = Paginator(products, 5)
    page = request.GET.get('page', 1)
    last_page = paginator.num_pages
    paginator_gen_list = gen_page_list(int(page), paginator.num_pages)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "home.html", {"products": products,
                                         "cart": cart,
                                         "form": form,
                                         "last_page": last_page,
                                         "paginator_gen_list": paginator_gen_list,
                                         "search_form": search_form})


def cart(request):
    cart = view_cart(request)

    form = ProductsForm()
    delete_form = DeleteItemFromCartForm()
    if request.method == "POST":
        if 'create' in request.POST:
            form = ProductsForm(request.POST)
            if form.is_valid():
                quantity = form.cleaned_data["quantity"]
                product_id = request.POST.get("product_id")
                add_item_to_cart(request, product_id=product_id, quantity=quantity)
        elif 'delete' in request.POST:
            delete_item = delete_item_from_cart(request, (request.POST.get("product_id")))

    total_price = cart_full_price(request)

    return render(request, "cart.html", {"cart": cart,
                                         "total_price": total_price,
                                         "form": form,
                                         "delete_form": delete_form})


def single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = view_cart(request)

    form = ProductsForm()
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            add_item_to_cart(request, product_id=product_id, quantity=quantity)

    return render(request, "single_product.html", {"product": product,
                                                   "cart": cart,
                                                   "form": form})


def view_cart(request):
    cart = request.session.get('cart', [])
    products_list = []
    for item in cart:
        for key, val in item.items():
            k = Product.objects.get(pk=key)
            products_list.append({k: val})
    return products_list

def add_item_to_cart(request, product_id, quantity):
    product_check = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', [])
    if cart:
        for product in cart:
            for key, val in product.items():
                if key != product_id:
                    continue
                else:
                    if val != quantity:
                        product[key] = quantity
                        request.session['cart'] = cart
    if {product_id: quantity} not in cart:
        cart.append({product_id: quantity})
        request.session['cart'] = cart


def delete_item_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    for item in cart:
        for key, val in item.items():
            if key == product_id:
                cart.remove(item)
                request.session['cart'] = cart


def cart_full_price(request):
    cart = request.session.get('cart', [])
    total_price = 0
    for item in cart:
        for key, val in item.items():
            k = Product.objects.get(pk=key)
            total_price += int(k.price) * int(val)
    return total_price


def checkout(request):
    form = CheckoutForm()
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            send_mail('Mountain shop list',
                      'qwd qwd qwd',
                      'ts.sprow@gmail.com',
                      ['jonnymountaintest@gmail.com'],
                      fail_silently=False)

            # send_mail('Mountain shop list',
            #           'bbbbbbbbb',
            #           'ts.sprow@gmail.com',
            #           [form.cleaned_data['email']],
            #           fail_silently=False)

            # msg = 'asasda'
            # from_addr = 'ts.sprow@gmail.com'
            # password = ''
            # to_addr = 'ts.sprow@gmail.com'
            # s = smtplib.SMTP_SSL('smtp.gmail.com')
            # s.login(from_addr, password)
            # s.sendmail(from_addr, [to_addr], msg)
    return render(request, "checkout.html", {"form": form})



class GetSingleProductView(APIView):
    serializer_class = ProductSerializer

    def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(product_id)
        return Response(self.serializer_class(product).data)


class AddItemToCartView(APIView):
    serializer_class = ProductSerializer

    def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(product_id)
        cart = self.request.session.get('cart', {})
        cart[product_id] = product
        return Response(cart)
