---
title: python - patsy - overview. 
category: python-libs
tags: python python-libs patsy statistics
---

## patsy: python package for describing statistical models.





Overview
“It’s only a model.”
patsy is a Python package for describing statistical models (especially linear models, or models that have a linear component) and building design matrices. It is closely inspired by and compatible with the formula mini-language used in R and S.

For instance, if we have some variable y, and we want to regress it against some other variables x, a, b, and the interaction of a and b, then we simply write:

patsy.dmatrices("y ~ x + a + b + a:b", data)
and Patsy takes care of building appropriate matrices. Furthermore, it:

Allows data transformations to be specified using arbitrary Python code: instead of x, we could have written log(x), (x > 0), or even log(x) if x > 1e-5 else log(1e-5),
Provides a range of convenient options for coding categorical variables, including automatic detection and removal of redundancies,
Knows how to apply ‘the same’ transformation used on original data to new data, even for tricky transformations like centering or standardization (critical if you want to use your model to make predictions),
Has an incremental mode to handle data sets which are too large to fit into memory at one time,
Provides a language for symbolic, human-readable specification of linear constraint matrices,
Has a thorough test suite (>97% statement coverage) and solid underlying theory, allowing it to correctly handle corner cases that even R gets wrong, and
Features a simple API for integration into statistical packages.
What Patsy won’t do is, well, statistics — it just lets you describe models in general terms. It doesn’t know or care whether you ultimately want to do linear regression, time-series analysis, or fit a forest of decision trees, and it certainly won’t do any of those things for you — it just gives a high-level language for describing which factors you want your underlying model to take into account. It’s not suitable for implementing arbitrary non-linear models from scratch; for that, you’ll be better off with something like Theano, SymPy, or just plain Python. But if you’re using a statistical package that requires you to provide a raw model matrix, then you can use Patsy to painlessly construct that model matrix; and if you’re the author of a statistics package, then I hope you’ll consider integrating Patsy as part of your front-end.

Patsy’s goal is to become the standard high-level interface to describing statistical models in Python, regardless of what particular model or library is being used underneath.

Download
The current release may be downloaded from the Python Package index at

http://pypi.python.org/pypi/patsy/
Or the latest development version may be found in our Git repository:

git clone git://github.com/pydata/patsy.git
Requirements
Installing patsy requires:

Python (version 2.6, 2.7, or 3.3+)
Six
NumPy
Installation
If you have pip installed, then a simple

pip install --upgrade patsy
should get you the latest version. Otherwise, download and unpack the source distribution, and then run

python setup.py install
Contact
Post your suggestions and questions directly to the pydata mailing list (pydata@googlegroups.com, gmane archive), or to our bug tracker. You could also contact Nathaniel J. Smith directly, but really the mailing list is almost always a better bet, because more people will see your query and others will be able to benefit from any answers you get.