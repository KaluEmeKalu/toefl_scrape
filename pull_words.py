from urllib.request import urlopen

url = "https://www.vocabulary.com/profiles/A1F53BBSTZZTSF"

# We Turn Our Code Into A get_html_text
# Function So That Our Code is Resuable
def get_html_text(url):

    print("\n\n attempting to open ")

    # Get HTML Response From Website
    response = urlopen(url)
    # Read HTML Response Data
    data = response.read()  # a `bytes` object
    # Convert Bytes Data into UTF-8 String
    html_text = data.decode('utf-8')  # a `str`object;

    print(" finished ")
    return html_text


# Create a Function that Opens and Saves
# a text file containing
# the html_text from the website
def save_text_file(text, filename):

    # This time we will use a different
    # way to open a file
    # This does the same thing
    # but is shorter
    with open(filename, 'w') as f:
        f.write(text)

html_text = get_html_text(url)
our_filename = "vocab_link_list.txt"
save_text_file(html_text, our_filename)
