from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path("src/version.py")
with open(ver_path, encoding="utf-8") as ver_file:
    # pylint: disable-next=exec-used
    exec(ver_file.read(), main_ns)

__version__ = main_ns["__version__"]

setup(
    name="LabsChecker",
    version=__version__,
    author="Me",
    include_package_data=True,
    packages=find_packages()
)