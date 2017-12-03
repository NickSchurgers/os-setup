import distro
from colorama import init, deinit

from console import Console
from distros import Fedora


class Main:

    def __init__(self):
        self.__distro = distro.id()
        self.__version = distro.major_version()

    def run(self):
        Console.info(f'OS Detected: {self.__distro} {self.__version}')
        {
            'fedora': Fedora
        }[self.__distro](self.__version).run()


if __name__ == "__main__":
    init(autoreset=True)
    main = Main()
    main.run()
    deinit()
