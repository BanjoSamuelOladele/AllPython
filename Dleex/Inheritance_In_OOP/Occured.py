"""Most occurred"""
from collections import Counter
from statistics import mode

name = ["Timi", "Time", "Timi", "Dele"]
occurred = Counter(name)
most = mode(name)
print(occurred)
print(most)