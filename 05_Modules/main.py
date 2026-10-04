import stats
import math

text = input("Write out scores here, separated by commas: ")

scores = []

for piece in text.split(","):
    scores.append(float(piece))

print(stats.calcAvg(scores))

#Making use of a standard python library
print(f"Average rounded up: {math.ceil(stats.calcAvg(scores))}")