Usage
=====

Installation
------------

Install TOX somewhere so that you have the ``tox`` command in your path, recommended is to have it in a separate vitualenv.

.. code-block:: sh

    python -m venv <tox-env>
    source <tox-env>/bin/activate
    $<tox-env>/bin/pip install tox

Simple Usage
------------

Instead of invoking test commands directly, with tox you will invoke the ``tox`` command and the tox environments will invoke all test steps and commands for you.

Call

.. code-block:: sh

    tox

in your product base directory.
This will invoke all environments named in the tox.ini envlist:

.. code-block:: ini

    [tox]
    envlist =
        <env1>,
        <env2>,
        ...
        <env#>

    ...


You also can invoke only a specific set of tox environments by:

.. code-block:: sh

    tox -e <env1>,<env2>,...,<env#>

That is especially useful as you could invoke environments that are normaly not used, as they are not on the envlist.

.. code-block:: sh

    tox -e isort-apply

Also you can pass positional arguments to the test command, if the tox.ini forward that (``{posargs}``):

.. code-block:: sh

    tox -- <positional argument>

for example:

.. code-block:: sh

    # invoke pdb on test failure (pytest)
    tox -- --pdb

    # invoke all tests ()
    tox -- --all

As Git-hook
-----------

As TOX is useful to ensure code-block quality check, it might be a good idea to set it as a git pre-commit hook.

Therefore create / edit the file ``<product base_path>/.git/hooks/pre-commit`` and add a line that invokes tox with those environments, for example:

.. code-block:: sh

    tox -e flake8,isort,docs

Advanced Usage
--------------

TOX has a lot of features and possibilities.
Please refere to the `tox documentation <http://tox.readthedocs.io/en/latest/>`_ to get up to date documentation.

Continiuous Integration Servers (CI)
------------------------------------

If external Continiuous Intergation Servers are used to test your package, the results should be identical to a local tox run, therefore the CI-Servers should invoke tox and not any other additional test commands.

Only optimisations for caching, parallel build, notification and additional steps should be in their configs.

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
