Plone Standard Sections
-----------------------

For Plone we recommend you to have the following special environments:

* flake8
* isort & isort-apply
* docs
* coverage-report
* release

Your ``tox.ini`` should look / start like this:

.. literalinclude:: ../../code_snippets/tox.d/tox_main.ini
    :language: ini

Flake8
~~~~~~

`flake8 <http://flake8.pycqa.org/en/latest/>`_ is a adaptable linter for Python that helps you to enforce coding conventions.

.. literalinclude:: ../../code_snippets/tox.d/flake8.ini
    :language: ini

Isort & Isort-apply
~~~~~~~~~~~~~~~~~~~

`isort <http://isort.readthedocs.io/en/latest/>`_ is a Python utility to sort import

.. literalinclude:: ../../code_snippets/tox.d/isort.ini
    :language: ini

Docs
~~~~

.. literalinclude:: ../../code_snippets/tox.d/docs.ini
    :language: ini

Coverage-report
~~~~~~~~~~~~~~~


.. literalinclude:: ../../code_snippets/tox.d/coverage.ini
    :language: ini

Release
~~~~~~~

.. literalinclude:: ../../code_snippets/tox.d/release.ini
    :language: ini
