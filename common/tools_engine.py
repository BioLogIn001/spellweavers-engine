def import_name(modulename, name):
    """Import a named object from a module in the context of this function.

    Source: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch15s04.html
    """
    try:
        module = __import__(modulename, globals(), locals(), [name])
    except ImportError:
        raise Exception("Module " + modulename + " not found")
        # return None
    return vars(module)[name]
