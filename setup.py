from setuptools import setup, find_packages

setup(name='maboss_test',
    version="1.0.0a4",
    author="Lorenzo Pantolini",
    author_email="lorenzopantolini@protonmail.com",
    description="A testing library for MaBoSS models",
	install_requires = ['maboss'],
	packages=['maboss_test'],
)
