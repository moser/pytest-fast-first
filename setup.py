import setuptools

setuptools.setup(
    name="pytest-fast-first",
    version="1.0.2",
    url="https://github.com/moser/pytest-fast-first",
    author="Martin Vielsmaier",
    author_email="moser@moserei.de",
    description="Pytest plugin that runs fast tests first",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=[],
    packages=["pytest_fast_first"],
    install_requires=["pytest"],
    setup_requires=["pytest-runner"],
    tests_require=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "pytest11": ["notifier = pytest_fast_first"],
    },
)
