from setuptools import setup

setup(
    name='newsfeed',
    version='0.1',
    py_modules=['newsfeed'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        newsfeed=newsfeed:main
    ''',
)