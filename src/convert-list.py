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
        a = open(os.path.join(path, output_file5), 'wt', encoding = 'UTF-8')

        h.write('<ul>\n')

        with open(os.path.join(path, project_list_template), 'r', encoding = 'UTF-8') as b:
            list_template = b.read

        for index, e in enumerate(lines):
            if index == 0:
                continue

            name = e.split(",")[0]
            user = e.split(",", 2)[2].split(",")[0].strip()

            h.write(f'<li><a href="https://github.com/{user}/{name}">{name}</li>\n')

            p.write(f'<!-- {name} --> <a href="https://github.com/{user}/{name}"><img src="https://github-readme-stats.vercel.app/api/pin/?username={user}&theme={theme}&repo={name}" alt="{name}"></a>\n')

            j.write(f'{name}\n')

        h.write('</ul>\n')

        print("1")

        c = open(os.path.join(path, template1), 'r', encoding = 'UTF-8')
        d = open(os.path.join(path, template2), 'r', encoding = 'UTF-8')

        print("2")

        c_content = c.read()
        d_content = d.read()

        print("3")

        a.write(c_content)

        print("4")

        p.close()

        print("5")

        p = open(os.path.join(path, output_file3), 'r', encoding = 'UTF-8')

        a.write(p.read())

        a.write(d_content)

    except:
        print('Error: No write Access')
        sys.exit(1)

# run on execution
if __name__ == '__main__':

    theme = 'midnight-purple'

    template1 = 'template_1.md'
    template2 = 'template_2.md'

    project_list_template = 'project-list-template.md'

    input_file = 'project-list.csv'
    output_file = 'project-list_js_var.txt'
    output_file2 = 'project-list_index.md'
    output_file3 = 'project-list_img.md'
    output_file4 = 'project-list.txt'

    output_file5 = 'project-list.md'

    path = os.path.dirname(os.path.abspath(__file__))

    read_list(path)

    print("Created the file successfully!")

    sys.exit(0)
