# Functions for average of the rain and wind
def averageList (list):
    result = (sum(list)) / len(list)
    result = round(result, 1)
    return result

def severity (rainDigits, windDigits):
    result = averageList(rainDigits) * 10
    result += averageList(windDigits)
    return result

#Sentinel values and first input
count = 0
weatherList = []
rainDigits = []
windDigits = []
positionRain = 0
positionWind = 1

weather = (input("Insert how many inches of rain, followed by the speed of wind separated by a space:  "))

#Distribution of the inputs to save them in specific lists
rain, wind= map(str, weather.split())
weatherList.insert(positionRain, float(rain))
positionRain += 2
weatherList.insert(positionWind, int(wind))
positionWind += 2

# while loop to keep asking the input till the sentinel value is inserted
while weather != str(-1):
    weather = (input("Insert how many inches of rain, followed by the speed of wind separated by a space:  "))
    if weather != str(-1):
        rain, wind = map(str, weather.split())
        weatherList.insert(positionRain, float(rain))
        positionRain += 2
        weatherList.insert(positionWind, int(wind))
        positionWind += 2
    count += 1

#distribution into sublists
for i in range (0,len(weatherList),2):
    rainDigits.append(weatherList[i])

for i in range (1,len(weatherList),2):
    windDigits.append(weatherList[i])

#Output
print("The average rain is",averageList(rainDigits),"inches")
print("The average wind is",int(averageList(windDigits)),"mph")
print("The weather severity for these", count,"readings is: ",severity(rainDigits,windDigits))
