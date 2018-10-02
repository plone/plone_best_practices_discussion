.. _package_layout:

====================
Plone Package Layout
====================

Proposal of Alexander Loechel
=============================

Currently we do not have a recommended / defined package layout for Plone core or Plone addon packages.
All packages are Python eggs


We encourage all developer to use a certain package layout.
This package layout should be provided by skeletion generators (`PloneCLI <https://pypi.org/project/plonecli/>`_ , underlying Template Set `bobtemplates.plone <https://pypi.org/project/bobtemplates.plone/>`_ of `mr.bob <https://pypi.org/project/mr.bob/>`_, or old `ZopeSkel <https://pypi.org/project/ZopeSkel/>`_).

.. code-block:: filesystem

    <package root>/
    ├─_build/ (tox will generate html reports in this directory)
    |  ├─coverage
    |  ├─docs
    |  ├─flake8
    |  ├─pytest
    ├─docs/ (Documentation / Sphinx)
    |  ├─index.rst
    |  ├─...
    |  ├─distutils.conf
    |  └─conf.py
    ├─src/ (source code-block directory)
    |  └─...
    ├─tests/ (optional - external pytest test directory)
    |  └─...
    ├─.editorconf
    ├─.gitignore
    ├─.gitattributes
    ├─.travis.yml
    ├─Manifest.in
    ├─README.{rst/md}
    ├─setup.cfg (Python Tools and Package Configuration)
    ├─setup.py
    ├─tox.ini
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
  * tests/ --> Packge Tests should go into a separate folder in the base directory (To be discussed in detail) ref:`test_folder`
  * docs/ --> Package Documentation written in Sphinx / restructuredText
  * _build/ --> generated HTML Reports (not in VCS)
  * .tox/ --> Folder where virtualenvs will be created and hold by tox (not in VCS)
  * bin/, lib/, include/, share/ --> Folders that could exists, if virtualenv was invoked for developmemt on the base folder (not in VCS)

Explanation of Configuration Files
----------------------------------

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    setup_cfg/index
    tests_folder.rst
