#!/usr/bin/python
#
# Utility script to generate .pc files for libsoup
# for Visual Studio builds, to be used for
# building introspection files

# Author: Fan, Chun-wei
# Date: March 10, 2016

import os
import sys

from replace import replace_multi
from pc_base import BasePCItems

def main(argv):
    base_pc = BasePCItems()

    base_pc.setup(argv)

    # Generate libsoup-2.4.pc
    replace_multi(base_pc.top_srcdir + '/libsoup-2.4.pc.in',
                  base_pc.srcdir + '/libsoup-2.4.pc',
                  base_pc.base_replace_items)

    # Generate libsoup-gnome-2.4.pc
    replace_multi(base_pc.top_srcdir + '/libsoup-gnome-2.4.pc.in',
                  base_pc.srcdir + '/libsoup-gnome-2.4.pc',
                  base_pc.base_replace_items)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
