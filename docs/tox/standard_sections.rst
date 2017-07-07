Plone Standard Sections
-----------------------

For Plone we recommend you to have the following special environments:

* flake8
* isort & isort-apply
* docs
* coverage-report
* release

Your ``tox.ini`` should look / start like this:

.. include:: ../../code_snippets/tox.d/tox.ini
    :code: ini

Flake8
~~~~~~

`flake8 <http://flake8.pycqa.org/en/latest/>`_ is a adaptable linter for Python that helps you to enforce coding conventions.

.. include:: ../../code_snippets/tox.d/flake8.ini
    :code: ini

Isort & Isort-apply
~~~~~~~~~~~~~~~~~~~

`isort <http://isort.readthedocs.io/en/latest/>`_ is a Python utility to sort import

.. include:: ../../code_snippets/tox.d/isort.ini
    :code: ini

Docs
~~~~

.. include:: ../../code_snippets/tox.d/docs.ini
    :code: ini
Coverage-report
~~~~~~~~~~~~~~~


.. include:: ../../code_snippets/tox.d/coverage.ini
    :code: ini

Release
~~~~~~~

.. include:: ../../code_snippets/tox.d/release.ini
    :code: ini
