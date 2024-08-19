'''
Method Overloading is compile time polymorphism where in a class has multiple methods with same name 
but different param list and behavior depends on number of params and type
There is a need for only single class.
It is typically used for mathematical perators and comparison operators

Whereas

Method Overriding is Run time Polymorphism where in child class inherits parent class method and adds more functionality to it
'''


class MathOperations:
    def add(self, *args):
        return (sum(args))


op = MathOperations()
print(op.add(3, 5))
print(op.add(3, 5, 7))

# Another Example


class Addition:
    # def add(datatype, *args):
    #     if datatype == 'int':
    #         answer = 0
    #     elif datatype == 'str':
    #         answer = ''

    #     print(answer)

    #     for x in args:
    #         answer = answer + x

    #     return answer

    def add(self, datatype, *args):

        # if datatype is int
        # initialize answer as 0
        if datatype == 'int':
            answer = 0

        # if datatype is str
        # initialize answer as ''
        elif datatype == 'str':
            answer = ''

        else:
            raise ValueError("Unsupported datatype. Use 'int' or 'str'.")

        # Traverse through the arguments
        for x in args:

            # This will do addition if the
            # arguments are int. Or concatenation
            # if the arguments are str
            answer = answer + x

        print(answer)


ad = Addition()
ad.add('int', 5, 6)
