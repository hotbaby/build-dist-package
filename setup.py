import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="build-dist-package",
    version="0.1.0",
    author="Meng yangyang",
    author_email="mengyy_linux@163.com",
    description="Fast build distribute package structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License',
    url="https://github.com/hotbaby/build-dist-package",
    packages=setuptools.find_packages(),
    scripts=["build_dist_package/bin/build-dist-package"],
    install_requires=["click==7.0"],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)