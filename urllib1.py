import urllib.request, urllib.parse, urllib.error

url = 'http://data.pr4e.org/romeo.txt'
file_handle = urllib.request.urlopen(url)
for line in file_handle:
    print(line.decode().strip())