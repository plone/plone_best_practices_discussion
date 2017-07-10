tests Folder in Package Root
----------------------------

Till now it was best practice to put Zope/Plone tests into a tests.py or tests folder in the namespace package base.
This should be discurraged and stopped.

Clean software development allows to ship production code without tests and docs (bdist and wheels), while sdist releases should contain all three (source, tests and docs).
Also if files in tests life in the namespace of the a Pyhon package it could be used or derived from other packages, that should not be done.
