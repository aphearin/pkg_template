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
This is scripted in bash with the newpkg alias, executed as follows:

```
$ newpkg pkgname /parent/dir/to/write/pkgname
```
