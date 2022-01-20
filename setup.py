from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="oligo",
    version_config=True,
    setup_requires=['setuptools-git-versioning'],
    author="hectorespert",
    author_email="hectorespertpardo@gmail.com",
    description="UNOFFICIAL Python client for i-DE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hectorespert/python-oligo",
    packages=find_packages(),
    install_requires=[
        'deprecated'
    ],
    extras_require={
        'requests': ['requests'],
        'asyncio':  ['aiohttp']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
