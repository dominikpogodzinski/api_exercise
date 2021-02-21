#!/usr/bin/env bash

/usr/bin/env python -m prospector --without-tool pyflakes
./manage.py test