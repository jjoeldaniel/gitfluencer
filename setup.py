from setuptools import setup, find_packages

setup(
    name='gitfluencer',
    version='0.1.4',
    description='Utility tool for interacting with the GitHub platform',
    author='jjoeldaniel',
    author_email='joeldanielrico@gmail.com',
    url='https://github.com/jjoeldaniel/gitfluencer',
    packages=find_packages(),
    install_requires=[
        'PyGithub',
        'Requests',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'gitfluencer=gitfluencer.app:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
