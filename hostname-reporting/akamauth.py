import requests
from akamai.edgegrid import EdgeGridAuth, EdgeRc

def akamai_auth():
    edgerc = EdgeRc('.edgerc')
    section = 'default'
    baseurl = 'https://%s' %edgerc.get(section, 'host')
    s =  requests.session()
    s.auth = EdgeGridAuth.from_edgerc(edgerc, section)
    return s, baseurl