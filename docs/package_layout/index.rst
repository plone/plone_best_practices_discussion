Plone Package Layout
====================



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
