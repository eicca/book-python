.. _OOP Abstract Class:

**************
Abstract Class
**************


Rationale
=========
* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation

.. glossary::

    abstract class
        Class which can only be inherited, not instantiated

    abstract method
        Method must be implemented in a subclass

    abstract static method
        Static method which must be implemented in a subclass


Example
=======
.. code-block:: python

    from abc import ABC, abstractmethod


    class Astronaut(ABC):

        @abstractmethod
        def say_hello(self):
            pass


    astro = Astronaut()
    # Traceback (most recent call last):
    #     ...
    # TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Astronaut(metaclass=ABCMeta):

        @abstractmethod
        def say_hello(self):
            pass


    astro = Astronaut()
    # Traceback (most recent call last):
    #     ...
    # TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello


Errors
======
.. code-block:: python
    :caption: In order to use Abstract Base Class you must create abstract method. Otherwise it won't prevent from instantiating.

    from abc import ABC

    class Astronaut(ABC):
        pass

    astro = Astronaut()
    print('no errors')
    # no errors

.. code-block:: python
    :caption: In order to use Abstract Base Class you must create abstract method. Otherwise it won't prevent from instantiating.

    from abc import ABCMeta

    class Astronaut(metaclass=ABCMeta):
        pass

    astro = Astronaut()
    print('no errors')
    # no errors

.. code-block:: python
    :caption: Must implement all abstract methods

    from abc import ABCMeta, abstractmethod

    class Human(metaclass=ABCMeta):
        @abstractmethod
        def say_hello(self):
            pass

    class Astronaut(Human):
        pass


    astro = Astronaut()
    # Traceback (most recent call last):
    #     ...
    # TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello

.. code-block:: python
    :caption: ``abc`` is common name and it is very easy to create file, variable lub module with the same name as the library, hence overwrite it. In case of error. Check all entries in ``sys.path`` or ``sys.modules['abc']`` to find what is overwriting it.

    from pprint import pprint
    import sys


    sys.modules['abc']
    # <module 'abc' from '/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/python3.8/abc.py'>

    pprint(sys.path)
    # ['/Users/matt/Developer/book-python/advanced/oop/solution',
    #   '/Applications/PyCharm 2020.2 EAP.app/Contents/plugins/python/helpers/pydev',
    #   '/Users/matt/Developer/book-python',
    #   '/Users/matt/Developer/book-python/_tmp',
    #   '/Applications/PyCharm 2020.2 '
    #   'EAP.app/Contents/plugins/python/helpers/pycharm_display',
    #   '/Applications/PyCharm 2020.2 '
    #   'EAP.app/Contents/plugins/python/helpers/third_party/thriftpy',
    #   '/Applications/PyCharm 2020.2 EAP.app/Contents/plugins/python/helpers/pydev',
    #   '/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
    #   '/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
    #   '/usr/local/Cellar/python@3.8/3.8.3/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
    #   '/Users/matt/Developer/book-python/.venv-3.8.3/lib/python3.8/site-packages',
    #   '/Applications/PyCharm 2020.2 '
    #   'EAP.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend',
    #   '/Users/matt/Developer/book-python',
    #   '/Users/matt/Developer/book-python/_tmp']


Use Cases
=========
.. code-block:: python
    :caption: Abstract Class

    from abc import ABC, abstractmethod


    class Document(ABC):
        def __init__(self, filename):
            self.filename = filename
            self.content = self._read_file_content(filename)

        def _read_file_content(self):
            with open(self.filename, mode='rb') as file:
                return file.read()

        @abstractmethod
        def display(self, content):
            pass


    class PDFDocument(Document):
        def display(self):
            # display self.content as PDF Document

    class WordDocument(Document):
        def display(self):
            # display self.content as Word Document


    file1 = PDFDocument('filename.pdf')
    file1.display()

    file2 = Document('filename.txt')
    # Traceback (most recent call last):
    #     ...
    # TypeError: Can't instantiate abstract class Document with abstract method display


Assignments
===========

OOP Abstract Define
-------------------
* Assignment name: OOP Abstract Define
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/oop_abstract_define.py`

:English:
    #. Create abstract class ``Iris``
    #. Create abstract method ``get_name()`` in ``Iris``
    #. Create class ``Setosa`` inheriting from ``Iris``
    #. Try to create instance of a class ``Setosa``
    #. Try to create instance of a class ``Iris``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz klasę abstrakcyjną ``Iris``
    #. Stwórz metodę abstrakcyjną ``get_name()`` w ``Iris``
    #. Stwórz klasę ``Setosa`` dziedziczące po ``Iris``
    #. Spróbuj stworzyć instancje klasy ``Setosa``
    #. Spróbuj stworzyć instancję klasy ``Iris``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

.. note::
    * Last line of doctest, second to last word of ``TypeError`` message
    * In Python 3.7, 3.8 there is "methods" word in doctest
    * In Python 3.9 there is "method" word in doctest
    * So it differs by "s" at the end of "method" word

:Output:
    .. code-block:: text

        >>> iris = Iris()
        Traceback (most recent call last):
          ...
        TypeError: Can't instantiate abstract class Iris with abstract method get_name

        >>> setosa = Setosa()

OOP Abstract Interface
----------------------
* Assignment name: OOP Abstract Interface
* Last update: 2020-10-14
* Complexity level: easy
* Lines of code to write: 14 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_abstract_interface.py`

:English:
    #. Define abstract class ``IrisAbstract``
    #. Attributes: ``sepal_length, sepal_width, petal_length, petal_width``
    #. Methods: ``sum()``, ``len()``, ``mean()``
    #. All methods and constructor must raise exception ``NotImplementedError``
    #. Create class ``Setosa`` inheriting from ``IrisInterface``
    #. Implement interface
    #. Compare result with "Output" section (see below)

:Polish:
    #. Zdefiniuj klasę abstrakcyjną ``IrisAbstract``
    #. Attributes: ``sepal_length, sepal_width, petal_length, petal_width``
    #. Metody: ``sum()``, ``len()``, ``mean()``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isabstract
        >>> assert isabstract(IrisAbstract)
        >>> assert hasattr(IrisAbstract, 'mean')
        >>> assert hasattr(IrisAbstract, 'sum')
        >>> assert hasattr(IrisAbstract, 'len')
