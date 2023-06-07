from django.shortcuts import render

# Create your views here.

def view_shoppingbag(request):
    """ A view that render the shopping bags content.  """

    return render(request, 'shoppingbag/shoppingbag.html')