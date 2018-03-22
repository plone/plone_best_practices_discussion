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
    $ cd <tox-env>
    $ /bin/pip install tox

.. warning::
    *On macOS there currently seems to be a problem with* ``python3 -m venv`` *command, that makes tox fail.*
    Please use Python 2.7 and virtualenv in this case.

.. note::
    I recommend to add the ``tox`` command to your global command scope,
    so that you could use it with all other virtualenvs:

    .. code-block:: console

        $ cd /usr/local/bin
        $ ln -s <tox-env>/bin/tox tox

Simple Usage
------------

Instead of invoking test commands directly,
with tox you will invoke the ``tox`` command and the tox environments will invoke all test steps and commands for you.

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

Long, repetitive lists of enviroments can written in a short form called `Generative envlist <https://tox.readthedocs.io/en/latest/config.html#generative-envlist>`_,
which will be expanded by tox.

.. code-block:: ini
   :emphasize-lines: 3

    [tox]
    envlist =
        py{27,34,35,36,py}-Plone{43,50,51}
        ...

The command ``tox -l`` lists all the available environment names.
Calling ``tox -e py27`` would invoke py27-Plone43, py27-Plone50, py27-Plone51.

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

The following snippets shows how you can use zc.buildout with tox,
when you want it to run for multiple versions of Python and Plone at once.

.. literalinclude:: ../../code_snippets/tox.d/10_buildout.ini
    :language: ini
    :emphasize-lines: 8-12,16-19

The version files need to be passed explicitly to the buildout command.
Here is an example, how a version file within your package needs should look like:

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

.. literalinclude:: ../../code_snippets/travis-ci.d/00_main.yml
    :language: yaml
    :emphasize-lines: 4-14,26

Jenkins
~~~~~~~

.. todo::

    Need to be added


Gitlab-CI
~~~~~~~~~

.. todo::

    Need to be added
