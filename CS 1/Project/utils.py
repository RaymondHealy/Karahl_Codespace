from rit_lib import *

"""
Raymond Healy

Utilities: This task involves writing tools for reading and processing the data, as well
as defining data structures to store the data. The other tasks import and use these
tools.
"""


# ---------------------------------------------<Required Syntax>--------------------------------------------#
def read_data(filename="worldbank_life_expectancy"):
    return ReadData(filename)


def filter_region(data, region):
    return FilterForRegion(data, region.strip())


def filter_income(data, income):
    return FilterForIncomeGroup(data, income.strip())


# ----------------------------------------------------------------------------------------------------------#

# ------------------------------------------------<Constants>-----------------------------------------------#
def kNoRegionString():
    return "No Region"


def kNoIncomeString():
    return "No Income Group"


# ----------------------------------------------------------------------------------------------------------#

# --------------------------------------------<Datum Utilities>---------------------------------------------#
Datum = struct_type("Datum", (str, "name"), (str, "code"), (list, "data"), (str, "region"),
                    (str, "incomeGroup"), (str, "notes"))


def MkDatum(name='', code='', data=[], region='', incomeGroup='', notes=''):
    return Datum(name, code, data, region, incomeGroup, notes)


def DataForYear(datum, year):
    if 1960 <= year <= 2015:
        return datum.data[year - 1960]
    else:
        raise IndexError(
            "Attempted to access data for an invalid year. <<DataForYear>> only accepts years b/n 1960 and 2015, inc.")


CountryValue = struct_type("CountryValue", (str, "country"), (float, "value"))


def CountryValueSort(countryValues, reverse=False):
    if reverse:
        countryValues.sort(key=lambda x: x.value, reverse=False)
    else:
        countryValues.sort(key=lambda x: x.value, reverse=True)
    return countryValues


Range = struct_type("Range", (str, "country"), (int, "year1"), (int, "year2"),
                    (float, "value1"), (float, "value2"))


def RangeSort(ranges):
    ranges.sort(key=lambda x: x.value2 - x.value1, reverse=False)
    return ranges


# ----------------------------------------------------------------------------------------------------------#

