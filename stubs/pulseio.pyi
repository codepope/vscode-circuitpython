import array
import microcontroller
import pulseio
from typing import Any

"""
pulseio
"""


# shared-bindings/pulseio/PulseIn.c:48
class PulseIn:
    def __init__(self, pin: microcontroller.Pin, maxlen: int = 2, *, idle_state: bool = False): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    def pause(self, ) -> Any: ...
    def resume(self, trigger_duration: int = 0) -> Any: ...
    def clear(self, ) -> Any: ...
    def popleft(self, ) -> Any: ...
    maxlen: Any = ...
    paused: Any = ...
    def __len__(self, ) -> Any: ...
    def __getitem__(self, index: Any) -> Any: ...

# shared-bindings/pulseio/PulseOut.c:48
class PulseOut:
    def __init__(self, carrier: pulseio.PWMOut): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    def send(self, pulses: array.array) -> Any: ...

# shared-bindings/pulseio/PWMOut.c:45
class PWMOut:
    def __init__(self, pin: microcontroller.Pin, *, duty_cycle: int = 0, frequency: int = 500, variable_frequency: bool = False): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    duty_cycle: Any = ...
    frequency: Any = ...
