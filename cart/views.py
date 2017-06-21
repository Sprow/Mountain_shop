from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse

# from cart.forms import CartForm
from cart.models import Cart, CartItem
from products.models import Product


from django.conf import settings


# def add_to_cart(request, item_id, quantity):
#     cart = request.session.get('cart', {})
#     cart[item_id] = quantity
#     request.session['cart'] = cart

# def view_cart(request):
#     session = request.session
#     cart = session.get(settings.CART_SESSION_ID)
#     if not cart:
#         cart = session[settings.CART_SESSION_ID] = {}



# def view_cart(request):
#     cart = request.session.get('cart', {})
#
#
# def add_to_cart(request, item_id, quantity):
#     cart = request.session.get('cart', {})
#     cart[item_id] = quantity
#     request.session['cart'] = cart
#
# def add(request):
#     cart = Cart(request.session)
#     product = Product.objects.get(id=request.GET.get('product_id'))
#     cart.add(product, price=product.price)
#     return HttpResponse("Added")
#
# def show(request):
#     return render(request, 'shopping/show-cart.html')



# class CartView(FormView):
#     template_name = 'cart.html'
#     form_class = CartForm
#
#     def get(self, request, *args, **kwargs):
#         cart_id = self.request.session.get("cart_id")
#         if cart_id == None:
#             cart = Cart()
#             cart.save()
#             cart_id = cart.id
#             self.request.session["cart_id"] = cart_id
#         cart = Cart.objects.get(id=cart_id)
#
#     def add_to_cart(self, request, item_id, quantity):
#         cart = request.session.get('cart', {})
#         cart[item_id] = quantity
#         request.session['cart'] = cart
#
#         if not request.is_ajax():
#             form = self.get_form()
#             return self.render_to_response(self.get_context_data(form=form, cart=cart))
#
#         if request.is_ajax():
#             item_id = request.GET.get("product")
#             item_instance = get_object_or_404(Product, id=item_id)
#             cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item_instance)
#             if not created:
#                 cart_item.quantity += 1
#                 cart_item.save()
#
#             data = {}
#             return JsonResponse(data)
