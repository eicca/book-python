.. _Protocol Reflection:

**********
Reflection
**********


Rationale
=========
* When accessing an attribute
* Built-in Functions:

    * ``setattr(obj, 'attribute_name', 'new value') -> None``
    * ``delattr(obj, 'attribute_name') -> None``
    * ``getattr(obj, 'attribute_name', 'default value') -> Any``
    * ``hasattr(obj, 'attribute_name') -> bool``


Protocol
========
* ``__setattr__(self, attribute_name, value) -> None``
* ``__delattr__(self, attribute_name) -> None``
* ``__getattribute__(self, attribute_name, default) -> Any``
* ``__getattr__(self, attribute_name, default) -> Any``

.. code-block:: python

    class Reflection:

        def __setattr__(self, attribute_name, value):
            ...

        def __delattr__(self, attribute_name):
            ...

        def __getattribute__(self, attribute_name, default):
            ...

        def __getattr__(self, attribute_name, default):
            ...


Example
=======
.. code-block:: python

    class Immutable:
        def __setattr__(self, name, value):
            raise PermissionError('Immutable')

.. code-block:: python

    class Protected:
        def __setattr__(self, name, value):
            if name.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__setattr__(name, value)


Set Attribute
=============
* Called when trying to set attribute to a value
* Call Stack:

    * ``astro.name = 'Mark Watney'``
    * => ``setattr(astro, 'name', 'Mark Watney')``
    * => ``astro.__setattr__('name', 'Mark Watney')``

.. code-block:: python

    class Astronaut:

        def __setattr__(self, name, value):
            if name.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__setattr__(name, value)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    astro._salary = 100
    # Traceback (most recent call last):
    #     ...
    # PermissionError: Field is protected


Delete Attribute
================
* Called when trying to delete attribute
* Call stack:

    * ``del astro.name``
    * => ``delattr(astro, 'name')``
    * => ``astro.__delattr__(name)``

.. code-block:: python

    class Astronaut:

        def __delattr__(self, name):
            if name.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__delattr__(name)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    astro._salary = 100

    del astro.name
    del astro._salary
    # Traceback (most recent call last):
    #     ...
    # PermissionError: Field is protected


Get Attribute
=============
* Called for every time, when you want to access any attribute
* Before even checking if this attribute exists
* If attribute is not found, then raises ``AttributeError`` and calls ``__getattr__()``
* Call stack:

    * ``astro.name``
    * => ``getattr(astro, 'name')``
    * => ``astro.__getattribute__('name')``
    * if ``astro.__getattribute__('name')`` raises ``AttributeError``
    * => ``astro.__getattr__('name')``

.. code-block:: python

    class Astronaut:

        def __getattribute__(self, name):
            if name.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__getattribute__(name)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    print(astro._salary)
    # Traceback (most recent call last):
    #     ...
    # PermissionError: Field is protected


Get Attribute if Missing
========================
* Called whenever you request an attribute that hasn't already been defined
* It will not execute, when attribute already exist
* Implementing a fallback for missing attributes

.. code-block:: python
    :caption: Example ``__getattr__()``

    class Astronaut:
        def __init__(self):
            self.name = None

        def __getattr__(self, name):
            return 'Sorry, field does not exist'


    astro = Astronaut()
    astro.name = 'Mark Watney'

    print(astro.name)
    # Mark Watney

    print(astro._salary)
    # Sorry, field does not exist

.. code-block:: python

    class Astronaut:
        def __init__(self):
            self.name = None

        def __getattribute__(self, name):
            print('Getattribute called... ')
            result = super().__getattribute__(name)
            print(f'Result was: "{result}"')
            return result

        def __getattr__(self, name):
            print('Not found. Getattr called...')
            print(f'Creating attribute {name} with `None` value')
            super().__setattr__(name, None)


    astro = Astronaut()
    astro.name = 'Mark Watney'

    astro.name
    # Getattribute called...
    # Result was: "Mark Watney"

    astro._salary
    # Getattribute called...
    # Not found. Getattr called...
    # Creating attribute _salary with `None` value

    astro._salary
    # Getattribute called...
    # Result was: "None"


Has Attribute
=============
* Check if object has attribute
* There is no ``__hasattr__()`` method
* Calls ``__getattribute__()`` and checks if raises ``AttributeError``

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name


    astro = Astronaut('Mark Watney')

    hasattr(astro, 'name')
    # True

    hasattr(astro, 'mission')
    # False

    astro.mission = 'Ares3'
    hasattr(astro, 'mission')
    # True


