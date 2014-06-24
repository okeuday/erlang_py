#-*-Mode:python;coding:utf-8;tab-width:4;c-basic-offset:4;indent-tabs-mode:()-*-
# ex: set ft=python fenc=utf-8 sts=4 ts=4 sw=4 et:
from distutils.core import setup
setup(
    name='erlang_py',
    py_modules=['erlang'],
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Erlang',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
    ],
    version='1.3.2',
    description='Erlang Binary Term Format for Python',
    author='Michael Truog',
    author_email='mjtruog@gmail.com',
    url='https://github.com/okeuday/erlang_py',
)
