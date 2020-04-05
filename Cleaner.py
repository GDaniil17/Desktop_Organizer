from PIL import Image, ImageGrab
from time import sleep, localtime
import pyautogui
import os
import getpass
import time
from datetime import datetime

cur = getpass.getuser()
pyautogui.keyDown("f6")
pyautogui.hotkey('win','d')
sleep(1)
img = ImageGrab.grab(bbox = None)
tmp_pic = localtime()
name_for_pic = f"{tmp_pic[3]}_{tmp_pic[4]}_of_{tmp_pic[2]}_{tmp_pic[1]}_{tmp_pic[0]}.bmp"
img.save(f"/Users/{cur}/Desktop/{cur}/"+name_for_pic, "BMP")

"""
from time import sleep
from PIL import Image, ImageGrab
#import yadisk

#y = yadisk.YaDisk(token="AgAAAAAJTGbeAADLW6TZSbwDw0hXk9OhJAgWZ2g")

if True:#y.check_token():   
    
    
    sleep(2.5)
    img = ImageGrab.grab(bbox = None)
    
    img.save("screen.bmp", "BMP")
    #y.upload("screen.BMP", "/screen.BMP", overwrite = True)
"""

##########################################################################################
##########################################################################################

file_exists = os.path.isfile("cleaner_cash.txt")
if file_exists:
        f = open("cleaner_cash.txt", "r")
        r = f.readline()
        if len(r) != 0 and int(r) > 0:
                inp = input("Do you want to run this program again ? \n Y/N \n")
                if "y" in inp.lower():
                        pass
                else:
                        f.close()
                        exit(0)
        f = open("cleaner_cash.txt", "w")
        f.write("1")
else:
        f = open("cleaner_cash.txt", "w")
        f.write("1")
f.close()

list_for_files = set()
d_files = {}

def on_modified():
        global old
        global list_for_files
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'cleaner_cash.txt' and filename != 'Cleaner.py' and filename != 'Cleaner.pyw' and filename != "Cleaner.exe" and filename != "Extensions.txt" and filename != "extensions.txt":
                try:                      
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'
                    

                    now = datetime.now()
                    year = now.strftime("%Y")
                    #month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    #month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            #for folder_month in os.listdir(folder_destination_path):
                            #    if month == folder_month:
                            folder_destination_path = extensions_folders[extension] + "/" + year# + "/" + month
                                    #month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    #if not month_exists:
                    #    os.mkdir(folder_destination_path + "/" + month)
                    #    folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename
                    list_for_files.add(new_name)
                    d_files[new_name] = folder_destination_path + "/" + new_name
                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                    print(f"{filename} successfully added to the directory")
                    f = open(f'C:/Users/{cur}/Desktop/{cur}/List_of_files.txt', "w")
                    #f = open("f'/Users/{cur}/Desktop/{cur}/List_of_directories.txt", "w")
                    t_list = ""
                    for name_list in list_for_files:
                        t_list += name_list + " - " + d_files[name_list] + "\n"
                    f.write(t_list)
                    f.close()
                    
                except Exception:
                    if filename not in old:
                        print(filename)
                        #list_for_files += folder_destination_path + " - " + filename + "\n"
                        old.add(filename)
