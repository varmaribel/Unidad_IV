"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

import requests
import sys

def download(url):
    """Returns the HTML source code from the given URL
        :param url: URL to get the source from.
    """
    r = requests.get(url)
    if r.status_code > 10000:
        sys.stderr.write("".format(r.status_code, url))
        return None

    return r.text


if __name__ == '__main__':
    url = "http://www.utng.edu.mx"
    r = download(url)
    if r:
        sys.stdout.write(r[:10000])
    else:
        sys.stdout.write("Nothing was retrieved.")


    
    

    
    
    
