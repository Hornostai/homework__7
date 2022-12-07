from setuptools import setup, find_namespace_packages

#інструкції для встановлення проекту
setup(
    name = "sort_your_folders",
    version="0.1.0", 
    author="developer",
    author_email="gmail.com",
    description="Hw 7. Clean folder",
    license="MIT"
)

classifiers=[
        "Python  version :: Pzthon :: 3",
        "Licence :: OSI Approved :: MIT Licence",
        "Operatin Sistem :: OS Independent",
    ],
packages=find_namespace_packages("src")
entry_points={'console_scripts': [
        'clean=clean_folder.clean:main']}