import subprocess
import sys
import json


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])


def update() -> 'Updates pip packages':
    print("Getting packages")
    a = subprocess.Popen([sys.executable, "-m", "pip", "list", "--local", "--outdated", "--format", "json"],
                         stdout=subprocess.PIPE)
    out, err = a.communicate()
    dict = json.loads(out)
    ##parsing plz wait
    if dict == []:  # check if no updates are available
        print('Nothing to update')
        exit()
    else:
        for x in dict:  # installing everything
            print('Installing {}'.format(x['name']))
            install(x['name'])


update()
