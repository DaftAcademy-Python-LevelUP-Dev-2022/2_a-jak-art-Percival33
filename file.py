def greeter(func):
    def inner(*args):
        names_str = func(*args)
        names = [ name.capitalize() for name in names_str.split(" ")]
        names.insert(0, "Aloha")
        return " ".join(names)
    return inner


def sums_of_str_elements_are_equal(func):
    def get_sum(number):
        sign = -1 if number[0] == "-" else 1
        
        sum_of_elements = 0

        for digit in number:
            if digit == "-":
                continue
            sum_of_elements += sign * int(digit)

        return sum_of_elements

    def inner(*args):
        numbers = func(*args).split(" ")
        sumA = get_sum(numbers[0])
        sumB = get_sum(numbers[1])

        if sumA == sumB:
            text = f"{sumA} == {sumB}"
        else:
            text = f"{sumA} != {sumB}"

        return text

    return inner


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