old = set()
extensions_folders = {
#No name
    'noname' : f"/Users/{cur}/Desktop/{cur}/Other/Uncategorized",
#Audio
    '.aif' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.cda' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.mid' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.midi' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.mp3' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.mpa' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.ogg' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.wav' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.wma' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.wpl' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
    '.m3u' : f"/Users/{cur}/Desktop/{cur}/Media/Audio",
#Text
    '.epub' : f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.cbr' : f"/Users/{cur}/Desktop/{cur}/Text/Comics",
    '.djvu' : f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.fb2' : f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.txt' : f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.doc' : f"/Users/{cur}/Desktop/{cur}/Text/Microsoft/Word",
    '.docx' : f"/Users/{cur}/Desktop/{cur}/Text/Microsoft/Word",
    '.odt ' : f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.pdf': f"/Users/{cur}/Desktop/{cur}/Text/PDF",
    '.rtf': f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.tex': f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.wks ': f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.wps': f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
    '.wpd': f"/Users/{cur}/Desktop/{cur}/Text/TextFiles",
#Video
    '.3g2': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.3gp': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.avi': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.flv': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.h264': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.m4v': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.mkv': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.mov': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.mp4': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.mpg': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.mpeg': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.rm': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.swf': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.vob': f"/Users/{cur}/Desktop/{cur}/Media/Video",
    '.wmv': f"/Users/{cur}/Desktop/{cur}/Media/Video",
#Images
    '.ai': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.bmp': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.gif': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.ico': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.jpg': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.jpeg': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.png': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.ps': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.psd': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.svg': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.tif': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.tiff': f"/Users/{cur}/Desktop/{cur}/Media/Images",
    '.CR2': f"/Users/{cur}/Desktop/{cur}/Media/Images",
#Internet
    '.asp': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.aspx': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.cer': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.cfm': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.cgi': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.pl': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.css': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.htm': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.js': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.jsp': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.part': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.php': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.rss': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
    '.xhtml': f"/Users/{cur}/Desktop/{cur}/Other/Internet",
#Compressed
    '.7z': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
    '.arj': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
    '.deb': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
    '.pkg': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
    '.rar': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
    '.rpm': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
    '.tar.gz': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
    '.z': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
    '.zip': f"/Users/{cur}/Desktop/{cur}/Other/Compressed",
#Disc
    '.bin': f"/Users/{cur}/Desktop/{cur}/Other/Disc",
    '.dmg': f"/Users/{cur}/Desktop/{cur}/Other/Disc",
    '.iso': f"/Users/{cur}/Desktop/{cur}/Other/Disc",
    '.toast': f"/Users/{cur}/Desktop/{cur}/Other/Disc",
    '.vcd': f"/Users/{cur}/Desktop/{cur}/Other/Disc",
#Data
    '.csv': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.dat': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.db': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.dbf': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.log': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.mdb': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.sav': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.sql': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.tar': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.xml': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
    '.json': f"/Users/{cur}/Desktop/{cur}/Programming/Database",
#Executables
    '.apk': f"/Users/{cur}/Desktop/{cur}/Other/Executables",
    '.bat': f"/Users/{cur}/Desktop/{cur}/Other/Executables",
    '.com': f"/Users/{cur}/Desktop/{cur}/Other/Executables",
    '.exe': f"/Users/{cur}/Desktop/{cur}/Other/Executables",
    '.gadget': f"/Users/{cur}/Desktop/{cur}/Other/Executables",
    '.jar': f"/Users/{cur}/Desktop/{cur}/Other/Executables",
    '.wsf': f"/Users/{cur}/Desktop/{cur}/Other/Executables",
#Fonts
    '.fnt': f"/Users/{cur}/Desktop/{cur}/Other/Fonts",
    '.fon': f"/Users/{cur}/Desktop/{cur}/Other/Fonts",
    '.otf': f"/Users/{cur}/Desktop/{cur}/Other/Fonts",
    '.ttf': f"/Users/{cur}/Desktop/{cur}/Other/Fonts",
#Presentations
    '.key': f"/Users/{cur}/Desktop/{cur}/Text/Presentations",
    '.odp': f"/Users/{cur}/Desktop/{cur}/Text/Presentations",
    '.pps': f"/Users/{cur}/Desktop/{cur}/Text/Presentations",
    '.ppt': f"/Users/{cur}/Desktop/{cur}/Text/Presentations",
    '.pptx': f"/Users/{cur}/Desktop/{cur}/Text/Presentations",
#Programming
    '.c': f"/Users/{cur}/Desktop/{cur}/Programming/C&C++",
    '.class': f"/Users/{cur}/Desktop/{cur}/Programming/Java",
    '.dart': f"/Users/{cur}/Desktop/{cur}/Programming/Dart",
    '.py': f"/Users/{cur}/Desktop/{cur}/Programming/Python",
    '.sh': f"/Users/{cur}/Desktop/{cur}/Programming/Shell",
    '.swift': f"/Users/{cur}/Desktop/{cur}/Programming/Swift",
    '.html': f"/Users/{cur}/Desktop/{cur}/Programming/C&C++",
    '.h': f"/Users/{cur}/Desktop/{cur}/Programming/C&C++",
#Spreadsheets
    '.ods' : f"/Users/{cur}/Desktop/{cur}/Text/Microsoft/Excel",
    '.xlr' : f"/Users/{cur}/Desktop/{cur}/Text/Microsoft/Excel",
    '.xls' : f"/Users/{cur}/Desktop/{cur}/Text/Microsoft/Excel",
    '.xlsx' : f"/Users/{cur}/Desktop/{cur}/Text/Microsoft/Excel",
#System
    '.bak' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.cab' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.cfg' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.cpl' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.cur' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.dll' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.dmp' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.drv' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.icns' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.ico' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.ini' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.lnk' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.msi' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.sys' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
    '.tmp' : f"/Users/{cur}/Desktop/{cur}/Text/Other/System",
}

if os.path.exists(f"/Users/{cur}/Desktop/Extensions.txt"):
        f = open(f"/Users/{cur}/Desktop/Extensions.txt", "r")
        s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
        while len(s) != 0:
                s = dict(map(lambda x: x.split('-'), s.split(',')))
                for i in s:
                        extensions_folders[i] = s[i]
                s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                
elif os.path.exists(f"/Users/{cur}/Desktop/{cur}/Extensions.txt"):
        f = open(f"/Users/{cur}/Desktop/{cur}/Extensions.txt", "r")
        s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
        while len(s) != 0:
                s = dict(map(lambda x: x.split('-'), s.split(',')))
                for i in s:
                        extensions_folders[i] = s[i]
                s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                
elif os.path.exists(f"/Users/{cur}/Desktop/{cur}/extensions.txt"):
        f = open(f"/Users/{cur}/Desktop/{cur}/extensions.txt", "r")
        s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
        while len(s) != 0:
                s = dict(map(lambda x: x.split('-'), s.split(',')))
                for i in s:
                        extensions_folders[i] = s[i]
                s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")

elif os.path.exists(f"/Users/{cur}/Desktop/extensions.txt"):
        f = open(f"/Users/{cur}/Desktop/extensions.txt", "r")
        s = f.read().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
        while len(s) != 0:
                s = dict(map(lambda x: x.split('-'), s.split(',')))
                for i in s:
                        extensions_folders[i] = s[i]
                s = f.readline().replace(" ", "").replace('"', "").replace(",", "").replace("\n", ",")
                

for i in set(extensions_folders.values()):
        if os.path.exists(i):
                continue
        else:
                print(i)
                os.makedirs(i)
                        

folder_to_track = f'/Users/{cur}/Desktop'
folder_destination = f'/Users/{cur}/Desktop/{cur}'


try:
    while True:
        time.sleep(1)
        on_modified()
except:
        f = open("cleaner_cash.txt", "w")
        f.write("0")
        f.close()
        try:
                f = open("f'/Users/{cur}/Desktop/{cur}/List_of_directories.txt", "w")
                f.write(list_of_files)
                f.close()
        except:
                pass
