# pkg_template

```
$ cd some/random/working/directory
$ git clone https://github.com/aphearin/pkg_template.git
$ cp pkg_template/scripts/format_python_package.py ./
$ python format_python_package.py pkgname rootdir
$ rm format_python_package.py
$ rm -rf pkg_template
$ cd rootdir/pkgname
$ git init
$ git add .
$ git commit -m "Initial commit"
```
This repo is set up to enable a one-liner bash script to create a new package. After cloning this repo to location `/path/to/pkg_template`, add the following line to your .bash_profile:

```
alias newpkg='/path/to/pkg_template/scripts/create_pkg.sh'
```
To use the alias to create a new package called `pkgname`:
```
$ newpkg pkgname /parent/dir/to/write/pkgname
```
