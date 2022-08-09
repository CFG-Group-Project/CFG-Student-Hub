from django import template

from ..models import BOXES, GlossaryCards

register = template.Library()

@register.inclusion_tag("flashcards/box_links.html")
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = GlossaryCards.objects.filter(box=box_num).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })

    return {"boxes": boxes}