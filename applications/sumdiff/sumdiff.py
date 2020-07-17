"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


sums = {}
diffs = {}

# Loop through every 2-combination of elements in `q`, store pairs that make a particular sum, and pairs that make a particular difference.
for i in q:
    for j in q:

        # Sums
        s = f(i) + f(j)

        # Store the pair that makes this sum
        if s in sums:
            sums[s].append((i, j))
        else:
            sums[s] = [(i, j)]

        # Differences
        d = f(i) - f(j)

        # Store the pair that makes this difference
        if d in diffs:
            diffs[d].append((i, j))
        else:
            diffs[d] = [(i, j)]

# If a key appears in `sums` AND in
# `diffs`, all those sums must equal all those diffs.
for sum_key in sums:
    if sum_key in diffs:

        # If they do, print out all combinations of sums and differences thatare equal to each other
        for s in sums[sum_key]:
            for d in diffs[sum_key]:  # these 0's and 1's will be i and j
                a, b, c, d = s[0], s[1], d[0], d[1]

                # Check to make sure it's correct
                assert f(a) + f(b) == f(c) - f(d)

                print(
                    f"f({a}) + f({b}) = f({c}) - f({d})"
                    f"    {f(a)} + {f(b)} = {f(c)} - {f(d)}"
                )
