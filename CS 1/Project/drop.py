from utils import *

"""Raymond Healy"""


# ---------------------------------------------<Required Syntax>--------------------------------------------#
def sorted_drop_data(data):
    return SortedDropData(data)


# ----------------------------------------------------------------------------------------------------------#

# --------------------------------------------<Sorting Function>--------------------------------------------#
def SortedDropData(data):
    countryLst = DictValuesToList(data)
    drops = []
    for country in countryLst:
        dataSet = country.data
        countryDrops = []

        for i in range(len(dataSet) - 1):
            if dataSet[i] is not None:
                for j in range(i + 1, len(dataSet)):
                    if dataSet[j] is not None:
                        countryDrops += [Range(country.name, i + 1960, j + 1960, dataSet[i], dataSet[j])]
                        countryDrops = RangeSort(countryDrops)
                        if len(countryDrops) > 1:
                            countryDrops = countryDrops[:1]

        drops += countryDrops
        drops = RangeSort(drops)



    return drops


# ----------------------------------------------------------------------------------------------------------#

# --------------------------------------------<Standalone Code>---------------------------------------------#
def main():
    (countries, codes, regions, incomeGroups) = ReadData()
    (countries, codes) = FilterToCountries(countries)

    region = "All"
    incomeGroup = "All"

    (countries, codes) = FilterForRegion(countries, region)
    (countries, codes) = FilterForIncomeGroup(countries, incomeGroup)

    regionLst = DictKeysToList(regions) + ["All"]
    incomeGroupLst = DictKeysToList(incomeGroups) + ["All"]

    temp = SortedDropData(countries)
    print("Worst Life Expectancy Drops: 1960 to 2015")
    for i in range(10):
        data = temp[i]
        print(i + 1, ":", data.country, "from", data.year1, '(', data.value1, ') to', data.year2, '(', data.value2,
              ') :', data.value2 - data.value1)


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------#
