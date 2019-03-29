from digi.xbee.devices import XBeeDevice

device = XBeeDevice("/dev/tty.usbserial-00000000", 9600)  # my macbook usb port
# device = XBeeDevice("/dev/ttyUSB0", 9600) # default usb port on raspberry Pi
device.open()


# Define callback.
def print_data_received_callback(xbee_message):
    sender = xbee_message.remote_device.get_64bit_addr()
    data = xbee_message.data.decode("utf8")
    timestamp = xbee_message.timestamp
    msg = """{time} from {sender}\n{data}""".format(
        time=timestamp, sender=sender, data=data)
    print(msg)


# Add the callback.
device.add_data_received_callback(print_data_received_callback)
