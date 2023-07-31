from setuptools import setup, find_packages

setup(
    name = 'booklover',
    version = '0.1.0',
    author = 'Kristian Olsson',
    author_email = 'kno5cac@virginia.edu',
    packages = find_packages(),
    url = 'https://github.com/kristianolsson23/DS5100-m09-package/',
    license = 'MIT',
    description = 'Package created for Booklovers in DS5100',
    install_requires = [
        "pandas"
    ],
)