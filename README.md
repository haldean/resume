Resumator
=========

A simple DSL for specifying and generating resumes in LaTeX and HTML format.

Installation
------------
Resumator requires argparse, which can be downloaded from pypi using
easy\_install.

Usage
-----

## Arguments

Resumator takes an output format and an input file as arguments. Output format
can be one of HTML and LaTeX (Markdown support is in the works). It also can
take an optional pre-file and post-file, which are inserted at the head and tail
of the output. This is useful for some output formats, like LaTeX, which don't
output a complete, valid document; it needs to be wrapped in document tags to be
valid.

## Input Format


