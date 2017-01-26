
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

    j = 0

    for key, value in marketSummary.items():
        for j in range(len(marketSummary)- 1):
            beforePoint = marketSummary[j-1]
            afterPoint = marketSummary[j+1]
            occurances = key * value
            slope = ((beforePoint[0] + afterPoint[0]) / 2)
            priceOccurance.append((j, occurances, slope))

            if (0 < slope < 0.5):
                possibleMaxima.append(slope)

    j = possibleMaxima[possibleMaxima[1]]

    for x in range(len(possibleMaxima) -1):
        if possibleMaxima[x] < possibleMaxima[j]:
            j+=1
        else:
            possibleMaxima[x] = possibleMaxima[j]





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
