from django import template

from ..models import Topics, Card

register = template.Library()

@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    boxes = []
    for box_num in Topics:
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })

    return {"boxes": boxes}