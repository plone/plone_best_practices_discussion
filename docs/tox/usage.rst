Usage
=====

Installation
------------

Install tox somewhere so that you have the ``tox`` command in your path, recommended is to have it in a separate vitualenv.

.. code-block:: console

    # For Python 3.4+ you could use this
    $ python -m venv <tox-env>
    # On Python 2.7 or Python 3 before 3.4 please use
    $ virtualenv <tox-env>
    $ cd <tox-env>/bin/pip install tox

*currently there seems to be a problem with* ``python3 -m venv`` *command, so that tox fail.*
Please install with Python 2.7

I recommend to add the ``tox`` command to your global command scope, so that you could use it with all other virtualenvs:

.. code-block:: console

    $ cd /usr/local/bin
    $ ln -s <tox-env>/bin/tox tox

Simple Usage
------------

Instead of invoking test commands directly, with tox you will invoke the ``tox`` command and the tox environments will invoke all test steps and commands for you.

Call ``tox`` in your product base directory.
This will invoke all environments named in the tox.ini envlist:

.. code-block:: ini
   :emphasize-lines: 2

    [tox]
    envlist =
        <env1>,
        <env2>,
        ...
        <env#>

    ...


You also can invoke only a specific set of tox environments by:

.. code-block:: console

    $ tox -e <env1>,<env2>,...,<env#>

That is especially useful as you could invoke environments that are normaly not used, as they are not on the envlist.

.. code-block:: console

    $ tox -e isort-apply

A special feature of TOX is that you could call a group of envs by a common pattern,

.. code-block:: ini
   :emphasize-lines: 3

    [tox]
    envlist =
        py{27,34,35,36,py}-Plone(43,50,51)
        ...

calling ``tox -e py27`` would invoke py27-Plone43, py27-Plone50, py27-Plone51.

Also you can pass positional arguments to the test command, if the tox.ini forward that (``{posargs}``):

.. code-block:: ini
   :emphasize-lines: 4

    [testenv]
    commands =
        {envbindir}/buildout -c {toxinidir}/buildout.cfg install test
        coverage run {envbindir}/test -v1 --auto-color {posargs}

.. code-block:: console

    $ tox -- <positional argument>

for example:

.. code-block:: console

    # invoke pdb on test failure (pytest)
    $ tox -- --pdb

    # invoke all tests ()
    $ tox -- --all

As Git-hook
-----------

As TOX is useful to ensure code-block quality check, it might be a good idea to set it as a git pre-commit hook.

Therefore create / edit the file ``<product base_path>/.git/hooks/pre-commit`` and add a line that invokes tox with those environments, for example:

.. code-block:: console

    $ tox -e flake8,isort,docs

Advanced Usage
--------------

tox has a lot of features and possibilities.
Please refer to the `tox documentation <http://tox.readthedocs.io/en/latest/>`_ to get up to date documentation.

Usage with zc.buildout
----------------------

TOX with zc.buildout is not that straight foreward, but possible to run against multiple Versione of Python and Plone together:

.. literalinclude:: ../../code_snippets/tox.d/10_buildout.ini
    :language: ini
    :emphasize-lines: 8-12,16-19

where your package needs to contain a version file that looks like that:

.. literalinclude:: ../../code_snippets/tox.d/11_version_plone51.cfg
    :language: ini
    :emphasize-lines: 3-5

Continuous Integration Servers (CI)
-----------------------------------

If external Continiuous Intergation Servers are used to test your package, the results should be identical to a local tox run, therefore the CI-Servers should invoke tox and not any other additional test commands.

Only optimizations for caching, parallel build, notification and additional steps should be in their configs.

Travis-CI
~~~~~~~~~

If your Package runs Travis-CI it should be contain a ``.travis.yml`` file.

Jenkins
~~~~~~~

.. todo::

    Need to be added


Gitlab-CI
~~~~~~~~~

.. todo::

    Need to be added
