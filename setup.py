"""Setup configuration for the HTTP CLI package."""

from setuptools import find_packages, setup

setup(
    name="http-cli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "http_cli=http_cli.cli:main",
        ],
    },
    author="Malte Mindedal",
    description="A simple HTTP CLI client",
    python_requires=">=3.7",
)
