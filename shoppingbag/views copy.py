from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from courses.models import Course

# Create your views here.

def view_shoppingbag(request):
    """ A view that render the shopping bags content.  """

    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_shoppingbag(request, item_id):
    """ Add a quantity of the specified course to the shopping bag """

# courses
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
    else:
        shoppingbag[item_id] = quantity
     #   messages.success(request, f'Added {course.name}')



    request.session['shoppingbag'] = shoppingbag
    print(request.session['shoppingbag'])
    return redirect(redirect_url)


def adjust_shoppingbag(request, item_id):
    """Adjust the quantity of the specified course to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'course_size' in request.POST:
        size = request.POST['course_size']
    shoppingbag = request.session.get('shoppingbag', {})

    if size:
        if quantity > 0:
            shoppingbag[item_id]['items_by_size'][size] = quantity
        else:
            del shoppingbag[item_id]['items_by_size'][size]
            if not shoppingbag[item_id]['items_by_size']:
                shoppingbag.pop(item_id)
    else:
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
        if 'course_size' in request.POST:
            size = request.POST['course_size']
        shoppingbag = request.session.get('shoppingbag', {})

        if size:
            del shoppingbag[item_id]['items_by_size'][size]
            if not shoppingbag[item_id]['items_by_size']:
                shoppingbag.pop(item_id)
        else:
            shoppingbag.pop(item_id)

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)