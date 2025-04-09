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
            o.write('`;\n')

        h = open(os.path.join(path, output_file2), 'wt', encoding = 'UTF-8')
        p = open(os.path.join(path, output_file3), 'wt', encoding = 'UTF-8')
        j = open(os.path.join(path, output_file4), 'wt', encoding = 'UTF-8')

        h.write('<ul>\n')

        for index, e in enumerate(lines):
            if index == 0:
                continue

            name = e.split(",")[0]
            user = e.split(",", 2)[2].split(",")[0].strip()

            h.write(f'<li><a href="https://github.com/{user}/{name}">{name}</li>\n')

            p.write(f'<!-- {name} --> <a href="https://github.com/{user}/{name}"><img src="https://github-readme-stats.vercel.app/api/pin/?username={user}&theme={theme}&repo={name}" alt="{name}"></a>\n')

            j.write(f'user\n')

        h.write('</ul>\n')        

    except:
        print('Error: No write Access')
        sys.exit(1)

# run on execution
if __name__ == '__main__':

    theme = 'midnight-purple'

    input_file = 'project-list.csv'
    output_file = 'project-list_js_var.txt'
    output_file2 = 'project-list_index.md'
    output_file3 = 'project-list_img.md'
    output_file4 = 'project-list.txt'

    path = os.path.dirname(os.path.abspath(__file__))

    read_list(path)

    print("Created the file successfully!")

    sys.exit(0)
