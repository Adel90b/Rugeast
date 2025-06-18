from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from oscar.core.loading import get_class

Product = get_class('catalogue.models', 'Product')
User = get_user_model()


@receiver(post_save, sender=Product)
def store_site(sender, instance, created, *args, **kwargs):
    """This signal will save current site to the all products explicitly """
    # Todo: Store sites to the products model
    print("Signal touched")
    return None