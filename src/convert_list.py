# script written by Shadowdara

# SCRIPTS ARE ONLY FOR IMPORTING!!!

# files required:

import os
import configparser

# read the csv table and convert it to a multiple line javascript variable
def create_files(path):
    # variables
    theme = 'midnight-purple'

    ini_info = 'file_info.ini'

    template1 = 'template_1.tp'
    template2 = 'template_2.tp'
    template3 = 'template_dev_info.tp'

    input_file = 'project_list.csv'

    output_file = 'del_project_list_js_var.txt'
    output_file2 = 'del_project_list_index.md'
    output_file3 = 'del_project_list_img.md'
    output_file4 = 'del_project_list.txt'
    output_file5 = 'project_list.md'
    output_file6 = 'dev_info.md'

    # open the files
    try:
        with open(os.path.join(path, input_file), 'r', encoding = 'UTF-8') as r:
            lines = r.readlines()

    except FileNotFoundError as e:
        print(f"Error: {e}: {input_file}")

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

        file_info = configparser.ConfigParser(allow_no_value=True)
        file_info.read(os.path.join(path, ini_info), encoding = 'UTF-8')

        k = open(os.path.join(path, template3), 'r', encoding = 'UTF-8')

        with open(os.path.join(path, output_file6), "w", encoding="UTF-8") as g:
            g.write(k.read())
            g.write('\n')

            for section in file_info.sections():
                g.write(f"### [{section}]\n")

                for item in file_info.options(section):
                    g.write(f"- {item}\n")

                g.write("\n")
        
        a.close()
        c.close()
        d.close()
        p.close()
        j.close()
        h.close()

        print("Created all files successfully!")

    except:
        print('Error: No write Access')
