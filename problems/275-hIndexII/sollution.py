"""
275. H-Index II
Given an array of integers citations where citations[i] is the number of citations a researcher
received for their ith paper and citations is sorted in non-descending order,
return the researcher's h-index.
"""


def hIndex(citations: list[int]) -> int:
    citations = citations[::-1]
    i = 0
    while i < len(citations):
        if i >= citations[i]:
            return i
        i += 1
    return len(citations)


if __name__ == "__main__":
    citations = [0, 1, 3, 5, 6]
    print(hIndex(citations))
