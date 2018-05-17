Plone Standard Sections
-----------------------

For Plone we recommend you to have the following special environments:

* flake8
* isort & isort-apply
* docs
* coverage-report
* release

Your ``tox.ini`` should look / start like this:

.. literalinclude:: ../../../code_snippets/tox.d/00_tox_main.ini
    :language: ini

Flake8, Isort & Isort-apply
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`flake8 <http://flake8.pycqa.org/en/latest/>`_ is a adaptable linter for Python that helps you to enforce coding conventions.
`isort <http://isort.readthedocs.io/en/latest/>`_ is a Python utility to sort import

.. literalinclude:: ../../../code_snippets/tox.d/90_lint.ini
    :language: ini
    :emphasize-lines: 1,10

Docs
~~~~

.. literalinclude:: ../../../code_snippets/tox.d/90_docs.ini
    :language: ini

Coverage-report
~~~~~~~~~~~~~~~


.. literalinclude:: ../../../code_snippets/tox.d/80_coverage.ini
    :language: ini

Release
~~~~~~~

.. literalinclude:: ../../../code_snippets/tox.d/99_release.ini
    :language: ini
