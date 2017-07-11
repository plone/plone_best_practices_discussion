Plone Package Layout
====================

We should encurage all developer to use a certain package layout.
For example:

.. code-block:: filesystem

    <package root>/
    ├─docs/ (Documentation / Sphinx)
    |  ├─index.rst
    |  ├─...
    |  ├─distutils.conf
    |  └─conf.py
    ├─src/ (source code-block directory)
    |  └─...
    ├─tests/ (optional - external pytest test directory)
    |  └─...
    ├─reports/ (tox will generate html reports in this directory)
    |  └─...
    ├─setup.py
    ├─setup.cfg (Python Tools and Package Configuration)
    ├─tox.ini
    ├─.editorconf
    ├─.travis.yml
    ├─.gitignore
    └─...


The package root should only contain necessary files and directories that will also live in Version Control.

* Necessary Python Package Files:

  * setup.py --> Package Meta-Daten
  * setup.cfg --> Python Tool and Package Configuration
  * Manifest.in -->

* Necessary Version Control Files (git / svn / hg):

  * .gitignore
  * .gitattributes

* Test Configuration:

  * tox.ini
  * .travis.yml

* Necessary general Files:

  * README.rst --> Package Description used to show Package details on Version Control Platform and PyPI
  * LICENSE --> License of this Package to presented on Version Control Platform
  * .editorconfig --> Configuration File for Editors / IDEs to enforce basic Coding Convention

* Subfolders with Meanings:

  * src/ --> Package Source Code
  * tests/ --> Packge Tests should go into a separate folder in the base directory (To be discussed in detail)
  * docs/ --> Package Documentation written in Sphinx / restructuredText
  * reports/ --> generated HTML Reports of Code Convention Tests (not in VCS)
  * .tox/ --> Folder where virtualenvs will be created and hold by tox (not in VCS)
  * bin/, lib/, include/, share/ --> Folders that could exists, if virtualenv was invoked for developmemt on the base folder (not in VCS)

Explanaition of Configuration Files
-----------------------------------


.. toctree::
    :maxdepth: 2
    :caption: Contents:

    setup_cfg/index
    editorconfig
    ../tox/index
    ../ci/travis-ci
    ../ci/jenkins
    tests_folder
