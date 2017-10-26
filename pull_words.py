sample_vocab_list_url = "https://www.vocabulary.com/lists/181261"
author_page = "https://www.vocabulary.com/profiles/A1F53BBSTZZTSF"
url = author_page


from urllib.request import urlopen

print("\n\n attempting to open ")
response = urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8')  # a `str`;

print("\n\n finished")