# ---------------------------------------------<File Utilities>---------------------------------------------#
def ReadData(filename="worldbank_life_expectancy"):
    """
        Init. Conditions: A file to an expectancy data <<txt>> file formatted as nindicated in the documentation
        Final Conditions: NA

        Parameters: filepath        - A valid string filepath to the expectancy data plaintext file
                    metaFilepath    - A valid string filepath to the expectancy metadata plaintext file

        Returns: A tuple of four dictionaries.
                    idx 0:  Values are <<Datum>>s, indexed by <<name>>
                    idx 1:  Values are <<Datum>>s, indexed by <<code>>
                    idx 2:  Values are lists of <<Datum>>s, indexed by <<region>>
                    idx 3:  Values are lists of <<Datum>>s, indexed by <<incomeGroup>>

        Description: Takes the specified life-expectancy data and metadata files and returns a <<tuple>> with two
                     dictionaries of <<Datum>>s indexed by <<name>> and <<code>>, and 2 dictionaries of <<list>>s
                     of <<Datum>>s indexed by <<region>> and <<incomeGroup>>
    """

    filepath = "data/" + filename.strip() + "_data.txt"
    metaFilepath = "data/" + filename.strip() + "_metadata.txt"

    # -------------------------------<Set up the return variables>--------------------------------#
    countries = {}  # To hold the <<Datum>> entries indexed by their <<name>>
    codes = {}  # To hold the <<Datum>> entries indexed by their three-character <<code>>
    regions = {}  # To hold <<list>>s of <<Datum>> entries sorted by <<region>>
    incomeGroups = {}  # To hold <<list>>s of <<Datum>> entries sorted by <<incomeGroup>>
    # --------------------------------------------------------------------------------------------#

    # ------------------------------------<Open the data file>------------------------------------#
    f = open(filepath)  # Open the file indicated by <<filepath>> as <<f>>
    lines = f.readlines()[1:]  # Take all lines from <<f>>, discarding the first, header line
    # --------------------------------------------------------------------------------------------#

    # ------------------------------<Turn data file into <<Datum>>s>------------------------------#
    for line in lines:  # On each line from the data <<filepath>>
        data = line.split(',')[:-1]  # Split <<line>> on each comma, and discard the empty, final string
        country = MkDatum(data[0].strip(),
                          data[1].strip(), [])  # Make a new <<Datum>> instance with the specified <<name>> and <<code>>
        data = data[2:]  # Remove the name and code from <<data>> to avoid "double counting"" them

        for dP in data:  # Go through each remaining sub-strings in <<data>> (refered to as data points or <<dP>>
            dP = dP.strip()  # Strip down the next number's string representation
            if dP == '':  # If <<datum>> is an empty string (i.e. no expectancy data)
                country.data += [None]  # Add a representative <<None>> in the data slot for that year
            else:  # Otherwise (if there is expectancy data for the year)
                country.data += [float(dP)]
                # Add the data point as a <<float>> to the expectancy data in the slot in order from 1960 to 2015

        # Save the partial country <<Datum>> indexed by <<code>> to easily insert metadata
        codes[country.code] = country
    # --------------------------------------------------------------------------------------------#

    # -------------------------------<Switch from data to metadata>-------------------------------#
    f.close()  # Close the expectancy data file
    f = open(metaFilepath)  # Open the expectancy metadata file as <<f>>
    lines = f.readlines()[1:]  # Read all metadata sets and discard the header line
    # --------------------------------------------------------------------------------------------#

    # -------------------------<Put metadata into the country <<Datum>>s>-------------------------#
    for line in lines:  # For each data set <<line>> in the metadata file
        line = line.strip().split(',')  # Strip down the data set and separate out the components

        code = line[0]  # Salvage the country code to find the pre-existing entry, if there is one

        region = line[1]  # Take the country region from the metadata file
        if region.strip() == '':  # If no region data is provided
            region = kNoRegionString()  # Lable the region as such

        incomeGroup = line[2]  # Take the income level indicated by the file
        if incomeGroup.strip() == '':  # If no income level data is provided
            incomeGroup = kNoIncomeString()  # Lable the group as such

        notes = ''  # Create an empty string for the remainder
        if len(line) > 3:  # If there are eny entries left
            notes = str(line[3])  # Add the next entry
            if len(line) > 3:  # If there are any remaining notes
                line = line[4:]  # Strip out the previously added note sub-string
                for l in line:  # For each remaining sub-string of <<notes>>
                    notes += ',' + l  # Replace the stripped out comma from <<split>> and add the next sub-string

        if code in codes:  # If this country code was specified in the data file
            codes[code].region = region  # Label the region that the country belongs to
            codes[code].incomeGroup = incomeGroup  # Lable the country's income bracket
            codes[code].notes = notes.strip(
                ' \t\r\n"').strip()  # Annotate each country <<Datum>>, removing whitespace and double quotes
        else:  # Otherwise (if this is a new country code)
            codes[code] = MkDatum('', code, [], region, incomeGroup,
                                  notes)  # Make a new <<Datum>> to store meta-data and store that by <<code>>
    # --------------------------------------------------------------------------------------------#

    # ------------------<Fill <<countries>>, <<regions>>, and <<incomeGroups>>>-------------------#
    for datum in codes.values():  # For each country (or, <<datum>>)
        region = datum.region  # Take the <<region>> from the country data
        incomeGroup = datum.incomeGroup  # Take the <<incomeGroup>> from the country data

        countries[datum.name] = datum  # Insert <<datum>>, labled with its <<name>>

        if region in regions:  # If the <<region>> has an associated <<list>> in <<regions>>
            regions[region] += [datum]  # Append <<datum>> to that <<list>>
        else:  # Otherwise (if the <<region>> does not have an associated <<list>> in <<regions>>)
            regions[region] = [datum]  # Create a new <<list>> for the <<region>> in <<regions>>

        if incomeGroup in incomeGroups:  # If the <<incomeGroup>> has an associated <<list>> in <<incomeGroups>>
            incomeGroups[incomeGroup] += [datum]  # Append <<datum>> to that <<list>>
        else:  # Otherwise (if the <<incomeGroup>> does not have an associated <<list>> in <<incomeGroups>>)
            incomeGroups[incomeGroup] = [datum]  # Create a new <<list>> for the <<incomeGroup>> in <<incomeGroups>>
    # --------------------------------------------------------------------------------------------#

    return countries, codes, regions, incomeGroups  # Return all of the created dictionaries


# ----------------------------------------------------------------------------------------------------------#

# ------------------------------------------------<Counters>------------------------------------------------#
def NumEntries(countryList):
    return len(countryList)


def NumCountries(dictIn):
    if isinstance(dictIn, tuple):
        dictIn = dictIn[0]

    countryList = DictValuesToList(dictIn)
    num = NumEntries(countryList)
    for country in countryList:
        if country.region == kNoRegionString():
            num -= 1

    return num


# ----------------------------------------------------------------------------------------------------------#

