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


# Now We Want the First 2
# Vocab Links From Len_W's 
# Vocabulary.com profile Page
def get_links(html_text):

    text = html_text
    link_start = "https://www.vocabulary.com/lists/"
    link_list = []

    next_word_position = text.find("wordlist shortlisting")

    start_link_position = text.find("/lists/", next_word_position)
    start_link_position += 7
    end_link_position = text.find('"', start_link_position)
    link = text[start_link_position: end_link_position]
    link = link_start + link
    link_list.append(link)

    ################################
    ################################
    #### Now Let's Get The 2nd Link
    ################################
    ################################

    # We simply get the next word position
    next_word_position = text.find("wordlist shortlisting", end_link_position)

    # Then We Copy and paste lines 39 to line 44
    start_link_position = text.find("/lists/", next_word_position)
    start_link_position += 7
    end_link_position = text.find('"', start_link_position)
    link = text[start_link_position: end_link_position]
    link = link_start + link
    link_list.append(link)

    ################################
    ################################
    #### Now Let's Get The 3rd Link
    ################################
    ################################
    
    # Just Copy And Paste Fro Line 53
    next_word_position = text.find("wordlist shortlisting", end_link_position)

    # And Again We Copy and paste lines 39 to line 44
    start_link_position = text.find("/lists/", next_word_position)
    start_link_position += 7
    end_link_position = text.find('"', start_link_position)
    link = text[start_link_position: end_link_position]
    link = link_start + link
    link_list.append(link)

    return link_list


our_filename = "vocab_link_list.txt"
with open(our_filename, 'r') as file:
    our_html_text = file.read()

our_links = get_links(our_html_text)
print(our_links)
