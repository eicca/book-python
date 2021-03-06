.. _Type Annotation:

***************
Type Annotation
***************


.. epigraph::
    Types are not required, and never will be
    -- Guido van Rossum, Python initiator, core developer, former BDFL


Rationale
=========
.. highlights::
    * Since Python 3.5, :pep:`484`, :pep:`526`, :pep:`544`
    * ``SyntaxError`` in Python before 3.5
    * Names: "type annotations", "type hints", "gradual typing"
    * Good IDE will give you hints
    * Types are used extensively in system libraries
    * More and more books and documentations use types
    * To type check use: ``mypy``, ``pyre-check``, ``pytypes``
    * More information in :ref:`cicd-tools`
    * https://www.infoq.com/presentations/dynamic-static-typing/


Int
===
.. code-block:: python

    data: int = 0
    data: int = 1
    data: int = -1


Float
=====
.. code-block:: python

    data: float = 0.0
    data: float = 1.23
    data: float = -1.23


Str
===
.. code-block:: python

    data: str = ''
    data: str = 'Jan Twardowski'


Bool
====
.. code-block:: python

    data: bool = True
    data: bool = False


Optional
========
.. code-block:: python

    from typing import Optional

    data: Optional[int] = 1
    data: Optional[int] = None

.. code-block:: python

    from typing import Optional


    firstname: str = 'Melissa'
    lastname: str = 'Lewis'
    age: Optional[float] = None


Union
=====
.. code-block:: python

    from typing import Optional

    data: Union[int, float] = 1
    data: Union[int, float] = 1.1


Final
=====
.. versionadded:: Python 3.8
    See :pep:`591`

.. code-block:: python

    from typing import Final


    m: Final[int] = 1
    km: Final[int] = 1000 * m

.. code-block:: python

    from typing import Final

    second: Final[int] = 1
    minute: Final[int] = 60 * second
    hour: Final[int] = 60 * hour
    day: Final[int] = 24 * day


Type Check is not Enforced
==========================
.. highlights::
    * This code will run without any problems
    * Although ``mypy`` or ``pyre-check`` will throw error

.. code-block:: python

    name: int = 'Jan Twardowski'
    age: float = 30
    is_adult: int = True


Future
======
.. versionadded:: Python 3.10
    :pep:`604` - Allow writing union types as X | Y

.. code-block:: python
    :caption: Union and Optional before Python 3.10

    from typing import Union, Optional

    age: Union[int, float] = 1337
    age: Optional[int] = 1337

.. code-block:: python

    age: int|float = 1337
    age: int|None = 1337


.. code-block:: python
    :caption: Result of this expression would then be valid in isinstance() and issubclass()

    isinstance(1337, int|None)
    isinstance(1337, int|float)
    issubclass(bool, int|float)


More Information
================
.. note:: More information in :ref:`Type Annotations` and :ref:`CI/CD Type Checking`
