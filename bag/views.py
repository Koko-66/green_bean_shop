
"""Views for 'bag' app"""
from django.shortcuts import redirect
from django.views.generic import TemplateView


class ViewBag(TemplateView):
    """Render bag view."""
    template_name = 'bag/bag.html'


def add_to_bag(request, item_id):
    """Add item to bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    if 'color' in request.POST:
        color = request.POST['color']
    # create bag object in the session to store number of items added
    # to bag, or grab it if already exists
    bag = request.session.get('bag', {})

    str_item_id = str(item_id)

    if size:
        if str_item_id in list(bag.keys()):
            print('reached here')
            if size in bag[str_item_id]['items_by_size'].keys():
                bag[str_item_id]['items_by_size'][size] += quantity
            else:
                bag[str_item_id]['items_by_size'][size] = quantity
        else:
            bag[str_item_id] = {'items_by_size': {size: quantity}}
    else:
        if str_item_id in list(bag.keys()):
            bag[str_item_id] += quantity
        else:
            bag[str_item_id] = quantity

    # overwrite bag in the session with updated one
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
