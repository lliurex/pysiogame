# -*- coding: utf-8 -*-

import os
import sys

os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))

lst = ["3, 3, 2", "3, 5, 2", "3, 7, 2", "4, 3, 2", "4, 5, 2", "4, 7, 2", "5, 3, 2", "5, 5, 2", "6, 3, 2", "6, 5, 2"]

if __name__ == "__main__":
    fin = ""
    i = 1
    for each in lst:
        s = """
                <level n="%i" data="[%s]" />""" % (i, each)
        fin = fin + s
        i += 1

    FILE = "genlvls.xml"
    with open(FILE, "w") as f:
        f.write(fin)

