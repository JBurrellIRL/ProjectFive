from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    View to add items to the shopping bag
    """
    quantity = 1

    bag = request.session.get('bag', {})
    bag[item_id] = bag.get(item_id, quantity)

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(reverse('products'))
