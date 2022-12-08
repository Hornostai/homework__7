from setuptools import setup, find_namespace_packages
#інструкції для встановлення проекту
setup(
    name='clean_folder_anastasia',
    version='0.1.1',
    description='Hw 7. Clean folder',
    author='A.G.',
    author_email='gornanastasia3006@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean=clean_folder.clean:main']})