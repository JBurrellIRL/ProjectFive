from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    View to add items to the shopping bag
    """
    quantity = 1
    product = get_object_or_404(Product, pk=item_id)

    bag = request.session.get('bag', {})
    bag[item_id] = bag.get(item_id, quantity)
    messages.success(
        request, f'Added {product.artist} - {product.name} to your bag!')

    request.session['bag'] = bag

    return redirect(reverse('products'))


def remove_from_bag(request, item_id):
    """
    View to remove an item from the bag
    """
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.success(
        request, f'Removed {product.artist} - {product.name} from your bag.')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
