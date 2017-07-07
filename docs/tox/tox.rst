============================
TOX - A Test Invocation Tool
============================

The Plone community believes in certain best practices for software development.

Documentation, Coding Conventions and Tests are essential elements of a continuous and reproducibale software development quality.

The community is large enough to set standards in the whole Python world, but to small to maintain several tools that are not directly connected to Plone the Product.

We embrace standards and standard tools within the general Python community that helps us to keep our Product on high quality.

`TOX <https://pypi.python.org/pypi/tox>`_ is such a standard tool today.
TOX is essentially a script wrapper around `virtualenv <https://pypi.pthon.org/pypi/virtualenv>`_ and is primary used for invocation of tests.
It is a good tool to create a set of independent test environments and call them in one command.

TOX allows to specify a list of environments which will be executed on invocation.
The key feature of TOX, that allows to specify multiple Python and Framework versions to test the package makes it very useful on local development.

TOX is not a replacement for Continuous Intergation Server, but it could help to translate those build matrixs for local test invocation.

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

Basic Strcuture
===============

TOX follows the UNIX philosphy to do only one thing and do that right. One second philosophy element is also followed, the configuration by a text files: the tox.ini files.

tox.ini files are very similar to zc.buildout's buildout.cfg.
They start with a general ``tox`` section that has a ``envlist`` parameter list comparable to ``buildout``'s ``parts`` list

.. code-block:: ini

    [tox]
    envlist =
        <env1>,
        <env2>,
        ...
        <env#>

    [testenv]
    # general settings for all testvens

    [testenv:env1]
    # Settings only for <env1>


Plone Standard Sections
-----------------------

For Plone we recommend you to have the following special environments:

* flake8
* isort & isort-apply
* docs
* coverage-report
* release

Those environments expect some common package layout:

.. code-block:: filesystem

    <package root>/
    ├─docs/ (Documentation / Sphinx)
    |  ├─index.rst
    |  ├─...
    |  └─conf.py
    ├─src/ (source code-block directory)
    |  └─...
    ├─tests/ (optional - external pytest test directory)
    |  └─...
    ├─reports/ (tox will generate html reports in this directory)
    |  └─...
    ├─setup.py
    ├─setup.cfg (Package Configuration)
    ├─tox.ini
    ├─.editorconf
    ├─.travis.yml
    ├─.coveragerc
    ├─.gitignore
    └─...

Your ``tox.ini`` should look / start like this:

.. code-block:: ini

    [tox]
    envlist =
        py{27,34,35,36,py}, # test Environemnts.
        docs,
        isort,
        flake8,
        coverage-report,

    skip_missing_interpreters = False

    [testenv]
    ...



Flake8
------

`flake8 <http://flake8.pycqa.org/en/latest/>`_ is a adaptable linter for Python that helps you to enforce coding conventions.

.. code-block:: ini

    [testenv:flake8]
    skip_install = true

    deps =
        flake8
        flake8-html
        flake8-coding
        flake8-debugger
        flake8-deprecated
        flake8-isort
        flake8-pep3101
        flake8-plone-hasattr
        flake8-polyfill
        flake8-print
        flake8-quotes
        flake8-string-format
        flake8-todo

    commands =
        mkdir -p {toxinidir}/reports/flake8
        - flake8 --format=html --htmldir={toxinidir}/reports/flake8 --doctests src tests setup.py
        flake8 --doctests src tests setup.py

    whitelist_externals =
        mkdir


Isort & Isort-apply
-------------------

`isort <http://isort.readthedocs.io/en/latest/>`_ is a Python utility to sort import

.. code-block:: ini

    [testenv:isort]
    skip_install = true

    deps =
        isort

    commands =
        isort --check-only --recursive {toxinidir}/src

    [testenv:isort-apply]
    skip_install = true

    deps =
        isort

    commands =
        isort --apply --recursive {toxinidir}/src

Docs
----

.. code-block:: ini

    [testenv:docs]
    skip_install = true

    deps =
        Sphinx

    commands =
        sphinx-build -b html -d build/docs/doctrees docs build/docs/html
        sphinx-build -b doctest docs build/docs/doctrees

Coverage-report
---------------


.. code-block:: ini

    [testenv:coverage-report]
    skip_install = true

    deps =
        coverage

    setenv =
        COVERAGE_FILE=.coverage

    commands =
        coverage erase
        coverage combine
        coverage html
        coverage xml
        coverage report

Release
-------

.. raw:: ini
    :file: ../../code_snippets/tox.d/release.ini
