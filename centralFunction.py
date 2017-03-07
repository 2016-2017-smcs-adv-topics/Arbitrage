
from collections import Counter
import math
class arbObject:

    def __init__(self):
        determineMarketPrice()
        mean()
        riskFactor()
        findStandardDeviation()
        totalDemand()
        potentialProfit()
        bullCoefficient()

    def determinePurchase(self):
        print("hello") #placeholder to suppress errors

def determineMarketPrice (priceData):

    marketSummary = Counter(priceData)  #returns a dictionary with counted values
    priceOccurance = []
    possibleMaxima = []

    for key, value in marketSummary.items():
        for j in range(len(marketSummary)- 1):
            beforePoint = marketSummary[j-1]
            afterPoint = marketSummary[j+1]
            occurances = key * value
            slope = ((beforePoint[0] + afterPoint[0]) / 2)
            priceOccurance.append((j, occurances, slope))

            if (0 < slope < 0.5):
                possibleMaxima.append((slope, occurances))

    occurancesOnly = [int(i[1]) for i in possibleMaxima]
    "''"
    localMaxima = []

    if len(possibleMaxima) == 1:
        globalMaxima = possibleMaxima[0]
        print ("Global Maxima found at %d and no local Maxima" % (globalMaxima))
    else:
        reverseOrderOccurances = sorted(occurancesOnly, reversed == True)
        globalMaxima = (possibleMaxima[reverseOrderOccurances[0]], reverseOrderOccurances[0])
        j = 1
        while j < len(reverseOrderOccurances):
            localMaxima.append((possibleMaxima[reverseOrderOccurances[j]], reverseOrderOccurances[j]))
            j += 1
        print("Global Maxima found at %s and local maxima at %s" % (globalMaxima, localMaxima))

    i = 1

    return marketSummary

def mean(marketSummary):

    return sum(marketSummary)*1.0/len(marketSummary)

def findStandardDeviation(marketSummary):
    length = len(marketSummary )
    m = mean(marketSummary)
    total_sum = 0
    for i in range(length):
        total_sum += (marketSummary[i]-m)**2
    stanDev = total_sum*1.0/length
    return math.sqrt(stanDev)





def potentialRisk (marketSummary, sellerRating, stanDev):
    SD =  ()
    PRC = float
    return PRC

def riskFactor (marketSummary, PRC):
    PPC = float
    return PPC

def totalDemand (purchaseData):
    MEC = float
    return MEC

def potentialProfit (outlierSniper):
    REC = float
    return REC

def bullCoefficient (PRC, PPC, MEC, REC):
    BC = float
    return BC
