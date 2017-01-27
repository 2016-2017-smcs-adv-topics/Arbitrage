
from collections import Counter

class arbObject:

    def __init__(self):
        determineMarketPrice()
        potentialRisk()
        potentialProfitability()
        rudolfElasticity()
        marketEffervescence()
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
        print("Global Maxima found at %s and local maxima at %s" % (globalMaxima, localMaxima))

    for



    return marketSummary

def potentialRisk (marketSummary, sellerRating):
    PRC = float
    return PRC

def potentialProfitability (marketSummary, PRC):
    PPC = float
    return PPC

def marketEffervescence (purchaseData):
    MEC = float
    return MEC

def rudolfElasticity (outlierSniper):
    REC = float
    return REC

def bullCoefficient (PRC, PPC, MEC, REC):
    BC = float
    return BC
