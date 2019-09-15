from setuptools import setup, find_packages

setup(
    name="bio-platform",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "starlette",
        "graphene",
        "uvicorn",
        "pytest"
    ]
)
