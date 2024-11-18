
def introspection_info(obj):
    dictionary = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getattr(obj, '__module__', None)
    }
    return dictionary


number_info = introspection_info(42)
print(number_info)