Use Cases
=========
.. code-block:: python

    class Astronaut:

        def __getattribute__(self, name):
            if name.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__getattribute__(name)

        def __setattr__(self, name, value):
            if name.startswith('_'):
                raise PermissionError('Field is protected')
            else:
                return super().__setattr__(name, value)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    print(astro.name)
    # Mark Watney

    astro._salary = 100
    # Traceback (most recent call last):
    #     ...
    # PermissionError: Field is protected

    print(astro._salary)
    # Traceback (most recent call last):
    #     ...
    # PermissionError: Field is protected

.. code-block:: python

    class Temperature:
        kelvin: float

        def __init__(self, kelvin):
            self.kelvin = kelvin

        def __setattr__(self, name, value):
            if value < 0.0:
                raise ValueError('Kelvin temperature cannot be negative')
            else:
                return super().__setattr__(name, value)


    t = Temperature(100)

    t.kelvin = 20
    print(t.kelvin)
    # 20

    t.kelvin = -10
    # Traceback (most recent call last):
    #     ...
    # ValueError: Kelvin temperature cannot be negative

.. code-block:: python

    class Temperature:
        kelvin: float
        celsius: float
        fahrenheit: float

        def __setattr__(self, name, value):
            super().__setattr__(name, value)

            if name == 'celsius':
                self.kelvin = value + 273.15
                self.fahrenheit = value * (9/5) + 32


    t = Temperature()
    t.celsius = 100

    print(t.kelvin)
    # 373.15

    print(t.celsius)
    # 100

    print(t.fahrenheit)
    # 212.0


Assignments
===========

Protocol Reflection Delattr
---------------------------
* Assignment name: Protocol Reflection Delattr
* Last update: 2020-10-16
* Complexity level: easy
* Lines of code to write: 7 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/protocol_reflection_delattr.py`

:English:
    #. Create class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Prevent deleting attributes
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Zablokuj usuwanie atrybutów
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> pt = Point(1, 2, 3)
        >>> pt.x, pt.y, pt.z
        (1, 2, 3)

        >>> del pt.x
        Traceback (most recent call last):
            ...
        PermissionError: Cannot delete attributes

        >>> del pt.notexisting
        Traceback (most recent call last):
            ...
        PermissionError: Cannot delete attributes

Protocol Reflection Setattr
---------------------------
* Assignment name: Protocol Reflection Setattr
* Last update: 2020-10-16
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/protocol_reflection_setattr.py`

:English:
    #. Create class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Prevent creation of new attributes
    #. Allow to modify values of ``x``, ``y``, ``z``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Zablokuj tworzenie nowych atrybutów
    #. Zezwól na modyfikowanie wartości ``x``, ``y``, ``z``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> pt = Point(1, 2, 3)
        >>> pt.x, pt.y, pt.z
        (1, 2, 3)

        >>> pt.notexisting = 10
        Traceback (most recent call last):
            ...
        PermissionError: Cannot set other attributes than x,y,z

        >>> pt.x = 10
        >>> pt.y = 20
        >>> pt.z = 30

        >>> pt.x, pt.y, pt.z
        (10, 20, 30)

Protocol Reflection Frozen
--------------------------
* Assignment name: Protocol Reflection Frozen
* Last update: 2020-10-16
* Complexity level: easy
* Lines of code to write: 11 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_reflection_frozen.py`

:English:
    #. Create class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Prevent creation of new attributes
    #. Allow to define ``x``, ``y``, ``z`` but only at the initialization
    #. Prevent later modification of ``x``, ``y``, ``z``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Zablokuj tworzenie nowych atrybutów
    #. Pozwól na zdefiniowanie ``x``, ``y``, ``z`` ale tylko przy inicjalizacji
    #. Zablokuj późniejsze modyfikacje ``x``, ``y``, ``z``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> pt = Point(1, 2, 3)
        >>> pt.x, pt.y, pt.z
        (1, 2, 3)

        >>> pt.notexisting = 10
        Traceback (most recent call last):
            ...
        PermissionError: Cannot set other attributes than x,y,z

        >>> pt.x = 10
        Traceback (most recent call last):
            ...
        PermissionError: Cannot modify existing attributes
        >>> pt.y = 20
        Traceback (most recent call last):
            ...
        PermissionError: Cannot modify existing attributes
        >>> pt.z = 30
        Traceback (most recent call last):
            ...
        PermissionError: Cannot modify existing attributes
