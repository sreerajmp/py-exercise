from setuptools import setup, find_packages

setup(
    name="py-exercise",
    version="0.1.0",
    author="sreeraj",
    author_email="sreerajmp1996@gmail.com",
    description="A project containing a scrapy crawler, a split function, and a statistics module",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/sreerajmp/py-exercise",
    packages=find_packages(),
    py_modules=['split', 'statistics.statistics'],
    install_requires=[
        'scrapy',
    ],
    entry_points={
        'console_scripts': [
            'statistics=statistics.statistics:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
