import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py4k_means",
    version="0.0.1",
    author="Mgs. M. Luthfi Ramadhan",
    author_email="luthfir96@gmail.com",
    description="K-Means Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luthfi118/py4k_means",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy','pandas'
      ],
    python_requires='>=3.7'
)
