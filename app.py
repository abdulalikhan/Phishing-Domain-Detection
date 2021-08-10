import urlFeatures
import jsFeatures
import domainFeatures

url = "https://www.google.com"

features = []
features.extend(urlFeatures.fetchURLFeatures(url))
features.extend(jsFeatures.fetchJSFeatures(url))
features.extend(domainFeatures.fetchDomainFeatures(url))

print(features)
