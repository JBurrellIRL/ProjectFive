from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category

# Create your views here.

from django.views import generic


def all_products(request):
    """A view to display all uploaded products"""

    products = Product.objects.all().order_by('?')
    categories = None
    paginaton = Paginator(products, 8)
    page = request.GET.get('page')
    # To allow people to search for products by category
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    # Pagination of product page
    try:
        products = paginaton.page(page)
    except PageNotAnInteger:
        products = paginaton.page(1)
    except EmptyPage:
        products = paginaton.page(paginaton.num_pages)

    context = {
        'products': products,
        'current_categories': categories
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to display the product detail page for each product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
