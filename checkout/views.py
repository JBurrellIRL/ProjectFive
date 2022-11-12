from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your bag is empty')
        return redirect(reverse('products'))

    order_form = OrderForm
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LsRpoIXXs3N3e4kl8g5HjR5kj7sYDUkKzTCAkDskFOF46VFYwRRGJ9O9V1rOL3FEiMa3okPbgCN2AGkgwbqTSeW00ce5voGvv'
    }

    return render(request, template, context)