# ------------------------------------------------<Filters>-------------------------------------------------#
def FilterForRegion(dictIn, region="All"):
    if isinstance(dictIn, tuple):
        dictIn = dictIn[0]

    countryList = DictValuesToList(dictIn)
    regionCodes = {}
    regionCountries = {}

    lst = []

    if region == "All" or region =="all":
        for country in countryList:
            if not country.region == kNoRegionString():
                lst += [country]
    else:
        for country in countryList:  # For each <<country>> in <<countryList>>
            if country.region == region:  # If <<country.incomeGroup>> matches the desired <<incomeGroup>>
                lst += [country]

    for country in lst:
        regionCodes[country.code] = country
        regionCountries[country.name] = country

    return regionCountries, regionCodes


def FilterForIncomeGroup(dictIn, incomeGroup="All"):
    if isinstance(dictIn, tuple):
        dictIn = dictIn[0]

    countryList = DictValuesToList(dictIn)
    incomeGroupCodes = {}
    incomeGroupCountries = {}

    lst = []

    if incomeGroup == "All" or incomeGroup == 'all':
        for country in countryList:
            if not country.incomeGroup == kNoIncomeString():
                lst += [country]
    else:
        for country in countryList:  # For each <<country>> in <<countryList>>
            if country.incomeGroup == incomeGroup:  # If <<country.incomeGroup>> matches the desired <<incomeGroup>>
                lst += [country]

    for country in lst:
        incomeGroupCodes[country.code] = country
        incomeGroupCountries[country.name] = country

    return incomeGroupCodes, incomeGroupCountries


def FilterToCountries(dictIn):
    data = DictValuesToList(dictIn)
    countries = {}
    codes = {}

    for country in data:
        if not country.region == kNoRegionString():
            countries[country.name] = country
            codes[country.code] = country

    return countries, codes


# ----------------------------------------------------------------------------------------------------------#

# ---------------------------------------------<Casting Tools>----------------------------------------------#
def DictValuesToList(dictionary):
    if isinstance(dictionary, tuple):
        dictionary = dictionary[0]

    return list(dictionary.values())


def DictKeysToList(dictionary):
    if isinstance(dictionary, tuple):
        dictionary = dictionary[0]

    return list(dictionary.keys())


# ----------------------------------------------------------------------------------------------------------#

# ---------------------------------------------<Print Utilities>--------------------------------------------#
def PrintValidData(datum):
    for year in range(1960, 2016):
        data = DataForYear(datum, year)
        if data is not None:
            print("Year:", year, "Life expectancy:", data)


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

def main():
    (countries, codes, regions, incomeGroups) = ReadData()
    countryLst = DictValuesToList(countries)
    regionLst = DictKeysToList(regions)
    incomeGroupLst = DictKeysToList(incomeGroups)

    print("Total Number of Entities:  ", NumEntries(countryLst))
    print("Total Number of Countries/Territories:  ", NumCountries(countries))

    print("\n\nRegions and Their Country Count:")
    for region in regionLst:
        (filteredCountries, filteredCodes) = FilterForRegion(countries, region)
        print(region, ':', NumCountries(filteredCountries))

    print("\n\nIncome Categories and Their Country Count:")
    for incomeGroup in incomeGroupLst:
        (filteredCountries, filteredCodes) = FilterForIncomeGroup(countries, incomeGroup)
        print(incomeGroup, ':  ', NumCountries(filteredCountries))

    region = input("\n\nEnter a Region Name: ").strip()
    print("Countries in the", region, "region:")
    (filteredCountries, filteredCodes) = FilterForRegion(countries, region)
    for country in filteredCountries.values():
        print(country.name, '(', country.code, ')')

    incomeGroup = input("\n\nEnter an Income Category: ").strip()
    print("Countries in the '", incomeGroup, "' Income Category:")
    (filteredCountries, filteredCodes) = FilterForIncomeGroup(countries, incomeGroup)
    for country in filteredCountries.values():
        print(country.name, '(', country.code, ')')

    sel = input("\n\nEnter the Name of a Country or Country Code (Enter to Quit):").strip()
    while sel != '':
        if sel in countries:
            print("Data for", sel)
            sel = countries[sel]
            PrintValidData(sel)

        elif sel.upper() in codes:
            print("Data for", sel)
            sel = codes[sel]
            PrintValidData(sel)
        else:
            print(sel, "is not a valid country name or code")

        sel = input("\n\nEnter the Name of a Country or Country Code (Enter to Quit):").strip()


def foo():
    (countries, codes, regions, incomeGroups) = ReadData()
    data = codes["RWA"].data

    minIdx = 0
    maxIdx = 0
    minimum = data[0]
    maximum = data[0]
    for i in range(len(data)):
        if data[i] < minimum:
            minimum = data[i]
            minIdx = i
        if data[i] > maximum:
            maximum = data[i]
            maxIdx = i

    print(minIdx + 1960)
    print(minimum)
    print('\n')
    print(maxIdx + 1960)
    print(maximum)


if __name__ == '__main__':
    main()
    # foo()
