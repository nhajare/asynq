import threading
from typing import Any, List

class LocalProfileState(threading.local): ...

def flush() -> List[Any]: ...
def append(stats: Any) -> None: ...
def reset() -> None: ...
def incr_counter() -> int: ...
