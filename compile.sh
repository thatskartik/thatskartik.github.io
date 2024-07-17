#!/bin/bash
pandoc --standalone -s -c style.css  $1.md -o $1.html -H mathjax.js --mathjax
