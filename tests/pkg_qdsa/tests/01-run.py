#!/usr/bin/env python3

# Copyright (C) 2017 Freie Universität Berlin
#
# This file is subject to the terms and conditions of the GNU Lesser
# General Public License v2.1. See the file LICENSE in the top level
# directory for more details.

import sys
from testrunner import run_check_unittests

# It takes ~11s on nucleo-l152re, so add some margin
TIMEOUT = 15


if __name__ == "__main__":
    sys.exit(run_check_unittests(timeout=TIMEOUT))
