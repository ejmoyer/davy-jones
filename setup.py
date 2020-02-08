import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="Davy Jones",
    version="0.0.1",
    author="Eric Moyer",
    author_email="ejmoyer3@comcast.net",
    url="https://github.com/ejmoyer/davy-jones",
    description="Gives Bash more of a GUI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
