from setuptools import setup, find_packages

setup(
    name='gitfluencer',
    version='0.1.0',
    description='Utility tool for interacting with the GitHub platform',
    author='jjoeldaniel',
    author_email='joeldanielrico@gmail.com',
    url='https://github.com/jjoeldaniel/gitfluencer',
    packages=find_packages(),
    install_requires=[
        'github3.py',
        'python-dotenv',
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
        'License :: Absolutely not OSI Approved :: WTFPL License',
        'Programming Language :: Python :: 3.x',
    ],
)
