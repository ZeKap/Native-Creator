# NativeCreator
This little python script will create any app from any web page using `nativefier` *(required)*, store them in your home (in `~/Nativer/`) and create the `.desktop` file so it appears in your app list.
# Usage
`python3 native-creator.py (-a/--add WEBSITE | -r/--remove) [-l/--lang LANGUAGE] [--verbose]` :
- `-a/--add WEBSITE` will create the website and shortcut and you're good to go.
- `-r/--remove` will ask you what website you want to remove, delete the corresponding folder and shortcut. No trace left behind thanks to `nativefier`.
- `-l/--lang LANGUAGE` will ask nativefier to use the app with the specified language
- `--verbose` will show verbose output of nativefier for debug
## Any suggestion ?
If you want to improve the "app", you can always do a pull request or edit on your computer, there is no license.
# Enjoy!
