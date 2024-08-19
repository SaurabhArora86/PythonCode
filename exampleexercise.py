# Secret Code language
# User enters inuput, if length of charcaters is < 3 reverese it
# if length of characters is > 3, take out first character append it at end and add 3 random characters at begining and at end
# reverse it for decoding
import random
import string

val = input("Enter String value")

# if (isinstance(val, str)):
#     raise TypeError("DataType is not string")

if (len(val) < 3):
    # String slicing
    print("Encoded value is: ", val[::-1])
else:
    finalVal = val[1:]+val[0]
    res1 = ''.join(random.choices(string.ascii_lowercase +
                                  string.digits, k=3)
                   )
    res2 = ''.join(random.choices(string.ascii_lowercase +
                                  string.digits, k=3)
                   )
    outcome = res1+finalVal+res2
    print(f'"Encoded value is ", {outcome} ')
