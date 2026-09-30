"""
1154. Day of the Year
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
"""


def isLeap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def dayOfYear(date: str) -> int:
    daysInMonth = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    fmtDate = date.split("-")
    if isLeap(int(fmtDate[0])):
        daysInMonth["02"] = 29

    numOfDay = 0
    for i in range(1, int(fmtDate[1])):
        numOfDay += daysInMonth[i]

    numOfDay += int(fmtDate[2])

    return numOfDay


if __name__ == "__main__":
    date = "2019-02-10"
    print(dayOfYear(date))
