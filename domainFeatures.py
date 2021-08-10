'''
Domain based features
1. Existence of DNS Record
2. Age of Domain
3. Alexa Rank
'''

import whois  # python-whois
from datetime import datetime as dt
from urllib.parse import urlparse, quote
import urllib.parse
from bs4 import BeautifulSoup


def fetchDomainFeatures(url):
    outputList = []
    domainName = ""
    # Existence of DNS record !
    dnsRecordExists = 1
    try:
        domainName = whois.whois(urlparse(url).netloc)
    except:
        dnsRecordExists = -1
    outputList.append(dnsRecordExists)
    outputList.append(domainAge(domainName))
    outputList.append(alexaRank(url))
    return outputList

# Age of domain


def domainAge(domainName):
    creationDate = domainName.creation_date
    expiryDate = domainName.expiration_date

    if isinstance(creationDate, str) or isinstance(expiryDate, str):
        try:
            creationDate = dt.strptime(creationDate, "%Y-%m-%d")
            expiryDate = dt.strptime(expiryDate, "%Y-%m-%d")
        except:
            return -1
    if ((expiryDate is None) or (creationDate is None)):
        return -1
    else:
        if type(expiryDate) is list:
            expiryDate = expiryDate[0]
        if type(creationDate) is list:
            creationDate = creationDate[0]
        ageOfDomain = abs((expiryDate - creationDate).days)
    if ((ageOfDomain/30) < 6):
        age = -1
    else:
        age = 1
    return age

# Website's Alexa Rank


def alexaRank(url):
    try:
        url = urllib.parse.quote(url)
        rank = BeautifulSoup(urllib.request.urlopen(
            "http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']
        rank = int(rank)
    except TypeError:
        return -1
    if rank < 100000:
        return 1
    else:
        return 0
