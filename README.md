Resumator
=========

A simple DSL for specifying and generating resumes in LaTeX and HTML format.

Installation
------------
Resumator requires argparse, which can be downloaded from pypi using
easy\_install.

Arguments
---------

Resumator takes an output format and an input file as arguments. Output format
can be one of HTML and LaTeX (Markdown support is in the works). It also can
take an optional pre-file and post-file, which are inserted at the head and tail
of the output. This is useful for some output formats, like LaTeX, which don't
output a complete, valid document; it needs to be wrapped in document tags to be
valid.

Input Format
------------

To create top-level headers, start a line with a double-equals sign. Trailing
double-equals will be ignored, so these are equivalent:

    == Header Name ==
    == Header Name

Each header is expected to have a series of resume items underneath them. A
resume item consists of where you worked or the name of the project, a location,
your position, and the dates during which you worked there. It also contains an
optional list of bulletpoints describing what you did. The format for this is
shown below.

    -- Organization
    Location
    Title
    Date
    - Bulletpoint one
    - Bulletpoint two
    - Bulletpoint three

The bulletpoints are optional, but the organization, location, title and date
are not. Any of these fields can, however, be left blank; if you wanted to not
specify the location of a certain position, it could be specified as:

    -- Organization

    Title
    Date

And if you just wanted to list the name of the organization, you could specify
it as:

    -- Organization




(Note that that is three blank lines following the organization)



