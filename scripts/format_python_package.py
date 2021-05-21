#!/bin/bash

import os
import argparse
import subprocess


def _replace_pkg_template_with_pkgname(pkg_fname, new_pkgname):
    with open(pkg_fname, "r") as f:
        new_raw_lines = [
            raw_line.replace("pkg_template", new_pkgname) for raw_line in f
        ]

    with open(pkg_fname, "w") as f:
        for line in new_raw_lines:
            f.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pkgname", help="Name of the package being created")
    parser.add_argument("rootdir", help="Parent directory of the new package")
    args = parser.parse_args()
    pkgname = args.pkgname
    rootdir = args.rootdir
    root_dirname_pkg = os.path.join(rootdir, pkgname)

    try:
        os.makedirs(root_dirname_pkg)
    except FileExistsError:
        raise FileExistsError("{0} already exists".format(root_dirname_pkg))

    cmd = "cp pkg_template/LICENSE {0}".format(root_dirname_pkg)
    __ = subprocess.check_output(cmd, shell=True)

    cmd = "cp pkg_template/README.md {0}".format(root_dirname_pkg)
    __ = subprocess.check_output(cmd, shell=True)

    cmd = "cp pkg_template/setup.py {0}".format(root_dirname_pkg)
    __ = subprocess.check_output(cmd, shell=True)

    cmd = "cp pkg_template/setup.cfg {0}".format(root_dirname_pkg)
    __ = subprocess.check_output(cmd, shell=True)

    cmd = "cp pkg_template/.gitignore {0}".format(root_dirname_pkg)
    __ = subprocess.check_output(cmd, shell=True)

    cmd = "cp -r pkg_template/pkg_template {0}".format(root_dirname_pkg)
    __ = subprocess.check_output(cmd, shell=True)

    name1 = os.path.join(root_dirname_pkg, "pkg_template")
    name2 = os.path.join(root_dirname_pkg, pkgname)
    cmd = "mv {0} {1}".format(name1, name2)
    __ = subprocess.check_output(cmd, shell=True)

    #  Search for 'pkg_template' and replace with pkgname in the following files:
    setup_fname = os.path.join(root_dirname_pkg, "setup.py")
    readme_fname = os.path.join(root_dirname_pkg, "README.md")
    fnames_to_modify = [setup_fname, readme_fname]
    for fname in fnames_to_modify:
        _replace_pkg_template_with_pkgname(fname, pkgname)
