from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from etsy import views

urlpatterns = [
	url(r'^stats/$', views.stats),
	url(r'^item/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product-detail'),
	url(r'^$', views.ProductList.as_view()),
	url(r'^list/$', views.ProductList.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)