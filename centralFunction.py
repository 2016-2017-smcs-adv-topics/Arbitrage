
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
        bullCoefficient(
            


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
#maketSummary

def mean(marketSummary):

    return sum(marketSummary)*1.0/len(marketSummary)
#mean

def findStandardDeviation(marketSummary):
    length = len(marketSummary )
    m = mean(marketSummary)
    total_sum = 0
    for i in range(length):
        total_sum += (marketSummary[i]-m)**2
    stanDev = total_sum*1.0/length
    return math.sqrt(stanDev)

#stanDev

def findGlobalMax(marketSummary):
    #need work here


return globalMax

def findS(GlobalMax, LocalMax,standDev):
    S = (GlobalMax - LocalMax)/standDev
    return S
#S is how many standard deviation to the left is the local max ( 0 derivative) from the global max

def finds
    s = 1;
    return s
# s is the coefficient for S, will be adjusted accordingly


def findLowRating(pricedata):
    Fivestar = float
    Fourstar = float
    Threestar = float
    Twostar = float
    Onestar = float
    C = (Threestar + Twostar + Onestar)/(Fivestar + Fourstar + Threestar + Twostar + Onestar)
    return C
#C is percentage of 3-star rating and below


def findc
    c = 1;
    return c
# c is the coefficient for C, will be adjusted accordingly


def findriskFactor ( sellerRating, stanDev):
    riskfactor = (1-s * S)*(c * C)
    return R
#R is the risk Factor

def findr
    r = 1;
    return r
# r is the coefficient for R, will be adjusted accordingly


def findtotalDemand (purchaseData):
    D = float
    return D

# D is the total number of transactions in the last 30 days

def findd
    d = 1;
    return d
# d is the coefficient for D, will be adjusted accordingly


def potentialProfit (GlobalMax, LocalMax):
    P =(GlobalMax - LocalMax)/GlobalMax
    return P

def findp
    p = 1;
    return p
# p is the coefficient for P, will be adjusted accordingly

def findbullCoefficient (d,D,r,R,p,P):
    BC = r*R*d*D/(p*P)
    return BC
