
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
