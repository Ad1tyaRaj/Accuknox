from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

# Signal handler
@receiver(post_save, sender=MyModel)
def mymodel_post_save(sender, instance, **kwargs):
    print(f"Signal handler executed! Instance: {instance.name}")




# ____________________________________________
# def test_signal_transaction():
#     try:
#         with transaction.atomic():
#
#             obj = MyModel(name="Test Object")
#             obj.save()
#
#
#             raise Exception("Forcing a rollback")
#     except Exception as e:
#         print(f"Exception caught: {e}")
#
#
#     if MyModel.objects.filter(name="Test Object").exists():
#         print("Object exists in the database!")
#     else:
#         print("Object does not exist in the database.")
#
#
# test_signal_transaction()


# Username: admin
# Password: admin