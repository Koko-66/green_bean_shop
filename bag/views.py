from django.shortcuts import redirect
from django.views.generic import TemplateView


class ViewBag(TemplateView):
    """Render bag view."""
    template_name = 'bag/bag.html'

def add_to_bag(request, pk):
    """Add item to bag"""

    template = 'products/product_detail.html'
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # get bag if exists, if not initiate an empty dictionary
    bag = request.session.get('bag', {})

    if pk in list(bag.keys()):
        bag[pk] += quantity
    else:
        bag[pk] = quantity

    # overwrite bag in the session with updated one
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)