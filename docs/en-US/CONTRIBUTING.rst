.. highlight:: shell

=================
How to Contribute
=================

Contribution are always welcome and appreciated!

You can contribute in many ways::

Types
----------------------

Reporting Bugs
~~~~~~~~~~~~~~~~

Please, report bugs at https://github.com/mstuttgart/pycep-correios/issues.

If you are to report a *bug*, please, include:

* Name and version of you operational system.
* Any details about your local setup that you may think it's useful in solving the problem.
* Detailed steps descriptions to reproduce the bug.

Fix bugs
~~~~~~~~~~~~~~~~

Search in the list of *issues* for those with *Bug* tag.
Any *issue* tagged as "Bug" is free open for anyone to fix it.

Adding new features
~~~~~~~~~~~~~~~~~~~~~~~~~~

Search in the list of *issues* for those with *Improvement* or *New feature* tags.
Any *issue* tagged with those *tags* is free open for anyone to develop it.

Improving documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

The PyCEPCorreios docs can always be improved. It can be done by official documentation in *docstrings*
or blog posting, articles, etc. in the web. If you did some blogging about PyCEPCorreios, please,
feel free to reach me, so it can be included here as a reference.

Send comments
~~~~~~~~~~~~~~~~~~

The best way to send comments is to open an *issue* at https://github.com/mstuttgart/pycep-correios/issues.

If you are adding a new feature to PyCEPCorreios, please follow the guidelines:

* Explain in detail how it would work.
* Keep the scope as simple as you can, so the development will be easier.
* Keep in mind this is a volunteer project and contibutions are always welcome :)

Submitting a Pull Request
-------------------------

Before you submit your pull request consider the following guidelines:

1. The *Pull Request* must include tests when you add a new *feature*.
2. If the *Pull Request* adds functionalities, the documentation must be updated with description in detail of usage.
3. The *Pull Request* submission must work for Python 2.7+ e 3.3+. Check https://travis-ci.org/mstuttgart/pycep-correios/pull_requests and make sure all tests pass for all the Python versions supported.


Ready to contribute? These are the steps how to configure `pycep_correios` for local development.

1. Fork `pycep_correios` in GitHub.
2. Clone the *branch*::

    $ git clone git@github.com:your_name_here/pycep-correios.git

3. Build the environment. If you have installed *virtualenv*, this is how you can configure the project for local development::

    $ cd pycep-correios
    $ virtualenv env
    $ pip install -r requirements.txt

4. Create a *branch*::

    $ git checkout -b your-branch-name

   Now, you're ready to make your changes.

5. When you are done, check if your changes follow pep8 with *flake8* and run the tests::

    $ flake8 pycep_correios tests
    $ python setup.py test

6. Check the changes and send them to GitHub::

    $ git add .
    $ git commit -m "Description of the commit."
    $ git push origin your-branch-name

7. Submit a *Pull Request* to the original PyCEPCorreios repository in GitHub.
