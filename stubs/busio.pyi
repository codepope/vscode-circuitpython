import Parity
import microcontroller
from typing import Any

"""
busio
"""


# shared-bindings/busio/OneWire.c:47
class OneWire:
    def __init__(self, pin: microcontroller.Pin): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    def reset(self, ) -> Any: ...
    def read_bit(self, ) -> Any: ...
    def write_bit(self, value: Any) -> Any: ...

# shared-bindings/busio/SPI.c:56
class SPI:
    def __init__(self, clock: microcontroller.Pin, MOSI: microcontroller.Pin = None, MISO: microcontroller.Pin = None): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    def configure(self, *, baudrate: int = 100000, polarity: int = 0, phase: int = 0, bits: int = 8) -> Any: ...
    def try_lock(self, ) -> Any: ...
    def unlock(self, ) -> Any: ...
    def write(self, buffer: bytearray, *, start: Any = 0, end: int = None) -> Any: ...
    def readinto(self, buffer: bytearray, *, start: Any = 0, end: int = None, write_value: int = 0) -> Any: ...
    def write_readinto(self, buffer_out: bytearray, buffer_in: bytearray, *, out_start: Any = 0, out_end: int = None, in_start: Any = 0, in_end: int = None) -> Any: ...
    frequency: Any = ...

# shared-bindings/busio/I2C.c:44
class I2C:
    def __init__(self, scl: microcontroller.Pin, sda: microcontroller.Pin, *, frequency: int = 400000, timeout: int = 255): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    def scan(self, ) -> Any: ...
    def try_lock(self, ) -> Any: ...
    def unlock(self, ) -> Any: ...
    def readfrom_into(self, address: int, buffer: bytearray, *, start: int = 0, end: int = None) -> Any: ...
    def writeto(self, address: int, buffer: bytearray, *, start: int = 0, end: int = None, stop: bool = True) -> Any: ...
    def writeto_then_readfrom(self, address: int, out_buffer: bytearray, in_buffer: bytearray, *, out_start: int = 0, out_end: int = None, in_start: int = 0, in_end: int = None) -> Any: ...

# shared-bindings/busio/UART.c:49
class UART:
    def __init__(self, tx: microcontroller.Pin, rx: microcontroller.Pin, *, baudrate: int = 9600, bits: int = 8, parity: Parity = None, stop: int = 1, timeout: float = 1, receiver_buffer_size: int = 64): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    def read(self, nbytes: Any = None) -> Any: ...
    def readinto(self, buf: Any) -> Any: ...
    def readline(self, ) -> Any: ...
    def write(self, buf: Any) -> Any: ...
    baudrate: Any = ...
    in_waiting: Any = ...
    timeout: Any = ...
    def reset_input_buffer(self, ) -> Any: ...

# shared-bindings/busio/UART.c:350
class busio:
    def __init__(self, ): ...
    ODD: Any = ...
    EVEN: Any = ...
