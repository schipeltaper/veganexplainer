# This document converts a markdown file to html file
import markdown2

# read the markdown file
with open('index.md', 'r') as file:
    markdown_text = file.read()

# convert markdown to html
html_text = markdown2.markdown(markdown_text)

# write the html file
with open('output.html', 'w') as file:
    file.write(html_text)