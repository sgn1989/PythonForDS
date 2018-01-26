def html_list(list_items):
    """
    Function which takes list of strings as input and returns an unordered HTML list
    """
    HTML_string = "<ul>\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\n".format(item)
    HTML_string += "</ul>"
    return HTML_string

print(html_list(['first string', 'second string']))
