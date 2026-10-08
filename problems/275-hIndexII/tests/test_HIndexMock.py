from unittest.mock import MagicMock, patch
from sollution import getTestCases, hIndex

import pytest


@patch("test_HIndexMock.getTestCases")
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


@patch("test_HIndexMock.getTestCases")
def testHIndexWhenDataSourceFails(mockGetTestCases: MagicMock) -> None:
    mockGetTestCases.side_effect = FileNotFoundError

    with pytest.raises(FileNotFoundError):
        getTestCases()


@patch("test_HIndexMock.getTestCases")
def testHIndexMockCallArguments(mockGetTestCases: MagicMock) -> None:
    mockGetTestCases.return_value = [([0, 1, 3, 5, 6], 3)]

    getTestCases()

    mockGetTestCases.assert_called_once_with()


@patch("test_HIndexMock.hIndex")
def testHIndexCall(mockHIndex: MagicMock) -> None:
    mockHIndex.return_value = 3

    citations: list[int] = [0, 1, 3, 5, 6]

    result: int = hIndex(citations)

    assert result == 3
    mockHIndex.assert_called_once_with(citations)
