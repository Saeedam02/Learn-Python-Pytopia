# Instance Method, Static Method, Class Method
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# more details are avalible at:
# https://github.com/pytopia/Python/blob/main/Python/04.%20Advanced/03.3%20Decorating%20Classes.ipynb