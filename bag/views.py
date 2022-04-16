from django.shortcuts import redirect
from django.views.generic import TemplateView


class ViewBag(TemplateView):
    """Render bag view."""
    template_name = 'bag/bag.html'

def add_to_bag(request, item_id):
    """Add item to bag"""

    template = 'products/product_detail.html'
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # create bag object in the session to store number of items added
    # to bag, or grab it if already exists
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # overwrite bag in the session with updated one
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)