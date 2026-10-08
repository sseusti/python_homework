import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.append(str(Path(__file__).parent.parent))

from sollution import getTestCases, hIndex


def testHIndexFromFile() -> None:
    testCases = getTestCases()

    for citations, expected in testCases:
        assert hIndex(citations) == expected


@patch("test_HIndex.getTestCases")
def testHIndexWithMock(mockGetTestCases: MagicMock) -> None:
    mockGetTestCases.return_value = [([100, 100, 100, 100, 100], 5)]

    testCases = getTestCases()

    for citations, expected in testCases:
        assert hIndex(citations) == expected
