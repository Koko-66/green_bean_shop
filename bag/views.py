"""Views for 'bag' app"""
from django.contrib import messages
from django.shortcuts import (
    redirect,
    reverse,
    HttpResponse,
)
from django.views.generic import TemplateView
from products.models import Product


class ViewBag(TemplateView):
    """Render bag view."""
    template_name = 'bag/bag.html'


def add_to_bag(request, item_id):
    """Add item to bag"""

    product = Product.objects.get(pk=item_id)
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
                        messages.success(request, f'Updated quantity of \
                            <strong>{product.product_name} {size} \
                                {color}</strong>.')
                    else:
                        bag[str_item_id]['items_by_size'][size][
                            'items_by_color'][color] = quantity
                        messages.success(request, f'Added <strong> \
                        {product.product_name} {size} {color}\
                            </strong> to the bag.')
                else:
                    items_by_color = {'items_by_color': {color: quantity}}
                    bag[str_item_id]['items_by_size'][size] = items_by_color
                    messages.success(request, f'Added <strong>\
                        {product.product_name} {size}</strong> to the bag.')
            else:
                bag[str_item_id] = {'items_by_size': {size: {
                    'items_by_color': {color: quantity}}}}
                messages.success(request, f'Added <strong>\
                    {product.product_name} {size} {color}\
                        </strong> to the bag.')
        else:
            if str_item_id in list(bag.keys()):
                if size in bag[str_item_id]['items_by_size'].keys():
                    bag[str_item_id]['items_by_size'][size] += quantity
                    messages.success(request, f'Updated quantity of <strong>\
                        {product.product_name} {size}</strong>.')
                else:
                    bag[str_item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Added <strong>\
                        {product.product_name}</strong> to the bag.')
            else:
                bag[str_item_id] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added <strong>\
                    {product.product_name} {size}</strong> to the bag.')
    # Handling products without size
    else:
        if color:
            if str_item_id in list(bag.keys()):
                if color in bag[str_item_id]['items_by_color'].keys():
                    bag[str_item_id]['items_by_color'][color] += quantity
                    messages.success(request, f'Updated quantity of <strong>\
                        {product.product_name} {color}</strong>.')

                else:
                    bag[str_item_id]['items_by_color'][color] = quantity
                    messages.success(request, f'Added \
                        <strong>{product.product_name} {color}\
                            </strong> to the bag.')
            else:
                bag[str_item_id] = {'items_by_color': {color: quantity}}
                messages.success(request, f'Added <strong>\
                    {product.product_name} {color}</strong>\
                         to the bag.')
        else:
            if str_item_id in list(bag.keys()):
                bag[str_item_id] += quantity
                messages.success(request, f'Updated quantity of <strong>\
                    {product.product_name}</strong>.')
            else:
                bag[str_item_id] = quantity
                messages.success(request, f'Added <strong>\
                    {product.product_name}</strong> to the bag.')
    # overwrite bag in the session with updated one
    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust items in the bag"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    color = None
    if 'size' in request.POST:
        size = request.POST['size']
    if 'color' in request.POST:
        color = request.POST['color']
    bag = request.session.get('bag', {})
    str_item_id = str(item_id)
    # Handle different types of products depending on whether they have size
    # or color, both or none.
    if size:
        if color:
            if quantity > 0:
                bag[str_item_id]['items_by_size'][
                    size]['items_by_color'][color] = quantity
                messages.success(request, f'Updated quantity of <strong>\
                    {product.product_name} {size} {color}\
                    </strong>.')
            else:
                del bag[str_item_id]['items_by_size'][size][
                        'items_by_color'][color]
                if not bag[str_item_id]['items_by_size'][size][
                        'items_by_color']:
                    del bag[str_item_id]['items_by_size'][size]
                if not bag[str_item_id]['items_by_size']:
                    bag.pop(str_item_id)
                messages.success(request, f'Removed <strong>\
                    {product.product_name} {size} {color}\
                    </strong>.')
        else:
            if quantity > 0:
                bag[str_item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Updated quantity of <strong>\
                    {product.product_name} {size}</strong>.')
            else:
                del bag[str_item_id]['items_by_size'][size]
                if not bag[str_item_id]['items_by_size']:
                    bag.pop(str_item_id)
                messages.success(request, f'Removed <strong>\
                    {product.product_name} {size} {color}\
                        </strong>.')
    # Handling products without size
    else:
        if color:
            if quantity > 0:
                bag[str_item_id]['items_by_color'][color] = quantity
                messages.success(request, f'Updated quantity of <strong>\
                    {product.product_name} {color}</strong>.')
            else:
                del bag[str_item_id]['items_by_color'][color]
                if not bag[str_item_id]['items_by_color']:
                    bag.pop(str_item_id)
                messages.success(request, f'Removed <strong>\
                    {product.product_name} {color}</strong>.')
        else:
            if quantity > 0:
                bag[str_item_id] = quantity
                messages.success(request, f'Updated quantity of <strong>\
                    {product.product_name}</strong>.')
            else:
                bag.pop(str_item_id)
                messages.success(request, f'Removed <strong>\
                    {product.product_name}</strong>.')

    # Overwrite bag in the session with updated one
    request.session['bag'] = bag
    return redirect(reverse('bag:view_bag'))


def remove_item(request, item_id):
    """Remove item from the bag"""

    product = Product.objects.get(pk=item_id)
    try:
        size = None
        color = None
        if 'size' in request.POST:
            size = request.POST['size']
        if 'color' in request.POST:
            color = request.POST['color']
        bag = request.session.get('bag', {})

        str_item_id = str(item_id)
        # Handle different types of products depending on whether they
        # have size or color, both or none.
        if size:
            if color:
                del bag[str_item_id]['items_by_size'][size][
                    'items_by_color'][color]
                if not bag[str_item_id]['items_by_size'][size][
                        'items_by_color']:
                    del bag[str_item_id]['items_by_size'][size]
                if not bag[str_item_id]['items_by_size']:
                    bag.pop(str_item_id)
                messages.success(request, f'Removed <strong>\
                    {product.product_name} {size} {color}</strong>.')
            else:
                del bag[str_item_id]['items_by_size'][size]
                if not bag[str_item_id]['items_by_size']:
                    bag.pop(str_item_id)
                messages.success(request, f'Removed <strong>\
                    {product.product_name} {size}</strong>.')

        # Handling products without size
        else:
            if color:
                del bag[str_item_id]['items_by_color'][color]
                if not bag[str_item_id]['items_by_color']:
                    bag.pop(str_item_id)
                messages.success(request, f'Removed <strong>\
                    {product.product_name} {color}</strong>.')
            else:
                bag.pop(str_item_id)
                messages.success(request, f'Removed <strong>\
                    {product.product_name}</strong>.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
