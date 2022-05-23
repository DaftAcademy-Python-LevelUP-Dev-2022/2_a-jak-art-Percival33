def greeter(func):
    def inner(*args):
        names_str = func(*args)
        names = [ name.capitalize() for name in names_str.split(" ")]
        names.insert(0, "Aloha")
        return " ".join(names)
    return inner


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
