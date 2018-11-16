#!/usr/bin/env python

import click
from build_dist_package import build_dist_package


@click.command()
@click.argument('pkg-name')
@click.option('--path', default='.', help='package path')
@click.option('--pkg-desc', default='A small example package', help='package short description')
@click.option('--pkg-url', default='https://github.com/pypa/sampleproject', help='package website url')
@click.option('--author', default='Example Author', help='author')
@click.option('--author-email', default='author@example.com', help='author email address')
def cli(pkg_name, path, pkg_desc, pkg_url, author, author_email):
    build_dist_package(pkg_name, path=path, pkg_desc=pkg_desc, pkg_url=pkg_url,
                       author=author, author_email=author_email)

