from setuptools import setup, find_packages

print("""

- upload
    - build wheel: python setup1.py bdist_wheel
    - upload to server: python setup.py sdist upload -r internal

- download
    - Just pip install <package>

""")

if __name__ == '__main__':
    packageName = 'sample_repo'

    # requirements
    try:
        with open("requirements.txt", 'r') as file:
            requirement = file.readlines()
    except FileNotFoundError:  # happened when install this package on other instance
        with open(f"{packageName}.egg-info/requires.txt", 'r') as file:
            requirement = file.readlines()

    # packages
    package_root = 'src'
    package_paths = find_packages(
        where=package_root,
        exclude=['*.DS_Store']
    )
    package_paths = [f'{package_root}.{path}' for path in package_paths]
    print(package_paths)

    setup(
        name=packageName,
        version='0.0.1b0',  # versioning standard: https://www.python.org/dev/peps/pep-0440/
        description='Sample repository structure',
        author='Ka Hei Ng, Alan',
        author_email='kaheicanaan@gmail.com',
        classifiers=['Programming Language :: Python :: 3.8'],
        url='https://github.com/kaheicanaan/python-repo-template',
        packages=package_paths,
        keywords=['gbComp', 'Computation', 'pyComp'],
        install_requires=requirement,
    )
