import subprocess

from colorama import Fore


class Console:

    @classmethod
    def success(cls, msg: str):
        print(Fore.GREEN + msg)

    @classmethod
    def info(cls, msg: str):
        print(Fore.YELLOW + msg)

    @classmethod
    def run(cls, args: []):
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        out, err = p.communicate()
        if p.returncode != 0:
            print(Fore.RED + err.strip())
        else:
            print(Fore.WHITE + out.strip())
