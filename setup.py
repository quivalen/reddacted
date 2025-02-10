#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='reddact',
    version='1.0',
    license='MIT',

    description='reddact',
    long_description='Analyze the content of comments to identify anything that might be likely to reveal PII that you may not want correlated with your anonymous username and perform sentiment analysis on the content of those posts',
    author='Taylor Wilsdon',
    author_email='taylorwilsdon@gmail.com',
    url='https://github.com/taylorwilsdon/reddact',
    download_url='https://github.com/taylorwilsdon/reddact/archive/refs/heads/master.zip',

    classifiers=['Development Status :: 1 - Alpha',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Software Development :: Build Tools',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.11',
                 'Environment :: Console',
                 ],
    keywords = ['reddact', 'reddit', 'llm', 'pii', 'sentiment', 'analysis', 'nlp'],
    platforms=['Any'],

    scripts=[],
    provides=[],
    install_requires=['cliff', 'praw', 'nltk', 'requests', 'six', 'openai', 'rich'],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'reddact = reddact.cli:main'
        ],
        'reddit.sentiment': [
            'listing = reddact.cli:Listing',
            'user = reddact.cli:User'
        ],
    },
)
