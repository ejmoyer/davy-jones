import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="davyjones",
    version="0.0.1",
    author="Eric Moyer",
    author_email="ejmoyer3@comcast.net",
    url="https://github.com/ejmoyer/davy-jones",
    description="TBA.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
