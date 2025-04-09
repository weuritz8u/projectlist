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
    template3 = 'template_3.tp'

    template4 = 'template_dev_info.tp'

    input_file = 'project_list.csv'

    output_file = 'del_project_list_js_var.txt'

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

        j = open(os.path.join(path, output_file4), 'wt', encoding = 'UTF-8')
        a = open(os.path.join(path, output_file5), 'wt', encoding = 'UTF-8')

        c = open(os.path.join(path, template1), 'r', encoding = 'UTF-8')
        d = open(os.path.join(path, template2), 'r', encoding = 'UTF-8')
        w = open(os.path.join(path, template3), 'r', encoding = 'UTF-8')

        a.write(c.read() + '\n\n')

        for index, e in enumerate(lines):
            if index % 2 != 0:
                a.write('<div>\n')
                div_end = True

            if index == 0:
                continue

            name = e.split(",")[0]
            user = e.split(",", 2)[2].split(",")[0].strip()

            a.write(f'    <!-- {name} --> <a href="https://github.com/{user}/{name}"><img src="https://github-readme-stats.vercel.app/api/pin/?username={user}&theme={theme}&repo={name}" alt="{name}"></a>\n')

            if not index % 2 != 0:
                a.write('</div>\n\n\n')
                div_end = False

            j.write(f'{name}\n')
        
        if div_end:
            a.write('</div>\n')

        a.write('\n\n' + d.read() + '\n\n')
        a.write('<ul>\n')

        for index, e in enumerate(lines):
            if index == 0:
                continue

            name = e.split(",")[0]
            user = e.split(",", 2)[2].split(",")[0].strip()

            a.write(f'<li><a href="https://github.com/{user}/{name}">{name}</li>\n')

        a.write('</ul>')
        a.write('\n\n\n' + w.read())

        file_info = configparser.ConfigParser(allow_no_value=True)
        file_info.read(os.path.join(path, ini_info), encoding = 'UTF-8')

        k = open(os.path.join(path, template4), 'r', encoding = 'UTF-8')

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
        j.close()

        print("\nCreated all files successfully!\n")

    except:
        print('Error: No write Access')
