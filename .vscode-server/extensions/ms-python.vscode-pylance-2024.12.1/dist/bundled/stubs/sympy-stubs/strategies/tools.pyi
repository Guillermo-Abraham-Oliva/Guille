from typing import Any, Callable

def subs(d, **kwargs) -> Callable[[Any], Any] | Callable[..., Any]: ...
def canon(*rules, **kwargs) -> Callable[[Any], Any]: ...
def typed(ruletypes) -> Callable[[object], object]: ...