import operator
class comb:
    def __init__(self, sum, repr):
        self.sum = sum
        self.repr = repr

# Time Complexity :
# sort the lists : klogk
# make combinations : k^2
# sort the combinations : k^2log(k^2)
# Overall Time Complexity : O(k^2log(k^2))
# Space Complexity : O(k^2) to store the combinations
def printCheapestFlights(delhi_to_mumbai, mumbai_to_delhi, k):
    delhi_to_mumbai.sort()
    mumbai_to_delhi.sort()
    # slicing the list to length k as we want only k cheapest elements
    # handling case when list has less than k elements
    onwardj = delhi_to_mumbai
    if len(onwardj) >= k:
        onwardj = onwardj[:k]
    returnj = mumbai_to_delhi
    if len(returnj) >= k:
        returnj = returnj[:k]
    sums = []
    for i in range(len(onwardj)):
        for j in range(len(returnj)):
            sums.append(comb(onwardj[i]+returnj[j], "{0}, {1}".format(onwardj[i], returnj[j])))
    sums = sorted(sums, key=operator.attrgetter("sum"))
    for sum in sums[:k]:
        print(sum.repr)

delhi_to_mumbai = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
mumbai_to_delhi = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

printCheapestFlights(delhi_to_mumbai, mumbai_to_delhi, 10)