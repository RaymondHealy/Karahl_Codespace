from utils import *
import turtle as t
from random import *

"""Raymond Healy"""


# -------------------------------------------------<Stats>--------------------------------------------------#
def MedianForYear(countries, year):
    """
        Init. Conditions:   - <<countries>> containing <<Datum>> class objects, preferably in a <<dict>>
                              or <<list>>

        Final Conditions: NA, non-destructive

        Parameters: countries   : A <<tuple>> containing <<dict>>s of <<Datum>>s, of which only the first
                                  will be taken and then stored in a list
                                : **OR** A <<dict>> of <<Datum>>s, which will be cast into a <<list>>
                                : **OR** A <<list>> of <<Datum>>s, which will be used directly
                                : **OR** A <<Datum>>, whose data for the year will just be returned

                    year        : An integer representation of the year, from 1960 to 2015 inc.

        Returns: The median of life expectancies from the provided set (<<countries>>) for <<year>>
                 as a float

        Description: Takes set of <<Datum>>s and a <<year>>, and returns the floating point representation
                     of the median of the life expectancy
    """

    if isinstance(countries, tuple):  # If <<countries>> is a <<tuple>>
        # Only save the first entry
        countries = countries[0]

    if isinstance(countries, dict):  # If <<countries>> is a <<dict>>
        # Turn <<countries>> into a <<list>> of <<Datum>>s
        countries = DictValuesToList(countries)
    elif isinstance(countries, Datum):  # Otherwise if <<countries>> is just a <<Datum>>
        # Just return the data for <<countries>> from <<year>>
        return DataForYear(countries, year)

    dataLst = []
    for country in countries:
        data = DataForYear(country, year)
        if data is not None:
            dataLst += [data]

    if dataLst == []:
        return None
    else:
        dataLst.sort()
        if len(dataLst) % 2 == 1:
            return dataLst[len(dataLst) // 2]
        else:
            foo = dataLst[len(dataLst) // 2 - 1]
            bar = dataLst[len(dataLst) // 2]
            return (foo + bar) / 2


# ----------------------------------------------------------------------------------------------------------#

# -------------------------------------------<Plotting Functions>-------------------------------------------#
def Setup():
    t.ht()  # Hide the turtle
    t.speed(0)
    t.tracer(0, 0)
    t.up()
    t.screensize(500, 500)
    t.bgcolor("black")
    t.color("white")
    t.setworldcoordinates(-50, -50, 450, 450)
    t.update()


def DrawAxes():
    t.ht()

    t.color("white")
    t.rt(90)
    t.fd(10)

    t.up()
    t.fd(20)
    t.lt(90)
    t.down()
    t.write("1960", False, align="center")
    t.up()
    t.rt(90)
    t.bk(20)
    t.down()

    t.bk(10)
    t.lt(90)
    t.fd(400)
    t.rt(90)
    t.fd(10)

    t.up()
    t.fd(20)
    t.lt(90)
    t.down()
    t.write("2015", False, align="center")

    t.up()
    t.rt(90)
    t.bk(20)
    t.down()

    t.bk(10)
    t.lt(90)
    t.bk(200)

    t.up()
    t.rt(90)
    t.fd(25)
    t.lt(90)
    t.down()
    t.write("Year", False, align="center")
    t.up()
    t.lt(90)
    t.fd(25)
    t.rt(90)
    t.down()
    t.bk(200)

    t.bk(10)
    t.up()
    t.bk(20)
    t.down()
    t.write("0", False, align="center")
    t.up()
    t.fd(20)
    t.down()
    t.fd(10)

    t.lt(90)
    t.fd(200)

    t.lt(90)
    t.up()
    t.fd(25)
    t.down()
    t.write("Life\nExp.", False, align="center")
    t.up()
    t.bk(25)
    t.rt(90)
    t.down()
    t.fd(200)

    t.lt(90)
    t.fd(10)

    t.up()
    t.fd(20)
    t.down()
    t.rt(180)
    t.write("100", False, align="center")
    t.up()
    t.fd(20)

    t.fd(10)
    t.rt(90)
    t.fd(400)
    t.lt(90)

    t.update()


def PlotDataPoint(year, expectancy, color="white"):
    t.ht()
    t.color(color)
    t.down()
    (x, y) = Data2Coordinates(year, expectancy)
    t.setpos(x, y)
    t.update()


def PlotSeries(lstDataPoints, name, color='white', seriesNum=1):
    t.ht()
    t.up()
    t.color(color)
    t.setpos(10, 435 - (seriesNum - 1) * 15)
    t.down()
    t.write(name)
    t.up()

    nextValue = lstDataPoints[0]
    startingYear = 1960

    while nextValue is None and startingYear < 2015:
        startingYear += 1
        nextValue = lstDataPoints[startingYear - 1960]

    if not startingYear == 2015:
        (x, y) = Data2Coordinates(startingYear, nextValue)
        t.setpos(x, y)
        t.down()

        for year in range(startingYear, 2016):
            nextValue = lstDataPoints[year - 1960]

            if nextValue is not None:
                PlotDataPoint(year, nextValue, color)

    t.color("white")
    t.up()
    t.setpos(0, 0)
    t.update()


def PlotCountry(dictIn, key, color='white', seriesNum=1):
    country = dictIn[key]
    data = country.data

    PlotSeries(data, country.name, color, seriesNum)


def PlotRegion(dictIn, region, color='white', seriesNum=1):
    dictIn = FilterToCountries(dictIn)
    dictIn = FilterForRegion(dictIn, region)
    data = []
    for year in range(1960, 2016):
        data += [MedianForYear(dictIn, year)]

    PlotSeries(data, region, color, seriesNum)


def PlotIncomeGroup(dictIn, incomeGroup, color='white', seriesNum=1):
    dictIn = FilterToCountries(dictIn)
    dictIn = FilterForIncomeGroup(dictIn, incomeGroup)
    data = []
    for year in range(1960, 2016):
        data += [MedianForYear(dictIn, year)]

    PlotSeries(data, incomeGroup, color, seriesNum)


# ----------------------------------------------------------------------------------------------------------#

def Data2Coordinates(year, expectancy):
    x = 0
    if 1960 <= year <= 2015:
        x = (year - 1960) / 56 * 400
    else:
        raise IndexError("Invalid submitted in <<Data2Coordinates>>, valid years are between 1960 and 2015," +
                         " inclusive")

    y = expectancy / 100 * 400

    return x, y


# ---------------------------------------------<Standalone Run>---------------------------------------------#
def main():
    (countries, codes, regions, incomeGroups) = ReadData()
    regionLst = DictKeysToList(regions)
    incomeGroupLst = DictKeysToList(incomeGroups)
    codeLst = DictKeysToList(codes)

    Setup()
    DrawAxes()

    for i in range(len(incomeGroupLst)):
        PlotIncomeGroup(countries, incomeGroupLst[i], (random(), random(), random()), i + 1)

    input("Press Enter to Continue")

    t.clear()
    Setup()
    DrawAxes()
    for i in range(len(regionLst)):
        PlotRegion(countries, regionLst[i], (random(), random(), random()), i + 1)

    t.done()


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------#
