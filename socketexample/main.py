#
# Main function
#

import argparse
from socketprogram import run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--run", help="pleas input server or client")
    arguments = parser.parse_args()
    run_input = arguments.run

    if run_input in ['server', 'client']:
        run(run_input)
    else:
        print("Please pass correct argument")


if __name__ == "__main__":
    main()
