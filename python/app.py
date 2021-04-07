from jnpr.junos import Device
from lxml import etree

with Device(host='dallas-fw0', user='automation', password='juniper123') as firewall:
    filter = '<configuration><interfaces><interface></interface></interfaces></configuration>'
    data = firewall.rpc.get_config(filter_xml=filter)
    print (etree.tostring(data, encoding='unicode', pretty_print=True))  
