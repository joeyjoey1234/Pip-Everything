import subprocess
import sys
import json


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])


def update() -> 'Updates pip packages':
    # list of stuff you dont want.
    no = []
    yes_no = 'yes'
    print("Getting packages")
    a = subprocess.Popen([sys.executable, "-m", "pip", "list", "--local", "--outdated", "--format", "json"],
                         stdout=subprocess.PIPE)
    out, err = a.communicate()
    dict = json.loads(out)
    # parsing plz wait

    if dict == [1]:  # check if no updates are available
        print('Nothing to update')
        exit()
        # lets you pick what you don't want(in case version issue in PROD)
    elif yes_no != 'no':
        for x in dict:
            print(x['name'])
        while yes_no != 'no':
            dont_want: 'user input' = input("Anything you dont want? (Package name or no) ")
            no.append(dont_want)
            yes_no = dont_want

    for x in dict:  # installing everything
        if x["name"] in no:
            pass
        else:
            print('Installing {}'.format(x['name']))
            install(x['name'])


update()