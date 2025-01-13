import random
from typing import (
    Protocol, 
    runtime_checkable, 
    Any,
    Iterable,
    TYPE_CHECKING
)


@runtime_checkable
class RandomPicker(Protocol):
    def pick(self) -> Any: ...


# Extending RandoPicker
@runtime_checkable
class LoadableRandomPicker(RandomPicker, Protocol):
    def load(self, Iterable) -> None: ...


class SimplePicker:
    def __init__(self, items: Iterable) -> None:
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self) -> Any:
        return self._items.pop()
    

def test_isinstance() -> None:
    popper: RandomPicker = SimplePicker([1])
    assert isinstance(popper, RandomPicker)


def test_item_type() -> None:
    items = [1, 2]
    popper = SimplePicker(items)
    item = popper.pick()
    assert item in items
    if TYPE_CHECKING:
        reveal_type(item)
    assert isinstance(item, int)