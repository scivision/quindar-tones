=============
quindar-tones
=============

Generate tones on keypress including:

* Quindar tones used by NASA for decades as in-band PTT signaling
* Motorola tone remote
* Nextel chirp

:prereqs: Python 3 or 2.7, PyGame, Numpy

Install
=======
::

    flit install -s


Usage
=====
::

    python keytones.py



* left-arrow: 2525 Hz
* right-arrow: 2475 Hz
* up-arrow: tone remote leadin 2175 1950 Hz
* down-arrow: Nextel chirp 1800 Hz bips


