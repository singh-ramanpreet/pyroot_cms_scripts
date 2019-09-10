import setuptools

with open("README.md", "r") as f:
    readme = f.read()

setuptools.setup(
    name="pyroot_cms_scripts",
    version="0.1",
    author="Ramanpreet Singh",
    author_email="",
    description="CMS Style and Text for pyROOT",
    long_description=readme,
    url="https://github.com/singh-ramanpreet/pyroot_cms_scripts",
    package_dir={"pyroot_cms_scripts": "src"},
    packages=["pyroot_cms_scripts"],
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
