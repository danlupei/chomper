#!/usr/bin/python

import os
import pwd
import sys

from subprocess import call

def main():
    SCRIPT = os.path.realpath(__file__)
    CURRENTDIR = os.path.dirname(SCRIPT)
    PROJECTDIR = os.path.dirname(CURRENTDIR)
    CURRENT_USER = pwd.getpwuid(os.getuid())[0]

    PYTHON_VERSION = sys.version_info
    INTERPRETER = f"python{PYTHON_VERSION[0]}.{PYTHON_VERSION[1]}"

    call([
        "sudo",
        INTERPRETER,
        f"{PROJECTDIR}/chomper/block.py",
        f"--rule={sys.argv[1]}",
        f"--block_length={sys.argv[2]}",
        f"--settings_json_path={PROJECTDIR}/data/block_settings.json",
        "--reset_command",
        f"env PATH=${os.environ['PATH']}"
    ])
