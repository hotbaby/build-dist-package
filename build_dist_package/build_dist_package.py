# encoding: utf8

import os

__all__ = ('build_dist_package',)

SETUP_TPL = """
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{pkg_name}",
    version="0.0.1",
    author="{author}",
    author_email="{author_email}",
    description="{pkg_desc}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{pkg_url}",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
"""

LICENSE_TPL = """
MIT License

Copyright (c) 2018 hotbaby

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

README_TPL = """
# {pkg_name}

{pkg_desc}
"""

REQUIREMENTS_TEST_TPL = """
pytest==3.10.0
pylint==1.9.3
flake8==3.5.0
"""


REQUIREMENTS_DEV_TPL = """
twine==1.12.1
autopep8==1.4
pylint==1.9.3
flake8==3.5.0
click==7.0
"""


def _touch_file(file_path):
    with open(file_path, 'w+'):
        pass
    return file_path


def create_structure(pkg_name, path='.', **kwargs):
    """
    create package structure.
    /pkg
        /pkg
            __init__.py
        setup.py
        LICENSE
        README.md
    """
    os.mkdir(os.path.join(path, pkg_name))
    _touch_file(os.path.join(path, pkg_name, 'setup.py'))
    _touch_file(os.path.join(path, pkg_name, 'LICENSE'))
    _touch_file(os.path.join(path, pkg_name, 'README.md'))

    os.mkdir(os.path.join(path, pkg_name, pkg_name))
    _touch_file(os.path.join(path, pkg_name, pkg_name, '__init__.py'))

    os.mkdir(os.path.join(path, pkg_name, 'tests'))
    _touch_file(os.path.join(path, pkg_name, 'tests', '__init__.py'))
    _touch_file(os.path.join(path, pkg_name, 'requirements-test.txt'))
    _touch_file(os.path.join(path, pkg_name, 'requirements-dev.txt'))


def init_setup(pkg_name, path='.', author='Author',
               author_email='author@example.com',
               pkg_desc='A small example package',
               pkg_url='https://github.com/pypa/sampleproject', **kwargs):

    file_path = os.path.join(path, pkg_name, 'setup.py')
    assert os.path.exists(file_path), '%s not exists!' % file_path

    stream = SETUP_TPL.format(pkg_name=pkg_name, author=author, author_email=author_email,
                              pkg_desc=pkg_desc, pkg_url=pkg_url)
    with open(file_path, 'w+') as f:
        f.write(stream)

    return True


def init_license(pkg_name, path='.', **kwargs):
    file_path = os.path.join(path, pkg_name, 'LICENSE')
    assert os.path.exists(file_path), '%s not exists!' % file_path

    stream = LICENSE_TPL
    with open(file_path, 'w+') as f:
        f.write(stream)

    return True


def init_readme(pkg_name, path='.', pkg_desc='', **kwargs):
    file_path = os.path.join(path, pkg_name, 'README.md')
    assert os.path.exists(file_path), '%s not exists!' % file_path

    stream = README_TPL.format(pkg_name=pkg_name, pkg_desc=pkg_desc)
    with open(file_path, 'w+') as f:
        f.write(stream)

    return True


def init_tests(pkg_name, path='.', **kwargs):
    file_path = os.path.join(path, pkg_name, 'requirements-test.txt')
    assert os.path.exists(file_path), '%s not exists!' % file_path

    stream = REQUIREMENTS_TEST_TPL
    with open(file_path, 'w+') as f:
        f.write(stream)

    return True


def init_requirements_dev(pkg_name, path='.', **kwargs):
    file_path = os.path.join(path, pkg_name, 'requirements-dev.txt')
    assert os.path.exists(file_path), '%s not exists!' % file_path

    stream = REQUIREMENTS_DEV_TPL
    with open(file_path, 'w+') as f:
        f.write(stream)

    return True


def build_dist_package(pkg_name, path='.', **kwargs):
    create_structure(pkg_name, path, **kwargs)
    init_setup(pkg_name, path, **kwargs)
    init_license(pkg_name, path, **kwargs)
    init_readme(pkg_name, path, **kwargs)
    init_tests(pkg_name, path, **kwargs)
    init_requirements_dev(pkg_name, path, **kwargs)
    print 'build %s distribution package successfully.' % pkg_name
