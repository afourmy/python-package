from setuptools import setup, find_packages

requirements = []
with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='sample',
    version='1.0.0',
    description='A sample Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/afourmy/python-package',
    author='Antoine Fourmy',
    author_email='antoine.fourmy@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='python package pytest coverage tox',
    packages=find_packages(exclude=('contrib', 'docs', 'tests')),
    install_requires=requirements,
    extras_require={
        'dev': ['check-manifest', 'coverage'],
    },
    project_urls={
        'Source': 'https://github.com/afourmy/python-package',
    },
)
