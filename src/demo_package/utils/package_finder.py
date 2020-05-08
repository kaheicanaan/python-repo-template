import pip


def list_available_packages():
    print(pip.get_installed_distributions())
