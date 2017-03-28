import urllib.request
import os


def download(url):
	print ("downloading with urllib")
	urlSplit = os.path.basename(url)
	print (urlSplit)
	urllib.request.urlretrieve(url, urlSplit)
	print ("done")

