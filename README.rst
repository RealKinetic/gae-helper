GAE Helper
====================

A Simple set of tools and patterns to ease the pain of App Engine application
dependency management.

Prerequisites
-------------

This setup guide assumes you are on a somewhat sane posix environment.

- Python 2.7
  
  Download from http://python.org/download/ but should already be on available.

- Google AppEngine SDK
  
  Choose your flavour from https://developers.google.com/appengine/downloads


Create your virtual environment
-------------------------------

This assumes you're using virtualenvwrapper (and you really should)::

    mkvirtualenv your_project

Activate the virtual environment::

    workon your_project


Getting started
---------------

All dependencies are handled automatically.

Firing up the dev server::

    make run

Running the tests
-----------------

There are python tests, run them both before committing::

    make test

