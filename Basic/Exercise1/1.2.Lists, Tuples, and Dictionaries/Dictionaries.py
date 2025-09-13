# Dictionaries are used when you want to store named data as key:data pairs, and uses braces to create. We'll find
# dictionaries useful when we start working with NumPy arrays and pandas.DataFrames, where we'll want to start
# organizing our data with variable names or individual object names. A dictionary is a set that is ordered (as of
# Python 3.7), mutable, but do not allow duplicates.
# Two common purposes of dictionaries for GIS data processing is to create rows (records or observations) and to
# create columns (fields or variables) in our data. We'll start with create a row.
CA = {
 "name":"California",
 "capital":"Sacramento",
 "areakm2":423970,
 "population":39538223
}
print(len(CA))
print(type(CA))
print(CA)
print("\n")

GROVELAND = {"ELEVATION":853,
 "LATITUDE":37.8444,
 "LONGITUDE":-120.2258,
 "PRECIPITATION":176.02}
print(GROVELAND)

print("\n")

PRECIPITATION = {"GROVELAND":176.02,
 "LEE VINING":71.88,
 "PLACERVILLE":170.69}
print(PRECIPITATION["PLACERVILLE"])

PRECIPITATION["BRIDGEPORT"] = 41.4
print(PRECIPITATION)

print(PRECIPITATION.keys())
for station in PRECIPITATION.keys():
 print(PRECIPITATION[station])
print("\n")

print(GROVELAND.keys())