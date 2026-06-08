# Stop using variables
# to count things!
# Instead do this:

from collections import Counter

n = Counter("amém")

print(n.most_common(3))