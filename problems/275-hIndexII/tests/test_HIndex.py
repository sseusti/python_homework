from sollution import getTestCases, hIndex


def testHIndexFromFile() -> None:
    testCases = getTestCases()

    for citations, expected in testCases:
        assert hIndex(citations) == expected
