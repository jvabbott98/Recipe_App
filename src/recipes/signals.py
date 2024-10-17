from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Recipe

@receiver(m2m_changed, sender=Recipe.ingredients.through)
def recalculate_difficulty_on_ingredient_change(sender, instance, **kwargs):
    instance.calculate_difficulty()
    instance.save()