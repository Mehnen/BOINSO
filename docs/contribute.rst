*****************
How to contribute
*****************

As with every open source project on github you just have to fork the repository, implement your ideas and send a pull request. If you want to contribute on a regular basis just send an e-mail to gregor_ and you will be added as a contributor.

.. _gregor: gregor.beyerle@gmail.com

Code Conventions
================

We use the pyflakes and pep8 modules to enforce a tidy coding style. We also try to stick to the basic architecture of the Django project as it provides a very solid basis for maintanable and scalable web applications. We aren't by any means "professionals" and our work may break these conventions so if you find any error just let us know! If you use a pep8 linter you can exclude the following warnings:

    E501, C0301, W0142, W0402, R0201, E1101, E1102, C0103, R0901, R0903, R0904, C1001, W0223, W0232, W0201, E1103, R0801, C0111

Vagrant
=======

We are using very different development setups in our team. As we don't want to spend our time with fixing "But-It-Works-On-My-Machine"-bugs we like to use Vagrant_. If you have never tried Vagrant for one of your projects don't be afraid to test it. The base container is a basic Ubuntu 14.04LTS 32bit machin including a python2 interpreter, a python3 interpreter and a postgres database. Currently we only support virtual box but in the future we plan to also add VMWare Player and Hyper-V boxes.

Right now we only use a basic shell provisioner. If your worklow depends on a special setup you can customize `bootstrap.sh`.

**To use our provided boxes you will need an** Atlas_ **account!**

.. _Vagrant: https://docs.vagrantup.com/v2/getting-started/index.html
.. _Atlas: https://atlas.hashicorp.com/

Basic setup
===========

If you don't want to use Vagrant this is no problem. Just run the application as you would any other Django app (you will have to change the database backend in `Boinso.settings.py` though). If you use a normal Python installation make sure to use a virtual environment. If you favour using Anaconda stick to destinct conda environment. Naturally you can do whatever you want with your local setup but seperating application dependencies doesn't interfere with other project dependencies.

Testing
=======

We are always eager to improve our test coverage. If you implement new functionallity please add automated tests!