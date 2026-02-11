import importlib


def import_name(modulename: str, name: str):
    """Import a named object from a module.

    Arguments:
      modulename (str): dotted module path
      name (str): attribute name to retrieve from the module
    """
    try:
      module = importlib.import_module(modulename)
    except ImportError:
      raise ModuleNotFoundError(f"Module {modulename} not found")
    return getattr(module, name)