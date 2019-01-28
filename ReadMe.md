ELFRelocs.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
[wheel](https://gitlab.com/KOLANICH/ELFRelocs.py/-/jobs/artifacts/master/raw/wheels/ELFRelocs-0.CI-py3-none-any.whl?job=build)
[![PyPi Status](https://img.shields.io/pypi/v/ELFRelocs.svg)](https://pypi.python.org/pypi/ELFRelocs)
![GitLab Build Status](https://gitlab.com/KOLANICH/ELFRelocs.py/badges/master/pipeline.svg)
[![Coveralls Coverage](https://img.shields.io/coveralls/KOLANICH/ELFRelocs.py.svg)](https://coveralls.io/r/KOLANICH/ELFRelocs.py)
![GitLab Coverage](https://gitlab.com/KOLANICH/ELFRelocs.py/badges/master/coverage.svg)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/ELFRelocs.py.svg)](https://libraries.io/github/KOLANICH/ELFRelocs.py)


A framework to compute relocations for ELF file format.

You inherit the class `Relocator` and `RelocWrapper` and implement everything which is NotImplemented. Then you call the method `computeRelocatedPtr` passing there **RAW Virtual address of a pointer** and **its value**, and get the relocated address (linker gonna patch the program, replacing that pointer with this value when loading, if everything dependent is loaded by the desired addresses).

`libs` submodule contains some already implemented relocators for some libs.


Requirements
------------
* [`Python >=3.4`](https://www.python.org/downloads/). [`Python 2` is dead, stop raping its corpse.](https://python3statement.org/) Use `2to3` with manual postprocessing to migrate incompatible code to `3`. It shouldn't take so much time.

* [`ELFMachine`](https://gitlab.com/KOLANICH/ELFMachine.py)
