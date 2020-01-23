import setuptools
from glob import glob

setuptools.setup(
    name='ds_kit',
    version='0.0.1',
    url='https://github.com/wenmin-wu/ds-kit',
    author='WU WENMIN',
    author_email='wuwenmin1991@gmail.com',
    description='Data Science Kit',
    packages=setuptools.find_packages('.'),
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
)