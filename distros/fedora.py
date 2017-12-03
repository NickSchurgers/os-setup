from console import Console


class Fedora:

    def __init__(self, version):
        self.__version = version

    def run(self):
        Console.info('Setting cinnamon terminal to tilix')
        Console.run(
            ['gsettings', 'set', 'org.cinnamon.desktop.default-applications.terminal', 'exec', '/usr/bin/tilix']
        )
        Console.success('Default terminal set')

        Console.info('Adding Repo\'s')
        self.__setup_repos()

        Console.info('Updating dnf')
        Console.run(['sudo', 'dnf', '-y', 'update'])

    def __setup_repos(self):
        # Console.info('REPOS: Yarn')
        # Console.run(
        #     'sudo wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo')
        #
        # Console.success('REPOS: Yarn done')

        Console.info('REPOS: Dotnet core')
        Console.run(['sudo', 'rpm', '--import', 'https://packages.microsoft.com/keys/microsoft.asc'])
        Console.run([
            'sudo', 'sh', '-c', 'echo -e "[packages-microsoft-com-prod]\nname=packages-microsoft-com-prod '
                                '\nbaseurl=https://packages.microsoft.com/yumrepos/microsoft-rhel7.3-prod\nenabled=1'
                                '\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > '
                                '/etc/yum.repos.d/dotnetdev.repo'])
        Console.success('REPOS: Dotnet core done')

        Console.info('REPOS: Fedy')
        Console.info('folkswithhats')
        Console.run(['sudo', 'dnf', '-y', 'install', 'https://dl.folkswithhats.org/fedora/'
                                                     f'{self.__version}/RPMS/folkswithhats-release.noarch.rpm'])
        Console.info('rpmfusion')
        Console.run(['sudo', 'dnf', '-y', 'install', f'https://download1.rpmfusion.org/free/fedora/rpmfusion-free'
                                                     f'-release-{self.__version}.noarch.rpm'])
        Console.run(['sudo', 'dnf', '-y', 'install', f'https://download1.rpmfusion.org/nonfree/fedora/rpmfusion'
                                                     f'-nonfree-release-{self.__version}.noarch.rpm'])
        Console.success('REPOS: Fedy done')
