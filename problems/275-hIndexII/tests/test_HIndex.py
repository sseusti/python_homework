import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.append(str(Path(__file__).parent.parent))

from sollution import getTestCases, hIndex


def testHIndexFromFile() -> None:
    testCases = getTestCases()

    for citations, expected in testCases:
        assert hIndex(citations) == expected


@patch("test_HIndex.getTestCases")
def testHIndexWithMock(mockGetTestCases: MagicMock) -> None:
    mockGetTestCases.return_value = [
        ([100, 100, 100, 100, 100], 5),
        ([1, 1, 1, 1, 1], 1),
        ([0, 0, 0], 0),
        ([10, 10, 10, 10, 10, 10], 6),
    ]

    testCases = getTestCases()

    for citations, expected in testCases:
        assert hIndex(citations) == expected

    mockGetTestCases.assert_called_once()


@patch("test_HIndex.getTestCases")
def testHIndexWhenDataSourceFails(mockGetTestCases: MagicMock) -> None:
    mockGetTestCases.side_effect = FileNotFoundError

    with pytest.raises(FileNotFoundError):
        getTestCases()
