***********************
Datetime Dates and Time
***********************


Creating ``date`` objects
=========================

Create ``date``
---------------
.. code-block:: python
    :caption: ``date`` object and its properties

    from datetime import date


    d = date(1961, 4, 12)
    # datetime.date(1961, 4, 12)

    d.year    # 1961
    d.month   # 4
    d.day     # 12

Current ``date``
----------------
.. code-block:: python
    :caption: ``date`` object with current date

    from datetime import date


    today = date.today()
    # datetime.date(2020, 1, 5)

    today.year    # 2020
    today.month   # 1
    today.day     # 5

``date`` methods
--------------------

.. code-block:: python
    :caption: ``date`` object methods

    from datetime import date


    d = date(1969, 7, 21)
    # datetime.date(1969, 7, 21)    # This is Monday

    d.weekday()
    # 0                             # Python defines Monday as zero

    d.isoweekday()
    # 1                             # ISO defines Monday as zero

    d.isoformat()
    # '1969-07-21'


Creating ``time`` objects
=========================

Create ``time``
---------------
.. code-block:: python
    :caption: ``time`` object and its properties

    from datetime import time


    t = time(2, 56, 15)
    # datetime.time(2, 56, 15)

    t.hour            # 2
    t.minute          # 56
    t.second          # 15
    t.microsecond     # 0

Noon and midnight
-----------------
.. code-block:: python
    :caption: ``time`` object representing midnight and noon

    from datetime import time


    time()              # datetime.time(0, 0)
    time(0, 0)          # datetime.time(0, 0)
    time(0, 0, 0)       # datetime.time(0, 0)

    time(12)            # datetime.time(12, 0)
    time(12, 0)         # datetime.time(12, 0)
    time(12, 0, 0)      # datetime.time(12, 0)

    time(24, 0)         # ValueError: hour must be in 0..23


Creating ``datetime`` objects
=============================

Create ``datetime``
-------------------
.. code-block:: python
    :caption: Create ``datetime``

    from datetime import datetime


    dt = datetime(1969, 7, 21, 2, 56, 15)
    # datetime.datetime(1969, 7, 21, 2, 56, 15)

    dt.year          # 1969
    dt.month         # 7
    dt.day           # 21
    dt.hour          # 2
    dt.minute        # 56
    dt.second        # 15
    dt.microsecond   # 0

Create ``datetime`` with empty time (midnight)
----------------------------------------------
.. code-block:: python
    :caption: Create ``datetime`` with empty time

    from datetime import datetime


    dt = datetime(1969, 7, 21)
    # datetime.datetime(1969, 7, 21, 0, 0, 0)

    dt.year          # 1969
    dt.month         # 7
    dt.day           # 21
    dt.hour          # 0
    dt.minute        # 0
    dt.second        # 0
    dt.microsecond   # 0

Create ``datetime`` from ``date`` and ``time`` objects
------------------------------------------------------
.. code-block:: python
    :caption: Create ``datetime`` from ``date`` and ``time`` objects

    from datetime import datetime, date, time


    d = date(1969, 7, 21)
    t = time(2, 56, 15)

    dt = datetime(
        year=d.year,
        month=d.month,
        day=d.day,
        hour=t.hour,
        minute=t.minute,
        second=t.second)
    # datetime.datetime(1969, 7, 21, 2, 56, 15)

.. code-block:: python
    :caption: Create ``datetime`` from ``date`` and ``time`` objects

    from datetime import datetime, date, time


    d = date(1969, 7, 21)
    t = time(2, 56, 15)

    dt = datetime(d.year, d.month, d.day, t.hour, t. minute, t.second)
    # datetime.datetime(1969, 7, 21, 2, 56, 15)

.. code-block:: python
    :caption: Create ``datetime`` from ``date`` and ``time`` objects

    from datetime import datetime, date, time


    d = date(1969, 7, 21)
    t = time(2, 56, 15)

    dt = datetime.combine(d, t)
    # datetime.datetime(1969, 7, 21, 2, 56, 15)

``datetime`` methods
--------------------
.. code-block:: python
    :caption: ``datetime`` methods

    from datetime import datetime


    dt = datetime(1969, 7, 21, 2, 56, 15)
    # datetime.datetime(1969, 7, 21, 2, 56, 15)

    dt.date()
    # datetime.date(1969, 7, 21)

    dt.time()
    # datetime.time(2, 56, 15)

    d.weekday()
    # 0             # Python defines Monday as zero

    d.isoweekday()
    # 1             # ISO defines Monday as one

    dt.isoformat()
    # '1969-07-21T02:56:15'

Current ``datetime`` in local time
----------------------------------
.. code-block:: python
    :caption: Current ``datetime`` in local timezone

    from datetime import datetime


    now = datetime.now()
    # datetime.datetime(2019, 1, 5, 20, 15, 0, 547414)

    now.year          # 2019
    now.month         # 1
    now.day           # 5
    now.hour          # 20
    now.minute        # 15
    now.second        # 0
    now.microsecond   # 547414


Assignments
===========

Create ``date``, ``time`` and ``datetime`` objects
--------------------------------------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/datetime_create_custom.py`

:English:
    #. Create ``date`` object with date of your birth
    #. Create ``time`` object with time of your birth
    #. Create ``datetime`` object with date and time of your birth

:Polish:
    #. Stwórz obiekt ``date`` z datą Twojego urodzenia
    #. Stwórz obiekt ``time`` z czasem Twojego urodzenia
    #. Stwórz obiekt ``datetime`` z datą i czasem Twojego urodzenia

Create current ``date`` and ``datetime`` objects
------------------------------------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/datetime_create_current.py`

:English:
    #. Create ``date`` object with current date
    #. Create ``datetime`` object with current date and time
    #. Create ``time`` object with current time
    #. Date and time must be from system, not hardcoded in code

:Polish:
    #. Stwórz obiekt ``date`` z obecną datą
    #. Stwórz obiekt ``datetime`` z obecną datą i czasem
    #. Stwórz obiekt ``time`` z obecnym czasem
    #. Data i czas ma być pobierana z systemu, nie zapisana w kodzie