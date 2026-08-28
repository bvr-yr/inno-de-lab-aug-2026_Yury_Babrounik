#!/usr/bin/env bash

./genrs 10000000 | "$1" >/dev/null
