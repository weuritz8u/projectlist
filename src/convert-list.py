# script written by Shadowdara

import os
import sys

# read the csv table and convert it to a multiple line javascript variable
def read_list(path):
    try:
        with open(os.path.join(path, input_file), 'r', encoding = 'UTF-8') as r:
            lines = r.readlines()

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        with open(os.path.join(path, output_file), 'wt', encoding = 'UTF-8') as o:
            o.write('const list = `')
            o.writelines(lines)
            o.write('`;')

        with open(os.path.join(path, output_file2), 'wt', encoding = 'UTF-8') as h:
            h.write('<ul><li>')
            for e in lines:
                lines = lines.split(",")[0]
                h.write(lines[e])
                h.write('</li>')
             h.write('</ul>')

    except:
        print('Error: No write Access')
        sys.exit(1)

# run on execution
if __name__ == '__main__':

    input_file = 'project-list.csv'
    output_file = 'project-list_js_var.txt'
    output_file2 = 'project-list_md_index.txt'

    path = os.path.dirname(os.path.abspath(__file__))

    read_list(path)

    print("Created the file successfully!")

    sys.exit(0)
