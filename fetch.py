import urllib.request

for i in range(1,12):
    url = f"https://raw.githubusercontent.com/AnujDeshmukh9/DSBD/main/A{i}.py"
    urllib.request.urlretrieve(url, f"Alpha{i}.py")