#!/usr/bin/env python3
import os
from setuptools import setup
from pathlib import Path
thisDir = Path(__file__).parent
setup(use_scm_version = True)
