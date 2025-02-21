from django.dispatch import Signal, receiver
import threading


my_Custom_signal = Signal()


@receiver(my_Custom_signal)
def my_signal_handler(sender, **kwargs):
    print(f"Signal handler is running in thread: {threading.get_ident()}")


def send_signal():
    print(f"Sending signal from thread: {threading.get_ident()}")
    my_Custom_signal.send(sender=None)

# observe the thread ID with this
send_signal()