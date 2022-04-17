
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
    color = None
    if 'size' in request.POST:
        size = request.POST['size']
    if 'color' in request.POST:
        color = request.POST['color']
    # create bag object in the session to store number of items added to bag,
    # or grab it if already exists.
    bag = request.session.get('bag', {})

    str_item_id = str(item_id)
    # Handle different types of products depending on whether they have size
    # or color, both or none. Check if item id already in bag with selected
    # color/size and update/create as needed.
    if size:
        if color:
            if str_item_id in list(bag.keys()):
                if size in bag[str_item_id]['items_by_size'].keys():
                    if color in bag[str_item_id]['items_by_size'][
                            size]['items_by_color'].keys():
                        bag[str_item_id]['items_by_size'][
                            size]['items_by_color'][color] += quantity
                    else:
                        bag[str_item_id]['items_by_size'][size][
                            'items_by_color'][color] = quantity
                else:
                    items_by_color = {'items_by_color': {color: quantity}}
                    bag[str_item_id]['items_by_size'][size] = items_by_color
            else:
                bag[str_item_id] = {'items_by_size': {size: {
                    'items_by_color': {color: quantity}}}}
        else:
            if str_item_id in list(bag.keys()):
                if size in bag[str_item_id]['items_by_size'].keys():
                    bag[str_item_id]['items_by_size'][size] += quantity
                else:
                    bag[str_item_id]['items_by_size'][size] = quantity
            else:
                bag[str_item_id] = {'items_by_size': {size: quantity}}
    # Handling products without size
    else:
        if color:
            if str_item_id in list(bag.keys()):
                if color in bag[str_item_id]['items_by_color'].keys():
                    bag[str_item_id]['items_by_color'][color] += quantity
                else:
                    bag[str_item_id]['items_by_color'][color] = quantity
            else:
                bag[str_item_id] = {'items_by_color': {color: quantity}}
        else:
            if str_item_id in list(bag.keys()):
                bag[str_item_id] += quantity
            else:
                bag[str_item_id] = quantity

    # overwrite bag in the session with updated one
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
