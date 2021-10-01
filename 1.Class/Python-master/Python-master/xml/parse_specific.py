from xml.etree import ElementTree

with open("C:\\1.Class\\Python-master\\Python-master\\xmlpodcasts.opml", 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter('outline'):
    name = node.attrib.get('text')
    url = node.attrib.get('xmlUrl')
    if name and url:
        print ('  %s :: %s' % (name, url))
    else:
        print (name)
