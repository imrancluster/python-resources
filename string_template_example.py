# example of template string function

from string import Template


def main():
    # normally, we use the following formatting
    string_format = "We have to go to the {0} by {1}.".format("New Market", "bus")
    print(string_format)

    # string formatting using template with placeholders
    template_format = Template("I am reading a ${book} book by ${author}.")
    substitute_template_format = template_format.substitute(book="science fiction", author="Zafar Igbal")
    print(substitute_template_format)

    # use dictionary for substitute method
    data = {
        "book": "science fiction",
        "author": "Zafar Iqbal"
    }

    substitute_template_format = template_format.substitute(data)
    print(substitute_template_format)


if __name__ == '__main__':
    main()
