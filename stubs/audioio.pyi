import microcontroller
from typing import Any

"""
audioio
"""


# shared-bindings/audioio/AudioOut.c:46
class AudioOut:
    def __init__(self, left_channel: microcontroller.Pin, *, right_channel: microcontroller.Pin = None, quiescent_value: int = 0x8000): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    def play(self, sample: Any, *, loop: Any = False) -> Any: ...
    def stop(self, ) -> Any: ...
    playing: Any = ...
    def pause(self, ) -> Any: ...
    def resume(self, ) -> Any: ...
    paused: Any = ...
