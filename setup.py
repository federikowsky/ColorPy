from setuptools import setup, find_packages

setup(
    name='pycolor',
    version='1.0',
    packages=find_packages(),
    description='A Python package for color formatting in the terminal.',
    author='federikowsky',
    license='MIT',
    url='https://github.com/federikowsky/pycolor',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        # List any dependencies your package may have
    ],
)
