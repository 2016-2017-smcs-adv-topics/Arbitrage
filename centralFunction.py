
from collections import Counter

class arbObject:

    def __init__(self):
        determineMarketPrice()
        potentialRisk()
        potentialProfitability()
        rudolfElasticity()
        marketEffervescence()
        self.finalCoefficient = bullCoefficient()

    def determinePurchase(self):


def determineMarketPrice (priceData):

    marketSummary = Counter(priceData)  #returns a dictionary with counted values
    priceOccurance = {}

    j = 0

    for key in priceOccurance.keys():
        for i in range(0,99):
            j += 1
            priceOccurance[key] = j

    # need to get the keys and values from the marketSummary

    for value in priceOccurance.values():
        for i in range(0,99):
            amtDupes = marketSummary[i, None]
            price = marketSummary[None, i]
            priceOccurance[value] =  amtDupes * price

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
