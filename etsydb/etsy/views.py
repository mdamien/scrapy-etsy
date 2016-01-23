from django.shortcuts import render_to_response
from django.db.models import Count, Sum
from django.views.generic import ListView, DetailView

from .models import Product

def stats(request):
    by_views = Product.objects.order_by('-views')[:10]
    by_price = Product.objects.order_by('-price')[:10]
    by_reviews = Product.objects.order_by('-rating_count')[:10]
    shops_by_nb = Product.objects.values('shop') \
                .annotate(count=Count('shop')).order_by('-count')[:10]
    return render_to_response('stats.html', {
            'by_views': by_views,
            'by_price': by_price,
            'by_reviews': by_reviews,
            'shops_by_nb': shops_by_nb
        })


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'
    paginate_by = 100


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'