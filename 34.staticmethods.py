# Static methods belong to a class rather than an instance
# Static methods can be called using Instance of a class or Class itself
# They act as a utility method and are defined using @staticmethod decorator
# We need not to have self as a parameter to it as Instance is not required to call it

class Math:

    @staticmethod
    def add(a, b):
        return (a+b)


A = Math()
print(A.add(10, 2))
print(Math.add(10, 4))
