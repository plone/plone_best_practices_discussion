setup.cfg - Common Configurations for Python Packages
-----------------------------------------------------

The setup.cfg file is a common configuration file in a Python package, that is respected by most of python tools.

We should encurage all Plone / Python developers to use this file instead if specific configuration files for tools.

Common Parts
~~~~~~~~~~~~

* isort
* flake8
* coverage



isort
.....




flake8
......



coverage
........

Section starting with ``[coverage:`` will be used by coverage if no ``.coveragerc`` file existis in this context (https://coverage.readthedocs.io/en/coverage-4.4.1/config.html#configuration-files).
