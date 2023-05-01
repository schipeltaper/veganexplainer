import markdown2

# read the markdown file
with open('input.md', 'r') as file:
    markdown_text = file.read()

# convert markdown to html
html_text = markdown2.markdown(markdown_text)

# write the html file
with open('output.html', 'w') as file:
    file.write(html_text)