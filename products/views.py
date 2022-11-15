from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category

# Create your views here.

from django.views import generic


def all_products(request):
    """A view to display all uploaded products"""

    products = Product.objects.filter(status=1).order_by('?')
    categories = None
    paginaton = Paginator(products, 8)
    page = request.GET.get('page')

    try:
        products = paginaton.page(page)
    except PageNotAnInteger:
        products = paginaton.page(1)
    except EmptyPage:
        products = paginaton.page(paginaton.num_pages)
    
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = Product.objects.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to display the product detail page for each product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
