from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from courses.models import Course

# Create your views here.

def view_shoppingbag(request):
    """ A view that render the shopping bags content.  """

    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_shoppingbag(request, item_id):
    """ Add a quantity of the specified course to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    course = Course.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
    else:
        shoppingbag[item_id] = quantity




    request.session['shoppingbag'] = shoppingbag
    print(request.session['shoppingbag'])
    return redirect(redirect_url)


def adjust_shoppingbag(request, item_id):
    """Adjust the quantity of the specified course to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    shoppingbag = request.session.get('shoppingbag', {})

    if quantity > 0:
        shoppingbag[item_id] = quantity
    else:
        shoppingbag.pop(item_id)

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_shoppingbag'))


def remove_from_shoppingbag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        shoppingbag = request.session.get('shoppingbag', {})

        shoppingbag.pop(item_id)

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)