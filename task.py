import json
import subprocess


def pack_installer(to_install):
    for key, value in to_install.items():
        pack_name = str(key+"=="+value)
        install_command = "pip install "+pack_name
        x = subprocess.run(install_command)
        if x.returncode == 0:
            pass
        else:
            check = False
            err.append(pack_name)
    if check:
        print('All Dependencies Installed Successfully')
    else:
        print()
        print('***************Packages Not installed******************')
        for i in err:
            print(i)

if __name__ == '__main__':
    open_file = open('pack.json','r')
    file_data = json.load(open_file)
    err = []
    to_install = file_data["Dependencies"]
    check = True
    pack_installer(to_install)
