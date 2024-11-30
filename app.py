from rich.console import Console
from rich.traceback import install

install()
console = Console()


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        print("Hello, world!")


if __name__ == '__main__':
    main_process = Main()
    main_process.run()
