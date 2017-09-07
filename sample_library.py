# Creating a sample library


def print_my_face():
    """
    This is a simple function in library
    :return: None
    """
    print("Face")


class my_class(object):
    """
    This is a sample class inheriting object class.
    """

    # Some member variables
    name = None
    sum = 0

    def __init__(self, naam, *args, **kwargs):
        """
        This is the initializer or constructor of the class
        :param naam: This parameter is required to set the name.
        :param args: All additional positional parameters come as tuple in args
        :param kwargs: All additional key-value parameters come as dict in kwargs
        """
        self.name = naam
        self.mem_list = args
        self.mem_dict = kwargs
        print("A new object has been created")

    def print_my_name(self):
        """
        This function prints the member variable: name
        :return: None
        """
        print(self.name)

    def print_list(self):
        """
        This function prints list if it's not empty
        :return: None
        """
        if self.mem_list:
            print(self.mem_list)

    def print_dict(self):
        """
        This function prints dictionary
        :return: None
        """
        if self.mem_dict:
            print(self.mem_dict)

    def add(self, a: int, b: int) -> None:
        """
        This function used to add two parameter and save in sum
        :param a: integer 1
        :param b: integer 2
        :return: None
        """
        self.sum = a + b
        return

    def increment(self):
        """
        This function increments sum
        :return:
        """
        self.sum += 1
