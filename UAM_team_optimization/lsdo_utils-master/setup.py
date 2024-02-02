from distutils.core import setup


setup(
    name='lsdo_utils',
    version='1',
    packages=[
        'lsdo_utils',
    ],
    install_requires=[
        'dash==2.15.0',
        'dash-daq==0.1.0',
        'pint',
    ],
)