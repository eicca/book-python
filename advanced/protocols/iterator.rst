.. _Protocol Iterator:

********
Iterator
********


Rationale
=========
* Used for iterating in a ``for`` loop


Protocol
========
* ``__iter__(self) -> self``
* ``__next__(self) -> raise StopIteration``
* ``iter(obj)`` -> ``obj.__iter__()``
* ``next(obj)`` -> ``obj.__next__()``

.. code-block:: python

    class Iterator:
        def __iter__(self):
            self._current = 0
            return self

        def __next__(self):
            if self._current >= len(self.values):
                raise StopIteration

            element = self.values[self._current]
            self._current += 1
            return element


Example
=======
.. code-block:: python

    class Crew:
        def __init__(self):
            self.members = list()

        def __iadd__(self, other):
            self.members.append(other)
            return self

        def __iter__(self):
            self._current = 0
            return self

        def __next__(self):
            if self._current >= len(self.members):
                raise StopIteration

            result = self.members[self._current]
            self._current += 1
            return result


    crew = Crew()
    crew += 'Mark Watney'
    crew += 'Jose Jimenez'
    crew += 'Melissa Lewis'

    for member in crew:
        print(member)

    # Mark Watney
    # Jose Jimenez
    # Melissa Lewis


Loop and Iterators
==================
.. code-block:: python
    :caption: For loop

    DATA = [1, 2, 3]

    for current in DATA:
        print(current)

.. code-block:: python
    :caption: Intuitive implementation of the ``for`` loop

    DATA = [1, 2, 3]
    iterator = iter(DATA)

    try:
        current = next(iterator)
        print(current)

        current = next(iterator)
        print(current)

        current = next(iterator)
        print(current)

        current = next(iterator)
        print(current)
    except StopIteration:
        pass

.. code-block:: python
    :caption: Intuitive implementation of the ``for`` loop

    DATA = [1, 2, 3]
    iterator = DATA.__iter__()

    try:
        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)
    except StopIteration:
        pass


Built-in Type Iteration
=======================
.. code-block:: python
    :caption: Iterating ``str``

    for character in 'hello':
        print(character)

    # h
    # e
    # l
    # l
    # o

.. code-block:: python
    :caption: Iterating sequences

    for number in [1, 2, 3]:
        print(number)

    # 1
    # 2
    # 3

.. code-block:: python
    :caption: Iterating ``dict``

    DATA = {'a': 1, 'b': 2, 'c': 3}

    for element in DATA:
        print(element)

    # a
    # b
    # c

.. code-block:: python
    :caption: Iterating ``dict``

    for key, value in DATA.items():
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3

.. code-block:: python
    :caption: Iterating nested sequences

    for key, value in [('a',1), ('b',2), ('c',3)]:
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3


Use Cases
=========
.. code-block:: python
    :caption: Iterator implementation

    class Parking:
        def __init__(self):
            self._parked_cars = list()

        def park(self, car):
            self._parked_cars.append(car)

        def __iter__(self):
            self._current = 0
            return self

        def __next__(self):
            if self._current >= len(self._parked_cars):
                raise StopIteration

            element = self._parked_cars[self._current]
            self._current += 1
            return element


    parking = Parking()
    parking.park('Mercedes')
    parking.park('Maluch')
    parking.park('Toyota')

    for car in parking:
        print(car)

    # Mercedes
    # Maluch
    # Toyota


.. _Itertools:

Standard Library Itertools
==========================
* ``import itertools``

.. code-block:: python
    :caption: ``itertools.count(start=0, step=1)``

    from itertools import count


    data = count(3, 2)

    next(data)
    # 3

    next(data)
    # 5

    next(data)
    # 7

.. code-block:: python
    :caption: ``itertools.cycle(iterable)``

    from itertools import cycle

    DATA = ['white', 'gray']

    for color in cycle(DATA):
        print(color)

    # white
    # gray
    # white
    # gray
    # ...

.. code-block:: python
    :caption: ``itertools.cycle(iterable)``

    from itertools import cycle

    DATA = ['even', 'odd']

    for i, status in enumerate(cycle(DATA)):
        print(i, status)

    # 0, even
    # 1, odd
    # 2, even
    # 3, odd
    # ...

.. code-block:: python
    :caption: ``itertools.repeat(object[, times])``

    from itertools import repeat

    data = repeat(10, 3)
    data
    # repeat(10, 3)

    next(data)
    # 10

    next(data)
    # 10

    next(data)
    # 10

    next(data)
    # Traceback (most recent call last):
    #   ...
    # StopIteration

