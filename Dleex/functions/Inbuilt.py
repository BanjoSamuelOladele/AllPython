"""Here ae are introduce to all python in built functions"""
import string
from random import randint
from random import choices

from join import join

print(randint(0, 10))  # here we get numbers ranging from 1 to 9, start at 1 stop at 8

# this print numbers only in the square brackets and the "k=3" print any
# of the random 3 present
print(choices([1, 3, 4, 2, 5, 3, 10], k=3))

password = join(choices(string.digits + string.ascii_letters, k=3))
print(password)

name = """str("name")"""
print(name)
