from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Product, Format, Genre
from .forms import ProductForm

# Create your views here.

from django.views import generic


def all_products(request):
    """View to display all published products"""
    products = Product.productmanager.all()
    genres = None
    formats = None
    paginaton = Paginator(products, 8)
    page = request.GET.get('page')

    try:
        products = paginaton.page(page)
    except PageNotAnInteger:
        products = paginaton.page(1)
    except EmptyPage:
        products = paginaton.page(paginaton.num_pages)

    if request.GET:
        if "format" in request.GET:
            formats = request.GET["format"].split(",")
            products = Product.productmanager.filter(
                format__name__in=formats)
            formats = Format.objects.filter(name__in=formats)

        if "genre" in request.GET:
            genres = request.GET["genre"].split(",")
            products = Product.productmanager.filter(
                genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

    context = {
        'products': products,
        'current_formats': formats,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    format = Format.objects.all()
    genre = Genre.objects.all()

    context = {
        'product': product,
        'format': format,
        'genre': genre,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ View to add a product to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store administrators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ View to edit a product in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store administrators can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(
            request, f'You are editing: {product.name} - {product.artist}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))
