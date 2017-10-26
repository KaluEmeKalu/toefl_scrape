from urllib.request import urlopen

url = "https://www.vocabulary.com/profiles/A1F53BBSTZZTSF"


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


def save_text_file(text, filename):


    with open(filename, 'w') as f:
        f.write(text)


def get_links(html_text):

    text = html_text
    link_start = "https://www.vocabulary.com/lists/"
    link_list = []

    next_word_position = text.find("wordlist shortlisting")

    while next_word_position != -1:
        start_link_position = text.find("/lists/", next_word_position)
        start_link_position += 7
        end_link_position = text.find('"', start_link_position)
        link = text[start_link_position: end_link_position]
        link = link_start + link
        link_list.append(link)
        next_word_position = text.find("wordlist shortlisting", end_link_position)


    return link_list


with open("vocab_link_list.txt", 'r') as file:
    our_html_text = file.read()

our_links = get_links(our_html_text)
first_link = our_links[0]

# Let's Open One HTML File & Save The Contents
html_text = get_html_text(first_link)
with open("first_vocab_link.txt", 'w') as file:
    file.write(html_text)
