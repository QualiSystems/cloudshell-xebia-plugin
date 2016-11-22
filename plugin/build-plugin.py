from zipfile import ZipFile
import os

save_path = os.getcwd()
os.chdir('..\\ext\\')
with ZipFile(os.path.join(save_path, 'cloudshell-plugin.jar'), 'w') as plugin:
    for path, subdirs, files in os.walk(os.getcwd()):
        for name in files:
            file = os.path.join(path, name)
            plugin.write(file)
