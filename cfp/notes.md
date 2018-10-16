# Scalable high performance scientific computing approaches

## Category
Science

## Duration
I prefer a 30 minute slot

## Description
[See abstract](cfp/abstract.md)

## Audience
Developers who primarily use Numpy to build their packages or applications, and
are looking for ways to make it run faster and to scale in multi-core computing clusters.

## Python level
Intermediate

## Objectives

The audience would learn about existing possibilities to write optimized
compiled extensions. The talk also introduces approaches to parallelize either
by splitting the arrays (domain decomposition parallelism) or splitting data
(data parallelism) with Python packages.


## Detailed abstract
### Motivation
Python community has flourished in the recent years and has given rise to a
mature set of packages, also known as the  "Scientific Python ecosystem".
Python quickly finds its way in education and research due it its expressive
syntax, allowing for readable, easy to maintain code. It is also well known
that to develop optimized Python applications, one has to write compiled
extensions (for example using Cython, Pythran, and Numba) - sometimes referred
to as the "two-language problem".

In this talk, we demonstrate that the ability of Python to interface into other
languages with very little "glue" code and to perform source-to-source
compilation (especially to C and C++) is, in fact a strength and not a problem.
We intend to present how we achieved this using Cython and Pythran,
present an overview of all possible options, its pros and cons.

Writing parallelized scalable applications is another area where Python shines.
In particular there are two parallelism paradigms which are important:

  1. Domain-decomposition parallelism where the computing breaks up very large
     arrays into smaller chunks. Usually this is done to lower the computation
     time or to fit the array in the memory available.

  2. Data parallelism which is employed to distribute a series of data and
     associated tasks into a combination of threads and processes distributed
     over several computing nodes. The tasks can be either I/O bound or CPU
     bound.

Traditionally research softwares have relied on OpenMP and MPI libraries to
parallelize. With Python the same are possible, using Pythran and mpi4py, for
instance. Multiprocessing, threading and asyncio libraries have provided a foundation
for other new packages to evolve pure-Python approaches: domain-decomposition
parallelism using Dask.array and data parallelism using multiprocessing,
threading, asyncio or trio. We intend to share our experiences with simple
examples demonstrating how to achieve this.

### Outline

1. Intro (10 min)
    1. About me
    1. Compiled extensions
    1. Domain decomposition parallelism
    1. Data parallelism
    1. Optimize and parallelize wisely with tools to profile, and benchmark
1. Case studies, exploring alternatives and micro-benchmarks (10 min)
    1. Example: Extensions using Cython and Pythran
    1. Example: Domain-decomposition with mpi4py
    1. Example: Data parallelism
1. Conclusion (10 min)
    1. Comparison of libraries and packages
    1. Questions
