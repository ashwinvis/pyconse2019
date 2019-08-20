# Make your Python code fly at transonic speeds!

## Category
Scientific computing

## Duration
I prefer a 30 minute slot

## Description
[See abstract](cfp/abstract.md)

## Audience
Developers who primarily use Python to build their packages or applications, and
are looking for ways to make it run faster.

## Python level
Intermediate

## Objectives

The audience would learn about the state of the art of writing Python
extensions to improve performance

## Detailed abstract

### Motivation
Python community has flourished in the recent years and has given rise to a
mature set of packages. Python's syntax, allowing for readable, easy to
maintain code. We recognize this advantage and show it is possible to have a
Python dominant code base and still achieve performance of C and C++.

### Compiled extensions
For scientific computing, to achieve remarkable performance one has to
write extensions (for example using Cython, cffi, Numba, Pythran).
In this talk, we demonstrate the ability of Python to:

1. interface into other languages with very little "glue" code using Cython, and
1. to perform source-to-source compilation (especially from Python to C and
   C++) via Pythran, Numba, etc.

We shall introduce a new package, called "Transonic", which aims be a
unified front-end for writing such libraries and uses type-hints to generate
extensions.

### Outline

1. Intro (10 min)
    1. About me
    1. Compiled extensions
    1. Optimize wisely by profiling
    1. Python's HPC landscape
1. Make your Python code fly at "transonic" speeds! (10 min)
    1. Examples and micro-benchmarks
1. Conclusion (5 min)
1. Questions (5 min)
