from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, Genre
from .forms import ProductForm

# Create your views here.

from django.views import generic


def all_products(request):
    """A view to display all uploaded products"""

    products = Product.objects.filter(status=1).order_by('?')
    genres = None
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
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = Product.objects.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "genre" in request.GET:
            genres = request.GET["genre"].split(",")
            products = Product.objects.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    
    form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
