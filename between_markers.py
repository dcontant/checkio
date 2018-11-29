def between_markers(text, begin, end):
    i = text.find(begin)
    if i == -1:
        i = 0
    else:
        i = i+len(begin)
    j = text.find(end)
    if j == -1:
        j = len(text)
    return text[i:j]


if __name__ == '__main__':
    
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('all good')
