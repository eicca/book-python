***************
Type Annotation
***************

Dict
====
.. code-block:: python

    data: dict = {}
    data: dict = dict()

.. code-block:: python

    from typing import Dict

    a: Dict[int, str] = {
        0: 'setosa',
        1: 'virginica',
        2: 'versicolor',
    }

    b: Dict[float, str] = {
        5.8: 'Sepal length',
        2.7: 'Sepal width',
        5.1: 'Petal length',
        1.9: 'Petal width',
    }

    c: Dict[str, float] = {
        'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9,
    }


``list`` of ``dict``
====================
.. code-block:: python
    :caption: Generic type annotation

    from typing import List


    data: List[dict] = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Dict, List, Union


    data: List[Dict[str, Union[List[float], str]]] = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Dict, List, Union

    Measurement = List[float]

    data: List[Dict[str, Union[Measurement, str]]] = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

.. code-block:: python
    :caption: Explicit type annotation

    from typing import Dict, List, Union

    Measurement = List[float]
    Data = Union[Measurement, str]
    Row = Dict[str, Data]

    data: List[Row] = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]


New Features
============
.. versionadded:: Python 3.9
    :pep:`585` Will be possible to use ``dict[str, int]``, ``dict[str, list[float]]`` etc without importing from ``typing``