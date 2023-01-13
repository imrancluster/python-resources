# example of template string function

from string import Template


def main():
    # normally, we use the following formatting
    string_format = "We have to go to the {0} by {1}.".format("New Market", "bus")
    print(string_format)


if __name__ == '__main__':
    main()