from setuptools import find_packages, setup

with open("README.md","r", encoding="utf-8") as readme:
    long_description = readme.read()
#інструкції для встановлення проекту
setup(
    name = "sort_your_folders",
    version="0.0.1", 
    author="developer",
    author_email="gornanastasia3006@gmail.com",
    description="this is program for sorted",
    long_description = long_description ,
    url="my_site.com",
    project_urls = {
        "Bugs": "project bug url",     
    }
)

classifiers=[
        "Python  version :: Pzthon :: 3",
        "Licence :: OSI Approved :: MIT Licence",
        "Operatin Sistem :: Linux"
    ]
package_dir={"": "src"},
packages=find_packages(where="srs"),
python_requires = ">=3.7"
test_require=["pytest"]
setup_requires=["pytest-runner"]
    