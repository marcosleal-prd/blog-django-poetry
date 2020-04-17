#!/bin/bash
isort -rc blog_python tests -c --diff \
&& black --check --diff blog_python tests \
&& pycodestyle blog_python tests \
&& flake8 blog_python tests \
&& mypy blog_python tests

# Run this for full check -> pylint blog_python tests
