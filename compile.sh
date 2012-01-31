#!/bin/sh
multimarkdown --smart --process-html resume.md | tidy -i --wrap 80 -o index.html
