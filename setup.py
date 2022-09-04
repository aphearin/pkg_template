import os
from setuptools import setup, find_packages


PACKAGENAME = "pkg_template"
__version__ = None
pth = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "pkg_template", "_version.py"
)
with open(pth, "r") as fp:
    exec(fp.read())


setup(
    name=PACKAGENAME,
    version=__version__,
    author="Andrew Hearin",
    author_email="ahearin@anl.gov",
    description="Some package",
    long_description="Just some package",
    install_requires=["numpy"],
    packages=find_packages(),
    url="https://github.com/aphearin/pkg_template",
    package_data={"pkg_template": ("tests/testing_data/*.dat",)},
)
