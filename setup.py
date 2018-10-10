import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="live_server",
    version="0.0.1",
    author="Ajit Singh",
    author_email="ajit.singh2905@gmail.com",
    description="Serves your pages for development and automatically reloads when changed.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajitid/live_server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)