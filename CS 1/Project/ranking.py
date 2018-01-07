from utils import *

"""Raymond Healy"""


# ---------------------------------------------<Required Syntax>--------------------------------------------#
def sorted_ranking_data(data, year):
    return SortedRankingData(data, year)


# ----------------------------------------------------------------------------------------------------------#

# ---------------------------------------------<Sort Function>----------------------------------------------#
def SortedRankingData(countries, year):
    if isinstance(countries, tuple):
        countries = countries[0]

    countryLst = DictValuesToList(countries)
    countryValues = []
    for country in countryLst:
        data = DataForYear(country, year)
        if data is not None:
            countryValues += [CountryValue(country.name, data)]

    countryValues.sort(key=lambda x: x.value, reverse=True)
    return countryValues


# ----------------------------------------------------------------------------------------------------------#

# --------------------------------------------<Print Functions>---------------------------------------------#
def PrintTop(sortedLst, num=10):
    num = min(len(sortedLst), num)

    for i in range(num):
        country = sortedLst[i]
        print(i + 1, ":", country.country, country.value)


def PrintBottom(sortedLst, num=10):
    num = min(len(sortedLst), num)

    for i in range(num):
        i = len(sortedLst) - 1 - i
        country = sortedLst[i]
        print(i + 1, ':', country.country, country.value)


# ----------------------------------------------------------------------------------------------------------#

# ---------------------------------------------<Standalone Run>---------------------------------------------#
def main():
    (countries, codes, regions, incomeGroups) = ReadData()
    regionLst = DictKeysToList(regions) + ["All"]
    incomeGroupLst = DictKeysToList(incomeGroups) + ["All"]

    year = 0
    region = ''
    incomeGroup = ''

    # Gather Initial Input Data
    while not 1960 <= year <= 2015:
        year = int(input('Enter Year of Interest (-1 to quit): ').strip())
        if year == -1:
            break

        if not 1960 <= year <= 2015:
            print("Not a valid year. Valid years are 1960-2015, inc.\n")
    if not year == -1:
        while not region in regionLst:
            region = input('Enter Region (enter "All" to consider all and -1 to exit): ').strip()
            if region == '-1':
                year = -1
                break
            if not region in regionLst:
                print("'", region, "' is not a valid region\n")
    if not year == -1:
        while not incomeGroup in incomeGroupLst:
            incomeGroup = input('Enter Income Group (enter "All" to consider all and -1 to exit): ').strip()
            if incomeGroup == '-1':
                year = -1
                break
            if not incomeGroup in incomeGroupLst:
                print("'", incomeGroup, "' is not a valid income group\n")

    while year != -1:
        (filteredCountries, filteredCodes) = FilterForRegion(countries, region)
        (filteredCountries, filteredCodes) = FilterForIncomeGroup(filteredCountries, incomeGroup)
        sorted = SortedRankingData(filteredCountries, year)

        print("\nTop 10 Life Expectancy for", year)
        PrintTop(sorted, 10)
        print('\nBottom 10 Life Expectancy for', year)
        PrintBottom(sorted, 10)
        print('\n')


        # clear the inputs
        year = 0
        region = ''
        incomeGroup = ''
        # Get New Inputs
        while not 1960 <= year <= 2015:
            year = int(input('Enter Year of Interest (-1 to quit): ').strip())
            if year == -1:
                break

            if not 1960 <= year <= 2015:
                print("Not a valid year. Valid years are 1960-2015, inc.\n")
        if not year == -1:
            while not region in regionLst:
                region = input('Enter Region (enter "All" to consider all and -1 to exit): ').strip()
                if region == '-1':
                    year = -1
                    break
                if not region in regionLst:
                    print("'", region, "' is not a valid region\n")
        if not year == -1:
            while not incomeGroup in incomeGroupLst:
                incomeGroup = input('Enter Income Group (enter "All" to consider all and -1 to exit): ').strip()
                if incomeGroup == '-1':
                    year = -1
                    break
                if not incomeGroup in incomeGroupLst:
                    print("'", incomeGroup, "' is not a valid income group\n")


if __name__ == '__main__':
    main()
# ----------------------------------------------------------------------------------------------------------#
