from printable_string import PrintableString
from decorators import PostWordDecorator, PostCommaDecorator, PostEndlDecorator, PostExclaimDecorator

if __name__ == '__main__':
    custom_string = PrintableString("")
    custom_string = PostWordDecorator(custom_string, "Hello")
    custom_string = PostCommaDecorator(custom_string)
    custom_string = PostWordDecorator(custom_string, "World")
    custom_string = PostExclaimDecorator(custom_string)
    custom_string = PostEndlDecorator(custom_string)

    print(custom_string.print())  # outputs "Hello, World! "
