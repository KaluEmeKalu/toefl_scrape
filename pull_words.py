from urllib.request import urlopen

url = "https://www.vocabulary.com/profiles/A1F53BBSTZZTSF"


def get_html_text(url):

    print("\n\n attempting to open " + url)

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


# Let's Create A Script 
# To GEt The Vocab Words 
# And Put Them in a Dictionary
def pull_words(text):

    # Instantiate words dictionary
    words_dict = {}

    # Get Beginning Point of First Word
    beginning = text.find('lang="en" word=')

    # While loop that runs as long as we can find
    # the string 'lang="en" word=' in our text
    while text.find('lang="en" word=', beginning) != -1:

        # Get Word Start & End Point
        word_start_point = text.find('"', beginning + 14)
        word_end_point = text.find('"', word_start_point + 1)

        # Get Definition Start & End Point
        start_definition = text.find('tion">', word_end_point) + 5
        end_definition = text.find('</div>', start_definition)

        # Get the Word & Definition
        word = text[word_start_point + 1 : word_end_point]
        word_definition = text[start_definition + 1 : end_definition]

        # Add Word & Definition to Dictionary
        words_dict[word] = [word_definition]

        # Start Over Again With Beginning Point of Next Word
        beginning = text.find('lang="en" word=', beginning + 1)

    return words_dict



with open("all_vocab_links.txt", 'r') as file:
    our_html_text = file.read()

words_dict = pull_words(our_html_text)
print(words_dict)