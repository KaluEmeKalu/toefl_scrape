from urllib.request import urlopen

url = "https://www.vocabulary.com/profiles/A1F53BBSTZZTSF"

# We Turn Our Code Into A get_html_text
# Function So That Our Code is Resuable
def get_html_text(url, filename):

    print("\n\n attempting to open ")

    # Get HTML Response From Website
    response = urlopen(url)
    # Read HTML Response Data
    data = response.read()  # a `bytes` object
    # Convert Bytes Data into UTF-8 String
    html_text = data.decode('utf-8')  # a `str`object;

    print(" finished ")
    return html_text

html_text = get_html_text(url)

# Open and Save a text file containing
# the html_text from the website
file = open("vocab_link_list.txt", "w")
file.write(html_text)
file.close()
