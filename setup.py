#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    'test': [
        "pytest>=5.1.3,<6",
        "pytest-trio==0.5.2",
        "pytest-xdist==1.18.1",
        "requests==2.22.0",
        "tox>=2.9.1,<3",
        "trio==0.13.0",
    ],
    'lint': [
        "black==19.3b",
        "flake8==3.4.1",
        "isort==4.3.18",
        "mypy==0.701",
        "pydocstyle>=3.0.0,<4",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
        "towncrier>=19.2.0, <20",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # noqa: W504
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc']
)


with open('./README.md') as readme:
    long_description = readme.read()


setup(
    name='dopple',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='0.4.0-alpha.0',
    description="""dopple: HTTP proxy to Unix Socket based JSON-RPC servers""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='The Ethereum Foundation',
    author_email='snakecharmers@ethereum.org',
    url='https://github.com/ethereum/dopple',
    include_package_data=True,
    install_requires=[],
    python_requires='>=3.6, <4',
    extras_require=extras_require,
    py_modules=['dopple'],
    license="Apache",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={'dopple': ['py.typed']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    entry_points={
        'console_scripts': [
            'dopple=dopple:main',
        ],
    },
)
