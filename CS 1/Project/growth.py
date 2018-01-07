from utils import *

"""Raymond Healy"""


# ---------------------------------------------<Required Syntax>--------------------------------------------#
def sorted_growth_data(data, year1, year2):
    return SortedGrowthData(data, year1, year2)


# ----------------------------------------------------------------------------------------------------------#

# ---------------------------------------------<Sort Function>----------------------------------------------#
def SortedGrowthData(dictIn, year1, year2):
    if year1 > year2:
        temp = year1
        year1 = year2
        year2 = temp
    countryLst = DictValuesToList(dictIn)
    countryValues = []
    for country in countryLst:
        data1 = DataForYear(country, year1)
        data2 = DataForYear(country, year2)
        if data1 is not None and data2 is not None:
            countryValues += [CountryValue(country.name.strip(), data2 - data1)]

    CountryValueSort(countryValues)
    return countryValues


# ----------------------------------------------------------------------------------------------------------#

# ---------------------------------------------<Standalone Run>---------------------------------------------#
def main():
    (countries, codes, regions, incomeGroups) = ReadData()
    regionLst = DictKeysToList(regions) + ['All']
    incomeGroupLst = DictKeysToList(incomeGroups) + ['All']

    year1 = 0
    year2 = 0
    region = ''
    incomeGroup = ''
    while not 1960 <= year1 <= 2015:
        year1 = int(input("Starting Year (1960-2015) (enter -1 to quit): ").strip())
        if year1 == -1:
            break
        if not 1960 <= year1 <= 2015:
            print("'", year1, "' Invalid\n")
    if not year1 == -1:
        while not 1960 <= year2 <= 2015:
            year2 = int(input("Ending Year (1960-2015) (enter -1 to quit): ").strip())
            if year2 == -1:
                year1 = -1
                break
            if not 1960 <= year2 <= 2015:
                print("'", year2, "' Invalid\n")
    if not year1 == -1:
        while not region in regionLst:
            region = input("Regional Filter (Enter 'All' not to filter) (Enter -1 to quit): ").strip()
            if region == '-1':
                year1 = -1
                break
            if not region in regionLst:
                print("'", region, "' Invalid\n")
    if not year1 == -1:
        while not incomeGroup in incomeGroupLst:
            incomeGroup = input("Income Group Filter (Enter 'All' not to filter) (Enter -1 to quit): ").strip()
            if incomeGroup == '-1':
                year1 = -1
                break
            if not incomeGroup in incomeGroupLst:
                print("'", incomeGroup, "' Invalid\n")

    while year1 != -1:
        (countriesFiltered, codesFiltered) = FilterForRegion(countries, region)
        (countriesFiltered, codesFiltered) = FilterForIncomeGroup(countriesFiltered, incomeGroup)

        sortedLst = SortedGrowthData(countriesFiltered, year1, year2)

        print("\nTop 10 Life Expectancy Growths:", year1, "to", year2)
        PrintTop(sortedLst)
        print("\nBottom 10 Life Expectancy Growths:", year1, "to", year2)
        PrintBottom(sortedLst)
        print('\n')





        year1 = 0
        year2 = 0
        region = ''
        incomeGroup = ''
        while not 1960 <= year1 <= 2015:
            year1 = int(input("Starting Year (1960-2015) (enter -1 to quit): ").strip())
            if year1 == -1:
                break
            if 1960 <= year1 <= 2015:
                print("'", year1, "' Invalid")
        if not year1 == -1:
            while not 1960 <= year2 <= 2015:
                year2 = int(input("Ending Year (1960-2015) (enter -1 to quit): ").strip())
                if year2 == -1:
                    year1 = -1
                    break
                if 1960 <= year2 <= 2015:
                    print("'", year2, "' Invalid")
        if not year1 == -1:
            while not region in regionLst:
                region = int(input("Regional Filter (Enter 'All' not to filter) (Enter -1 to quit): ").strip())
                if region == '-1':
                    year1 = -1
                    break
                if not region in regionLst:
                    print("'", region, "' Invalid")
        if not year1 == -1:
            while not incomeGroup in incomeGroupLst:
                incomeGroup = int(input("Income Group Filter (Enter 'All' not to filter) (Enter -1 to quit): ").strip())
                if incomeGroup == '-1':
                    year1 = -1
                    break
                if not incomeGroup in incomeGroupLst:
                    print("'", incomeGroup, "' Invalid")


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------#
