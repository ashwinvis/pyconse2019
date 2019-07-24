# High performance Python

## Category
Big data, Science

## Duration
I prefer a 30 minute slot

## Description
[See abstract](cfp/abstract.md)

## Audience
Developers who primarily use Numpy to build their packages or applications, and
are looking for ways to make it run faster and to scale in multi-core computing
clusters.

## Python level
Intermediate

## Objectives

The audience would learn about two things: 1) state of the art of writing
Python extensions to improve performance; 2) profiling code to know how and
where to optimize

## Detailed abstract

### Motivation
Python community has flourished in the recent years and has given rise to a
mature set of packages. Python's syntax, allowing for readable, easy to
maintain code. We recognize this advantage and show it is possible to have a
Python dominant code base and still achieve performance of C, C++ and Fortran.

### Compiled extensions
For scientific computing, to achieve remarkable performance one has to
write extensions (for example using Cython, cffi, ctypes) -
sometimes referred to as the "two-language problem".

In this talk, we demonstrate that the ability of Python to

1. interface into other languages with very little "glue" code using Cython, and
1. to perform source-to-source compilation (especially from Python to C and
   C++) via Pythran, Numba, etc.

is a strength of using Python. We shall also introduce a new package, called
"Transonic", which aims be a unified front-end for writing such extensions.

### Outline

1. Intro (10 min)
    1. About me
    1. Compiled extensions
    1. Optimize and parallelize wisely by profiling
1. Examples and micro-benchmarks (5 min)
1. Conclusion (5 min)
    1. Python's performance landscape
    1. Comparison of libraries and packages
1. Questions (10 min)
