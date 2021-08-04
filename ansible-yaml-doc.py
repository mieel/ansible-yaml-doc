"""
Python script to convert defaults/main.yml file to Markdown content

Requirements:
  write the MD code as yaml comments (start with '# ') above each variable
  any real yaml code is wrapped with ```yaml
  raw links are converted, line has to only contain the link, as such:
    # https://mylink.com

usage python3 yaml-doc.py output_file.md
"""

import sys


file = 'defaults/main.yml'
content = open(file, 'r')
lines = content.readlines()

table_items = []
attribute = ''
description = ''
link = ''

content = ""
current_line_type = 'comment'
for line in lines:
    print_line = line.replace('\n', '')
    if line.startswith('---'):
        continue
    last_line_type = current_line_type

    if line.startswith('# http'):
        print_line = f"[More info]({print_line})"

    if line.startswith('# '):
        current_line_type = 'comment'
        # remove comment markers to activate md format
        print_line = f"{print_line.replace('# ', '')}"
        description = f"{description}<br/>{print_line}"
    else:
        current_line_type = 'code'
        if print_line.strip() != '':
            attribute += f"`{print_line}`<br/>"
    if line.startswith("\n"):
        current_line_type = 'break'

    # append table after each break
    if current_line_type == 'break' and last_line_type == 'code':
        item = {
            'Attribute': attribute,
            'Description': description
        }
        table_items.append(item)

        attribute = ''
        description = ''
        link = ''
out_file = sys.argv[1]


# print(table_items)
table_content = ""
table_header = ""
table_header += "| Options and defaults | Description \n"
table_header += "| :-------- | :---- | \n"
table_content += table_header
for t in table_items:
    table_row = f"|{t['Attribute']}|{t['Description']}|\n"
    table_content += table_row
print(table_content)
file = open(out_file, "w")
file.write(table_content)
file.close()
