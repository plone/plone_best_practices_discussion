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
