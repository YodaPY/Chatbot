from setuptools import setup, find_namespace_packages

def long_description():
    with open("README.md") as fp:
        return fp.read()

def requirements():
    with open("requirements.txt") as fp:
        return fp.read().splitlines()

setup(
    name="Chatbot",
    description="Chatbot made using Tkinter",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="YodaPY",
    url="https://github.com/YodaPY/Chatbot",
    packages=find_namespace_packages(include=["chatbot" + "*"]),
    install_requires=requirements(),
    include_package_data=True,
    python_requires=">=3.7.0,<3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3 :: Only",
    ],
)