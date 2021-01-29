from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pipefun", # Replace with your own username
    version="0.0.2",
    author="starskyC",
    author_email="cl2004_0123@aliyun.com",
    description="A lightweight package that contains pipe operators and functional tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/starskyC/pipefun",
    packages=find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
