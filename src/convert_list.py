# script written by Shadowdara

# SCRIPTS ARE ONLY FOR IMPORTING!!!

import os
import sys
import configparser

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
        f = open(os.path.join(path, output_file6), 'wt', encoding = 'UTF-8')

        h.write('<ul>\n')

        for index, e in enumerate(lines):
            if index == 0:
                continue

            name = e.split(",")[0]
            user = e.split(",", 2)[2].split(",")[0].strip()

            h.write(f'<li><a href="https://github.com/{user}/{name}">{name}</li>\n')

            p.write(f'<!-- {name} --> <a href="https://github.com/{user}/{name}"><img src="https://github-readme-stats.vercel.app/api/pin/?username={user}&theme={theme}&repo={name}" alt="{name}"></a>\n')

            j.write(f'{name}\n')

        h.write('</ul>\n')

        c = open(os.path.join(path, template1), 'r', encoding = 'UTF-8')
        d = open(os.path.join(path, template2), 'r', encoding = 'UTF-8')

        c_content = c.read()
        d_content = d.read()

        a.write(c_content)

        p.close()

        p = open(os.path.join(path, output_file3), 'r', encoding = 'UTF-8')

        a.write(p.read())

        a.write(d_content)

        file_info = configparser.ConfigParser()
        file_info.read(info, encoding = 'UTF-8')

        for section in file_info.sections():
            f.write(f'### [{section}]\n')

            for key, value in file_info.items(section):
                f.write(f'- {value}\n')
            
            f.write('\n')

    except:
        print('Error: No write Access')
        sys.exit(1)

# run on execution
if __name__ == '__main__':

    theme = 'midnight-purple'

    info = 'file_info.ini'

    template1 = 'template_1.md'
    template2 = 'template_2.md'

    input_file = 'project_list.csv'

    output_file = 'del_project_list_js_var.txt'
    output_file2 = 'del_project_list_index.md'
    output_file3 = 'del_project_list_img.md'
    output_file4 = 'del_project_list.txt'
    output_file5 = 'del_project_list.md'
    output_file6 = 'file_info.md'

    path = os.path.dirname(os.path.abspath(__file__))

    read_list(path)

    print("Created the file successfully!")

    sys.exit(0)
