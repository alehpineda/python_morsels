from functools import wraps
from dataclasses import dataclass
from typing import Any, Optional

NO_RETURN = object()


def record_calls(func):  # Base problem
    @wraps(func)  # Bonus 1
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        call = Call(args, kwargs)
        wrapper.calls.append(call)
        try:  # Bonus 3
            call.return_value = func(*args, **kwargs)
        except BaseException as e:
            call.exception = e
            raise
        return call.return_value

    wrapper.calls = []
    wrapper.call_count = 0
    return wrapper


@dataclass
class Call:  # Bonus 2
    args: tuple
    kwargs: dict
    return_value: Any = NO_RETURN
    exception: Optional[BaseException] = None
