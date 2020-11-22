import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rangreetings',
    version='0.0.1',
    author='Randomness',
    author_email='randomnessyt92@gmail.com',
    description='A simple module that gives you a list of greetings you can use :)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/randomnessyt92/rangreetings',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)