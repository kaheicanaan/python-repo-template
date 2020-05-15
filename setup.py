from setuptools import setup, find_packages

print("""

- upload
    - create source archive and build wheel: python setup.py sdist bdist_wheel
    - upload to server: python setup.py sdist bdist_wheel upload -r internal

- install
    - pip install <packageName>

""")

if __name__ == '__main__':
    packageName = 'sample_repo'

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
        install_requires=[
            'pandas==0.25.3'
        ],
        extras_require={
            'restful': ['requests']
        }
    )
