
from collections import defaultdict

class arbObject:

    def __init__(self):
        determineMarketPrice()
        potentialRisk()
        potentialProfitability()
        rudolfElasticity()
        marketEffervescence()
        self.finalCoefficient = bullCoefficient()

    def determinePurchase(self, finalCoefficient):
        self.finalCoefficient


def shellSortPrice (priceData):

    #The following finds indecies of dupes in a list (need to decipher)
    D = defaultdict(list)
    for i, item in enumerate(priceData):
        D[item].append(i)
        D = {k: v for k, v in D.items() if len(v) > 1}
    #weight items with more duplicate prices

    # shell sort the weighted/deduped list

def determineMarketPrice (priceData):

    marketSummary = quickSortPrice(priceData)  #determine 1st-99th percentiles
    twoFive = []

    for x in range(0,24):
        twoFive.append(marketSummary[x])

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
