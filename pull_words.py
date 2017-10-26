from urllib.request import urlopen

url = "https://www.vocabulary.com/profiles/A1F53BBSTZZTSF"
print("\n\n attempting to open ")

# Get HTML Response From Website
response = urlopen(url)
# Read HTML Response Data
data = response.read()  # a `bytes` object
# Convert Bytes Data into UTF-8 String
html_text = data.decode('utf-8')  # a `str`object;

print(html_text)
print("\n\n finished")

