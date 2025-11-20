from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="oligo",
    version_config=True,
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=['setuptools-git-versioning'],
    author="hectorespert",
    author_email="hectorespertpardo@gmail.com",
    description="UNOFFICIAL Python client for i-DE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hectorespert/python-oligo",
    project_urls={
        "Source": "https://github.com/hectorespert/python-oligo",
        "Issues": "https://github.com/hectorespert/python-oligo/issues",
        "Documentation": "https://github.com/hectorespert/python-oligo#readme",
    },
    packages=find_packages(),
    install_requires=[
        'deprecated'
    ],
    extras_require={
        'requests': ['requests'],
        'asyncio':  ['aiohttp']
    },
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["i-DE", "iberdrola", "energy", "client"],
    python_requires='>=3.6',
)
