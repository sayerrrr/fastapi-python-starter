"""Python setup.py for fastapi_python_starter package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("fastapi_python_starter", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="fastapi_python_starter",
    version=read("fastapi_python_starter", "VERSION"),
    description="Awesome fastapi_python_starter created by sayerrrr",
    url="https://github.com/sayerrrr/fastapi-python-starter/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="sayerrrr",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["fastapi_python_starter = fastapi_python_starter.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
