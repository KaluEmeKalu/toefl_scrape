sample_url = "https://www.vocabulary.com/lists/181261"
lin_w = "https://www.vocabulary.com/profiles/A1F53BBSTZZTSF"

def get_webpage(url):
    import urllib

    print("\n\n attempting to open ")
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8') # a `str`;
    return text
    print("\n\n finished")



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