============================
tox - A Test Invocation Tool
============================

The Plone community believes in certain best practices for software development.

Documentation, Coding Conventions and Tests are essential elements of a continuous and reproducible software development quality.

The community is large enough to set standards in the whole Python world, but too small to maintain several tools that are not directly connected to Plone the Product.

We embrace standards and standard tools within the general Python community that helps us to keep the high quality of our Product.

`tox <https://pypi.python.org/pypi/tox>`_ is such a standard tool today.
tox is essentially a script wrapper around `virtualenv <https://pypi.pthon.org/pypi/virtualenv>`_ and is primary used for tests invocation.
It is an essential tool to create a set of independent test environments and call them in one command.

tox allows to specify a list of environments which will be executed on invocation.
The key feature of tox, that allows to specify multiple Python and Framework versions to test the package makes it very useful on local development.
For working with different Python versions those need to be installed and avaliable to tox, `pyenv <https://github.com/pyenv/pyenv>`_ is a tool that could help here.

tox is not a replacement for Continuous Integration Server, but it could help to translate those build matrix for local test invocation.

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    usage.rst
    basic_structure.rst
    standard_sections.rst
