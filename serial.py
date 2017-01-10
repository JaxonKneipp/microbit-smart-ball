import urllib.request
gamename = 'YAY!!'

url = 'http://ncss.seansweb.com.au/main.php?action=i&gamename='+gamename

urllib.request.urlopen(url)
