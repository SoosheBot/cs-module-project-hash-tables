import random

# Read in all the words in the input text file
with open("/Users/Mahadevi/Documents/CS7/hash-tables/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()

# What words can follow other words?

words = words.split()
following_words = {}  # Keeps track of all the words that can follow a word

prev = None

for w in words:
    if prev is not None:

        # Make an empty list for the first entries
        if prev not in following_words:
            following_words[prev] = []

        # Add word to the list of those that are following_words
        following_words[prev].append(w)

    prev = w

# Words that we can start a sentence with
# Check if word starts with a capital letter
is_good_start = lambda x: x[0].isupper() or len(x) > 1 and x[1].isupper()
starting_words = [w for w in following_words.keys() if is_good_start(w)]

# Print a number of paragraphs
for _ in range(5):

    # Choose the starting word
    w = random.choice(starting_words)

    stopped = False
    punctuation_marks = ".!?"  # Stop on any of these punctuation marks

    while not stopped:
        print(w, end=" ")
        # condition of dog? at end of sentence or someting like dogs!" word longer than 1 element
        if w[-1] in punctuation_marks or len(w) > 1 and w[-2] in punctuation_marks:
            stopped = True
        else:
            # Follow to the next word in the chain
            next_words = following_words[w]
            w = random.choice(next_words)

    print("\n")