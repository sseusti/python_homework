"""
275. H-Index II
Given an array of integers citations where citations[i] is the number of citations a researcher
received for their ith paper and citations is sorted in non-descending order,
return the researcher's h-index.
"""

PATH = "problems/275-hIndexII/data/hIndexTest.txt"


def hIndex(citations: list[int]) -> int:
    citations = sorted(citations, reverse=True)

    hIndexValue: int = 0

    for i, citation in enumerate(citations, start=1):
        if citation >= i:
            hIndexValue = i
        else:
            break

    return hIndexValue


def getTestCases() -> list[tuple[list[int], int]]:
    with open(PATH) as file:
        testCases = []

        for line in file:
            citations, expected = line.strip().split("|")

            testCases.append((list(map(int, citations.split())), int(expected)))

    return testCases


if __name__ == "__main__":
    citations = [0, 1, 3, 5, 6]
    print(hIndex(citations))
