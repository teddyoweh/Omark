
# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddy@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Question, il Reply :)mport pathlib
from setuptools import setup
import pathlib
 
HERE = pathlib.Path(__file__).parent

 
README = (HERE / "README.md").read_text()
 
setup(
    name="Omarke",
    version="1.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/teddyoweh/Omark",
    author="Teddy Oweh",
    author_email="teddy@teddyoweh.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['Omark'],
    include_package_data=True,
    install_requires=["opencv-python", "face_recognition"],
    entry_points={
        "console_scripts": [
            "Omark=reader.__main__:main",
        ]
    },
)