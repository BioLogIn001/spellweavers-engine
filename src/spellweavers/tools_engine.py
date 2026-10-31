import importlib
from typing import Any


def import_name(modulename: str, name: str) -> Any:
    """Import a named object from a module.

    Arguments:
      modulename (str): dotted module path
      name (str): attribute name to retrieve from the module
    """
    try:
        module = importlib.import_module(modulename)
    except ImportError as e:
        raise ModuleNotFoundError(f"Module {modulename} not found") from e
    return getattr(module, name)
