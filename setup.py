import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oligo",
    version="1.0.1",
    author="blackleg",
    author_email="hectorespertpardo@gmail.com",
    description="UNOFFICIAL Python client for i-DE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blackleg/python-oligo",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
