from distutils.core import setup

setup(
    name='nytimesarticle',
    version='0.1.0',
    author='Evan Sherlock',
    author_email='egsherlock@gmail.com',
    py_modules=['nytimesarticle'],
    url='http://github.com/evansherlock/nytimesarticle',
    license='LICENSE.txt',
    description='Fully-functional Python wrapper for the New York Times Article Search API',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.1.0",
    ],
)

