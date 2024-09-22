from setuptools import setup, find_packages

setup(
    name="text_generation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "languagemodels==0.20.0",
    ],
    description="A text generation module using languagemodels",
    author='DamianoLozzi',
    author_email='damianolozzi1989@gmail.com',
    url='',
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='tests',
)