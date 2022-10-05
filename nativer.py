import os
import argparse
import shutil
from shutil import which


def checkNativefier():
    """check that nativefier exists in os"""
    if(which('nativefier') == None):
        print("nativefier is not installed")
        exit(1)


def parse():
    """verify arguments from user"""
    parser = argparse.ArgumentParser(description='Turn websites into apps in one command and store them in ~/Nativer/')
    groupParse = parser.add_mutually_exclusive_group(required=True)
    groupParse.add_argument('-a', '--add', help='Add a website')
    groupParse.add_argument('-r', '--remove', action='store_true',help='Remove a website')
    global args
    args = parser.parse_args()

def getWebName(url:str) -> str:
    """get the name of a website from it's url"""
    # get what's between protocol and firt '/' if any
    return url.split('://')[1].split('/')[0] if "://" in url else url.split('/')[0]


def getAppName(folderName:str) -> str:
    """get the name of the app from folder name"""
    return folderName.split('.com')[0]+'.com'


def createWebFolder(url:str) -> str:
    """add a website from url"""
    webName = getWebName(url)
    path = os.path.expanduser('~')+'/Nativier/'
    #generate command for os
    commandAdd = 'nativefier '+url+' '+path+' --name '+webName
    os.system(commandAdd)
    return str(path+url+"-linux-x64")


def createWebShortcut(path:str, name:str) -> str:
    """create a shortcut in app list"""
    desktopFile = """[Desktop Entry]
Type=Application
Terminal=false
Encoding=UTF-8
Version=1.1
Name={}
Icon={}/resources/app/icon.png
Exec={}/{}
Categories=Network""".format(name,
               path,
               path,
               name)
    #print(desktopFile)
    #print(os.path.expanduser('~')+'/.local/share/applications/'+name+'.desktop')
    file = open(os.path.expanduser('~')+'/.local/share/applications/'+name+'.desktop', 'w')
    file.write(desktopFile)
    file.close()


def chooseWebFolder() -> str:
    """choose website from name in list"""
    path = os.path.expanduser('~')+'/Nativier/'
    liste = os.listdir(path)
    if(len(liste) == 0):
        print("No website to remove")
        exit(0)
    print('\nChoose a website to remove or q to quit:')
    for i in range(len(liste)):
        print(str(i+1)+' - '+liste[i])
    print('')
    choiceIsPossible = False
    choice = ''
    while(not choiceIsPossible):
        choice = input('Choice: ')
        if(choice.lower() == 'q'):
                exit()
        else:
            try:
                choice = int(choice)
                if(choice <= len(liste) and choice > 0):
                    choiceIsPossible = True
                else: raise
            except:
                print('Invalid choice. Please enter a number or q to quit')
    return (liste[choice-1])


def removeWebFolder(folder) -> None:
    """remove the folder chosen"""
    shutil.rmtree(os.path.expanduser('~')+'/Nativier/'+folder)
    print(folder.split('-linux-x64')[0]+' removed')


def removeWebShortcut(appName:str) -> None:
    """remove shortcut in app list"""
    os.remove(os.path.expanduser('~')+'/.local/share/applications/'+appName+'.desktop')


if(__name__ == '__main__'):
    checkNativefier()
    parse()
    if(args.add):
        path = createWebFolder(args.add)
        createWebShortcut(path, getWebName(args.add))
    elif(args.remove):
        folder = chooseWebFolder()
        removeWebFolder(folder)
        removeWebShortcut(getAppName(folder))