.. code-block:: python
    :caption: ``itertools.accumulate(iterable[, func, *, initial=None])``

    from itertools import accumulate

    data = accumulate([1, 2, 3, 4])

    next(data)
    # 1

    next(data)
    # 3

    next(data)
    # 6

    next(data)
    # 10

    next(data)
    # Traceback (most recent call last):
    #   ...
    # StopIteration


.. code-block:: python
    :caption: ``itertools.chain(*iterables)``

    from itertools import chain


    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    for x in chain(keys, values):
        print(x)

    # a
    # b
    # c
    # 1
    # 2
    # 3

.. code-block:: python
    :caption: ``itertools.chain(*iterables)``

    from itertools import chain


    class Iterator:
        def __iter__(self):
            self._current = 0
            return self

        def __next__(self):
            if self._current >= len(self.values):
                raise StopIteration

            element = self.values[self._current]
            self._current += 1
            return element


    class Character(Iterator):
        def __init__(self, *values):
            self.values = values


    class Number(Iterator):
        def __init__(self, *values):
            self.values = values


    chars = Character('a', 'b', 'c')
    nums = Number(1, 2, 3)

    print(chain(chars, nums))
    # <itertools.chain object at 0x116166970>

    print(list(chain(chars, nums)))
    # [1, 2, 3, 'a', 'b', 'c']

    for x in chain(chars, nums):
        print(x)

    # a
    # b
    # c
    # 1
    # 2
    # 3

.. code-block:: python
    :caption: ``itertools.compress(data, selectors)``

    from itertools import compress


    data = compress('ABCDEF', [1,0,1,0,1,1])

    next(data)
    # 'A'

    next(data)
    # 'C'

    next(data)
    # 'E'

    next(data)
    # 'F'

    next(data)
    # Traceback (most recent call last):
    #   ...
    # StopIteration

.. code-block:: python
    :caption: ``itertools.islice(iterable, start, stop[, step])``

    from itertools import islice


    data = islice('ABCDEFG', 2, 6, 2 )

    next(data)
    # 'C'

    next(data)
    # 'E'

    next(data)
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    # StopIteration

.. code-block:: python
    :caption: ``itertools.starmap(function, iterable)``

    from itertools import starmap


    data = starmap(pow, [(2,5), (3,2), (10,3)])

    next(data)
    # 32

    next(data)
    # 9

    next(data)
    # 1000

    next(data)
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    # StopIteration

.. code-block:: python
    :caption: ``itertools.product(*iterables, repeat=1)``

    from itertools import product


    data = product(['a', 'b', 'c'], [1,2])

    next(data)
    # ('a', 1)

    next(data)
    # ('a', 2)

    next(data)
    # ('b', 1)

    next(data)
    # ('b', 2)

    next(data)
    # ('c', 1)

    next(data)
    # ('c', 2)

    next(data)
    # Traceback (most recent call last):
    #   ...
    # StopIteration

.. code-block:: python
    :caption: ``itertools.permutations(iterable, r=None)``

    from itertools import permutations


    data = permutations([1,2,3])

    next(data)
    # (1, 2, 3)

    next(data)
    # (1, 3, 2)

    next(data)
    # (2, 1, 3)

    next(data)
    # (2, 3, 1)

    next(data)
    # (3, 1, 2)

    next(data)
    # (3, 2, 1)

    next(data)
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    # StopIteration

.. code-block:: python
    :caption: ``itertools.combinations(iterable, r)``

    from itertools import combinations


    data = combinations([1, 2, 3, 4], 2)

    next(data)
    # (1, 2)

    next(data)
    # (1, 3)

    next(data)
    # (1, 4)

    next(data)
    # (2, 3)

    next(data)
    # (2, 4)

    next(data)
    # (3, 4)

    next(data)
    # Traceback (most recent call last):
    #   ...
    # StopIteration

.. code-block:: python
    :caption: ``itertools.combinations_with_replacement(iterable, r)``

    from itertools import combinations_with_replacement


    data = combinations_with_replacement([1,2,3], 2)

    next(data)
    # (1, 1)

    next(data)
    # (1, 2)

    next(data)
    # (1, 3)

    next(data)
    # (2, 2)

    next(data)
    # (2, 3)

    next(data)
    # (3, 3)

    next(data)
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    # StopIteration

