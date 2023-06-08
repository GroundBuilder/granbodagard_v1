from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course


def shoppingbag_contents(request):

    shoppingbag_items = []
    total = 0
    course_count = 0
    shoppingbag = request.session.get('shoppingbag', {})

    for item_id, item_data in shoppingbag.items():
        if isinstance(item_data, int):
            course = get_object_or_404(Course, pk=item_id)
            total += item_data * course.price
            course_count += item_data
            shoppingbag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'course': course,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'course_count': course_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context