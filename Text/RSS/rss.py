from xml.dom import minidom
import urllib2

def rss_read(link):
    s = urllib2.urlopen(link).read()
    xmldoc = minidom.parseString(s)
    itemlist = xmldoc.getElementsByTagName('item')
    items = []
    if itemlist:
        for s in itemlist :
            items.append((s.getElementsByTagName('title')[0].childNodes[0].data,s.getElementsByTagName('link')[0].childNodes[0].data))
    else:
        itemlist = xmldoc.getElementsByTagName('entry')
        for s in itemlist :
            items.append((s.getElementsByTagName('title')[0].childNodes[0].data,s.getElementsByTagName('link')[0].attributes["href"].value))
    return items

def print_rss(items):
    for item in items:
        print '!!!\033[1m'+ item[0]+'\033[0m!!!'
        print '-->'+item[1]+'\n'

def main():
    try:
        items = rss_read("http://example.com/foo/bar/rss.xml")
        print_rss(items)
    except:
        print("Please add a valid feed")
if __name__=="__main__":
    main()