.. code-block:: python
    :caption: ``itertools.groupby(iterable, key=None)``. Make an iterator that returns consecutive keys and groups from the iterable. Generally, the iterable needs to already be sorted on the same key function. The operation of groupby() is similar to the uniq filter in Unix. It generates a break or new group every time the value of the key function changes. That behavior differs from SQL’s GROUP BY which aggregates common elements regardless of their input order.

    from itertools import groupby

    data = groupby('AAAABBBCCDAABBB')

    next(data)
    # ('A', <itertools._grouper object at 0x1215f5c70>)

    next(data)
    # ('B', <itertools._grouper object at 0x12157b4f0>)

    next(data)
    # ('C', <itertools._grouper object at 0x120e16ee0>)

    next(data)
    # ('D', <itertools._grouper object at 0x1215ef4c0>)

    next(data)
    # ('A', <itertools._grouper object at 0x12157b3a0>)

    next(data)
    # ('B', <itertools._grouper object at 0x12157b790>)

    next(data)
    # Traceback (most recent call last):
    #   ...
    # StopIteration

    [k for k, g in groupby('AAAABBBCCDAABBB')]
    # A B C D A B

    [list(g) for k, g in groupby('AAAABBBCCD')]
    # AAAA BBB CC D


Assignments
===========

Protocol Iterator Implementation
--------------------------------
* Assignment name: Protocol Iterator Implementation
* Last update: 2020-10-02
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/protocol_iterator_implementation.py`

:English:
    #. Use data from "Input" section (see below)
    #. Modify classes to implement iterator protocol
    #. Iterator should return instances of ``Mission``
    #. All tests must pass
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zmodyfikuj klasy aby zaimplementować protokół iterator
    #. Iterator powinien zwracać instancje ``Mission``
    #. Wszystkie testy muszą przejść
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        from dataclasses import dataclass


        @dataclass
        class Astronaut:
            firstname: str
            lastname: str
            missions: tuple = ()

        @dataclass
        class Mission:
            year: int
            name: str

:Output:
    .. code-block:: text

        >>> from inspect import isclass, ismethod
        >>> assert isclass(Astronaut)

        >>> astro = Astronaut('Mark', 'Watney')
        >>> assert hasattr(astro, 'firstname')
        >>> assert hasattr(astro, 'lastname')
        >>> assert hasattr(astro, 'missions')
        >>> assert hasattr(astro, '__iter__')
        >>> assert hasattr(astro, '__next__')
        >>> assert ismethod(astro.__iter__)
        >>> assert ismethod(astro.__next__)

        >>> astro = Astronaut('Jan', 'Twardowski', missions=(
        ...     Mission(1969, 'Apollo 11'),
        ...     Mission(2024, 'Artemis 3'),
        ...     Mission(2035, 'Ares 3'),
        ... ))

        >>> for mission in astro:
        ...     print(mission)
        Mission(year=1969, name='Apollo 11')
        Mission(year=2024, name='Artemis 3')
        Mission(year=2035, name='Ares 3')

Protocol Iterator Range
-----------------------
* Assignment name: Protocol Iterator Range
* Last update: 2020-10-02
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/protocol_iterator_range.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define class ``Range`` with parameters: ``start``, ``stop``, ``step``
    #. Write own implementation of a built-in ``range(start, stop, step)`` function
    #. Use Iterator protocol
    #. How to implement passing only stop argument (``range(start=0, stop=???, step=1)``)?
    #. All tests must pass
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj klasę ``Range`` z parametrami: ``start``, ``stop``, ``step``
    #. Zaimplementuj własne rozwiązanie wbudowanej funkcji ``range(start, stop, step)``
    #. Użyj protokołu Iterator
    #. Jak zaimplementować możliwość podawania tylko końca (``range(start=0, stop=???, step=1)``)?
    #. Wszystkie testy muszą przejść
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isclass, ismethod
        >>> assert isclass(Range)

        >>> r = Range(0, 0, 0)
        >>> assert hasattr(r, '__iter__')
        >>> assert hasattr(r, '__next__')
        >>> assert ismethod(r.__iter__)
        >>> assert ismethod(r.__next__)

        >>> list(Range(0, 10, 2))
        [0, 2, 4, 6, 8]

        >>> list(Range(0, 5))
        [0, 1, 2, 3, 4]

        >>> list(Range(5))
        [0, 1, 2, 3, 4]

        >>> list(Range())
        Traceback (most recent call last):
          ...
        ValueError: Invalid arguments

        >>> list(Range(1,2,3,4))
        Traceback (most recent call last):
          ...
        ValueError: Invalid arguments

        >>> Range(stop=2)
        Traceback (most recent call last):
          ...
        TypeError: Range() takes no keyword arguments

        >>> Range(start=1, stop=2)
        Traceback (most recent call last):
          ...
        TypeError: Range() takes no keyword arguments

        >>> Range(start=1, stop=2, step=2)
        Traceback (most recent call last):
          ...
        TypeError: Range() takes no keyword arguments
