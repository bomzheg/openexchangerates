from setuptools import setup

setup(
    name='async_openexchangerates',
    version='0.2.0',
    description='async openexchangerates.org python API client',
    long_description=open('README.rst').read(),
    url='https://github.com/bomzheg/openexchangerates',
    license='MIT',
    author='bomzheg',
    author_email='bomzheg@gmail.com',
    packages=['openexchangerates'],
    install_requires=[
        'aiohttp',
    ],
    tests_require=[
        'pytest',
        'pytest-asyncio'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
