from django.conf.urls import url

from products.views import single_product, GetSingleProductView, AddItemToCartView, cart, checkout


urlpatterns = [
    url(r'^(?P<product_id>[\d]+)$', single_product, name="single_product"),
    # url(r'^api/(?P<product_id>[\d]+)', GetCartView.as_view()),
    url(r'^cart/$', cart, name="cart"),
    url(r'^cart/checkout$', checkout, name="checkout"),
    url(r'^api/(?P<product_id>[\d]+)$', GetSingleProductView.as_view()),
    url(r'^api/cart/(?P<product_id>[\d]+)$', AddItemToCartView.as_view()),

]
