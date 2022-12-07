from setuptools import setup, find_namespace_packages
#інструкції для встановлення проекту
setup(
   name='clean_folder_anastasia',
    version='0.1.0',
    description='Hw 7. Clean folder',
    author='Name',
    author_email='gornanastasia3006@gmail.com',
    license='MIT',
)

classifiers=[
        "Python  version :: Pzthon :: 3",
        "Licence :: OSI Approved :: MIT Licence",
        "Operatin Sistem :: OS Independent",
    ],
packages=find_namespace_packages("src")
entry_points={'console_scripts': [
        'clean=clean_folder.clean:main']}