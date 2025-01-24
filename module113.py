import inspect
import types

def introspection_info(obj):
    """
    Функция для проведения интроспекции объекта и сбора его характеристик.
    
    Args:
        obj: Объект для исследования
    
    Returns:
        dict: Словарь с характеристиками объекта
    """
    
    info = {
        'type': type(obj).__name__,
        'class': str(type(obj)),
        'module': obj.__class__.__module__ if hasattr(obj, '__class__') else 'Неопределен'
    }

    
    try:
        info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]
    except Exception:
        info['attributes'] = []

    
    try:
        methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
        info['methods'] = methods
    except Exception:
        info['methods'] = []

    
    if isinstance(obj, (int, float, complex)):
        info['numeric_details'] = {
            'is_integer': isinstance(obj, int),
            'is_complex': isinstance(obj, complex)
        }
    
    elif isinstance(obj, str):
        info['string_details'] = {
            'length': len(obj),
            'is_alphanumeric': obj.isalnum(),
            'is_numeric': obj.isnumeric()
        }
    
    elif isinstance(obj, list):
        info['list_details'] = {
            'length': len(obj),
            'contains_only_numeric': all(isinstance(x, (int, float)) for x in obj)
        }
    
    elif inspect.isclass(obj):
        info['class_details'] = {
            'base_classes': [base.__name__ for base in obj.__bases__],
            'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
            'is_abstract': inspect.isabstract(obj)
        }
    
    elif callable(obj):
        info['function_details'] = {
            'is_builtin': inspect.isbuiltin(obj),
            'arguments': str(inspect.signature(obj)) if hasattr(obj, '__code__') else 'Недоступно'
        }

    return info


def demonstrate_introspection():
    print("Интроспекция числа:")
    number_info = introspection_info(42)
    print(number_info)

    print("\nИнтроспекция строки:")
    string_info = introspection_info("Hello, World!")
    print(string_info)

    print("\nИнтроспекция списка:")
    list_info = introspection_info([1, 2, 3, 4, 5])
    print(list_info)

    
    class CustomClass:
        def __init__(self, value):
            self.value = value
        
        def example_method(self):
            return self.value * 2

    print("\nИнтроспекция пользовательского класса:")
    custom_obj = CustomClass(10)
    custom_info = introspection_info(custom_obj)
    print(custom_info)

    print("\nИнтроспекция функции:")
    def sample_function(x, y):
        return x + y
    
    function_info = introspection_info(sample_function)
    print(function_info)


demonstrate_introspection()