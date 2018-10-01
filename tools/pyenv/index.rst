.. _pyenv:

pyenv
=====

Install pyenv
-------------

If you want to test several Python versions at the same time,
use a tool like `pyenv <https://github.com/pyenv/pyenv>`_.

This assumes that you use macOS and `homebrew <https://brew.sh/>`_

.. code-block:: console

    $ brew install pyenv
    $ pyenv install --list
    $ pyenv install <version>

For other Unix/Linux based Operation systems do:

.. code-block:: console

    $ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    $ pyenv install --list
    $ pyenv install <version>

We should encourage all developers to have the most recent Python buxfix release installed for all supported Minor-Releases that Plone aims to support.

`Supported Python Versions <https://docs.python.org/devguide/index.html#branchstatus>`_ are:

* 2.7
* 3.4
* 3.5
* 3.6
* 3.7 (Development)
