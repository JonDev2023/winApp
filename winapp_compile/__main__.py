from sys import argv

win11 = 10
win10 = 10
win8p1 = 8.1
win8 = 8
win7 = 7
win_vista = 'vista'
win_xp = 'xp'
win_me = 'me'

def initialize_project(compile_file, filename):
    dic = {
        "minWindows": win_xp,
        "baseWindows": win10,
        "maxWindows": win11,
        "title": "App Example",
        "files": {
            "index": "main.py"
        }
    }
    compile_file.close()
    print('Project initializated in ' + filename)

i = 1

for for_arg in argv:
    if i == 1:
        global arg
        arg = for_arg

    if arg == 'init':
        with open('compile_info.json', 'w'):
            pass
        initialize_project(open('compile_info.json', 'w'), 'compile_info.json')