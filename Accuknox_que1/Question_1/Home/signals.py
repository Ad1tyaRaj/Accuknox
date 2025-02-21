from django.dispatch import Signal, receiver
from django.db.models.signals import pre_init,post_init

# This is Custom signal use
# Create a signal
my_Custom_signal = Signal()

@receiver(my_Custom_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler is running......")
    # some work performs
    for i in range(5):
        print(f"Working..... {i}")
    print("Signal handler finished.")

# Sending
print("About to send the signal...")
my_Custom_signal .send(sender=None)
print("Signal sent....")



# # This is Built-in signal use
#
# @receiver(pre_init,sender =None)
# def pre_init_signal(sender,**kwargs):
#     print("Signal handler is running...")
#     # Simulate some work
#     for i in range(5):
#         print(f"Working... {i}")
#     print("Signal handler finished.")

