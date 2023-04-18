from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='gitfluencer',
    version='0.1.4',
    description='Utility tool for interacting with the GitHub platform',
    author='jjoeldaniel',
    author_email='joeldanielrico@gmail.com',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/jjoeldaniel/gitfluencer',
    keywords=['github', 'social'],
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
