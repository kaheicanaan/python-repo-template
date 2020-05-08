import os
import demo_package
from demo_package.utils import package_finder


if __name__ == '__main__':
    # print env
    print(os.environ)
    # print python packages
    package_finder.list_available_packages()
