from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.2",
    description="This contains code in the ./src dirctory of the project",
    author="Yixing Zheng",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=["setuptools"],
    entry_points={
        "packages": [
            "main = dab_project.main:main"
        ]
    }
)