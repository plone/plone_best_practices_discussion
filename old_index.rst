.. plone_best_practices_disscussion documentation master file.

==================================
Discussion on Plone Best Practices
==================================

This Repository is a Backlog of Ideas and Concepts for Discussion.
Fundamental changes on the codebase and documentation on Plone should be discussed before they will be implemented or enforced in core development.

The problem with *best practices* are, that everyone follow them, without knowing why they are done or why they came up.
Sometimes *best practices* harms a project, if the where not revisited and changed to better approcaches regularly.






This Package is a Placeholder / Backlog of Ideas and Concepts we want to discuss and afterwards move to general Documentation / Trainings Documentation or specific Documentations of Packages or Development Setups like buildout.coredev.

Mission Statement
=================

Plone currently have a set of **Best Practices** that should be used when develop Plone Add'ons or Plone Core Packages.
Those **Best Practices** did conflict in some cases with up to date Python Best Practices and neccessary changes to support multiple Python and Plone Versions.

Therefore this Repository is a platform to discuss tools, code snippets and conventions.

This is a deliverable of `PLIP: TOX as new standard test invocation tool in Plone and Plone guidelines (#2072)  <https://github.com/plone/Products.CMFPlone/issues/2072>`_.

Elements the community have agreed on, should be moved / implemented in plonecli / bobtemplates.plone and the buildout.coredev.

Background
==========

Plone has one big issue, it is still not fully ported to Python 3.
Python 2 support will end on `01.01.2020 <https://pythonclock.org/>`_.
For maintaining a software project substainable it is neccessary to have a defined process.

The **Zen of Python** was written with the lessons learned from Zope in mind.
A lot of those philosopical phases do not only apply to code but also to community practices, habits and methodoligies.

.. code-block:: pycon
    :emphasize-lines: 5, 15-16, 18

    >>> import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

This Document is to make some implicit knowledge explicit available and point to the preferred way of Doing a thing.

The Two Worlds of Software
==========================

Software is not developed for the sake of development but with solving a use case in mind.
The result of software development is most often to use the developed software in production --> operations.

.. graphviz::  base_triangle.dot

Software Projects that have quality standards must enforce those standards and provide documented processes.

For both **Software Development** and **System Operations** common IT Best Practices are published and widly addopted.
In Operations Standards for *IT Service Management (ITSM)* `ISO 20000:2011 <https://en.wikipedia.org/wiki/ISO/IEC_20000>`_ for Software Development the `Capability Maturity Model Integration (CMMI) <https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration>`_ describes certain processes.

.. graphviz:: extended_triangle.dot

One core Element of :ref:`cmmi` is a **Maturity Level**

.. graphviz:: development_process/cmmi.dot





Contents
========

.. toctree::
    :maxdepth: 5
    :caption: Contents:

    development_process/index.rst
    operations_process/index.rst
    package_layout/index.rst
    tools/index.rst

.. toctree::
    :hidden:

    CONTRIBUTORS.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`