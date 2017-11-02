#!/usr/bin/env python
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# *** Drew Coobs <coobs1@illinois.edu> ***
# Modified version of Chris Gerke's PkgDistributionCreator script
# https://github.com/autopkg/cgerke-recipes/blob/master/SharedProcessors/PkgDistributionCreator.py
#   

from subprocess import Popen, PIPE
from os import listdir, stat, chmod, geteuid, mkdir, rename, getcwd
from os.path import join, isfile, isdir
from distutils.dir_util import copy_tree
from shutil import copyfile, rmtree
from tempfile import mkdtemp
import fileinput
import argparse
import sys
import re
import atexit
from autopkglib import Processor, ProcessorError

__all__ = ["MakeMunki"]

class MakeMunki(Processor):
    makescript = 'munki-master/code/tools/make_munki_mpkg.sh'
    description = ("AutoPKG version of make_munki script. ")
    input_variables = {
        "root": {
            "required": True,
            "description": ("Set the munki source root "),
        },
        "recipe_dir": {
            "required": True,
            "description": ("Set the recipe directory "),
        },
        "output_file": {
            "required": True,
            "description": ("Set the output directory "),
        },
    }
    output_variables = {
    }

    __doc__ = description
    source_path = None

    def pkgBuild(self):
        cmd = [join(self.env['recipe_dir'], makescript),
               '-r', self.env['root'],
               '-o', self.env['output_file']]
        try:
        group = run_cmd(
        cmd,
        retgrep='Distribution.*(?P<munki_pkg>munkitools.*pkg).',
        verbose=args.verbose)
        munki_pkg = group.groupdict()['munki_pkg']
        except OSError as e:
            raise ProcessorError(
                "Error building munki pkg, e.strerror))
                    
    def main(self):
            try:
                self.pkgBuild()
            except OSError as e:
                raise ProcessorError(
                    "ERROR, e.strerror))

if __name__ == '__main__':
    processor = MakeMunki()
    processor.execute_shell()
