import sys
from . import caco_cli

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    caco_cli.main()


if __name__ == "__main__":
    main()

