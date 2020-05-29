from setuptools import setup, find_packages

print("""

- upload
    - create source archive and build wheel: python setup.py sdist bdist_wheel
    - upload to server: python setup.py sdist bdist_wheel upload -r internal

- install
    - pip install <packageName>

""")

if __name__ == '__main__':
    # packages
    package_root = 'src'
    package_paths = find_packages(
        where=package_root,
        exclude=['*.DS_Store']
    )
    print('package_paths:', package_paths)

    setup(
        name='sample_repo',
        version='0.0.1b0',  # versioning standard: https://www.python.org/dev/peps/pep-0440/
        description='Sample repository structure',
        author='Ka Hei Ng, Alan',
        author_email='kaheicanaan@gmail.com',
        classifiers=['Programming Language :: Python :: 3.8'],
        url='https://github.com/kaheicanaan/python-repo-template',
        package_dir={'': 'src'},
        packages=package_paths,
        keywords=['demo'],
        install_requires=[
            'pandas==0.25.3'
        ],
        extras_require={
            'restful': ['requests']
        }
    )
