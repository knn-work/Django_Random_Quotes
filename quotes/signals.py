from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from quotes.models import Quote
from quotes.views.random import update_total_weight


@receiver(post_save, sender=Quote)
def update_cache_if_weight_changed(sender, instance, created, update_fields, **kwargs):
    """
    Обновляет total_weight только при изменении поля 'weight'.
    """
    # Определяем, были ли переданы конкретные поля для обновления,
    # и если да, то проверяем, присутствует ли среди них 'weight'
    updated_weight = False
    if update_fields is not None:
        updated_weight = "weight" in update_fields
    elif (
        not created
    ):  # Если объект не создается впервые, проверяем фактическое изменение поля
        old_instance = sender.objects.get(pk=instance.pk)
        updated_weight = old_instance.weight != instance.weight

    if updated_weight:
        update_total_weight()


@receiver(post_delete, sender=Quote)
def handle_quote_deletion(sender, instance, **kwargs):
    """
    Обновление общей суммы весов при удалении цитаты.
    """
    update_total_weight()
