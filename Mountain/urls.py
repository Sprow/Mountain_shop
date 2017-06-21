from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from products.views import products, cart

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', products, name="home"),

    # url(r'^cart/$', cart, name="cart"),

    url(r'^products/', include('products.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    # url(r'^cart/', include('cart.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

