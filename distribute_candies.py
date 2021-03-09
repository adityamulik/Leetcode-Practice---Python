# n candies and is event
# candyType[i] and i is individual type
# Docs advice to have n/2 candies
import time

candies = [1,2]

# def distributeCandies():
#     start_time = time.time()
#
#     return min(len(candies) // 2, len(set(candies))), f"--- {time.time() - start_time} seconds ---"

def distributeCandies():
    start_time = time.time()
    eat = len(candies) // 2
    unique = len(set(candies))

    if unique > eat:
        return eat, f"--- {time.time() - start_time} seconds ---"

    else:
        return unique, f"--- {time.time() - start_time} seconds ---"

print(distributeCandies())