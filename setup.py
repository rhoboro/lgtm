from setuptools import find_packages, setup


setup(
    name='lgtm',
    version='1.0.0',
    packages=find_packages(exclude=('tests',)),
    package_data={'lgtm': ['data/*']},
    install_requires=[
        'Click~=7.0',
        'Pillow~=6.2.0',
        'requests>=2.22,<2.32',
    ],
    entry_points={
        'console_scripts': [
            'lgtm=lgtm.core:cli'
        ]
    },
)
