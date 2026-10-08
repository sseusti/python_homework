import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from sollution import getTestCases, hIndex


def testHIndexFromFile() -> None:
    testCases = getTestCases()

    for citations, expected in testCases:
        assert hIndex(citations) == expected
