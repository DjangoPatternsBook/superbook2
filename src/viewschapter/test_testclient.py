"""
Chapter 4 example of views

>>> from django.test import Client
>>> c = Client()

>>> c.get("http://0.0.0.0:8000/hello-fn/").content
b'Hello World!'

>>> c.post("http://0.0.0.0:8000/hello-fn/").content
b'Hello World!'

>>> c.get("http://0.0.0.0:8000/hello-cl/").content
b'Hello World!'

>>> c.post("http://0.0.0.0:8000/hello-cl/").content # doctest: +SKIP
Method Not Allowed (POST): /hello-cl/
b''

"""


if __name__ == "__main__":
    import sys
    import os
    import django
    sys.path.append(os.path.abspath(".."))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "superbook.settings.development")
    django.setup()

    import doctest
    doctest.testmod()
