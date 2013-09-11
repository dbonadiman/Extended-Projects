"""
Problem
-------
**RSS Feed Creator**
Given a link to RSS/Atom Feed,
get all posts and display them.

Solution
--------
The solution is provided using urllib2 for
the http get and mindom for the parsing of the
xml

Author
------
dbonadiman

"""
import sys
from xml.dom import minidom
import urllib2


def rss_read(link):
    """
    This function accept either an rss or an atom link
    and returns a list of tuple in the form
    (title, link)

    parameter:
    link ==> a valid link to an rss
    """
    s = urllib2.urlopen(link).read()
    xmldoc = minidom.parseString(s)
    itemlist = xmldoc.getElementsByTagName('item')
    items = []
    if itemlist:
        for s in itemlist:
            items.append((s.getElementsByTagName('title')[0].childNodes[0].data,
                         s.getElementsByTagName('link')[0].childNodes[0].data))
    else:
        itemlist = xmldoc.getElementsByTagName('entry')
        for s in itemlist:
            items.append((s.getElementsByTagName('title')[0].childNodes[0].data,
                          s.getElementsByTagName('link')[0].attributes["href"].value))
    return items


def print_rss(items):
    """
    This function prints a list of RSS items
    in the console

    Parameters:
    items => the list of items (title, link)

    Tests:

    >>> print_rss([('title','link')])
    title
    -->link
    <BLANKLINE>
    """
    for item in items:
        print item[0]
        print '-->'+item[1]+'\n'


def main():
    try:
        items = rss_read("http://example.com/foo/bar/rss.xml")
        print_rss(items)
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
