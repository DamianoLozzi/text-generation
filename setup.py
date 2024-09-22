from setuptools import setup,find_packages

setup(
    name="text_generation",
    version="0.1.0",
    author="Damiano Lozzi",
    author_email="damianolozzi1989@gmail.com",
    description="A text generation module using languagemodels",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "languagemodels==0.20.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='tests',
)