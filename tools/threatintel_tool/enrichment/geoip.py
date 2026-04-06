import geoip2.database
from ipwhois import IPWhois

GEO_DB_PATH = "GeoLite2-City.mmdb"

def enrich_ip(ip):
    enrichment = {}

    # GeoIP lookup
    try:
        with geoip2.database.Reader(GEO_DB_PATH) as reader:
            response = reader.city(ip)
            enrichment["country"] = response.country.name
            enrichment["city"] = response.city.name
    except Exception:
        pass

    # ASN lookup
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        enrichment["asn"] = res.get("asn")
        enrichment["org"] = res.get("network", {}).get("name")
    except Exception:
        pass

    return enrichment