import os
from datetime import date
import subprocess
import time
import psutil
import urllib.request
import os, sys, re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

django_server_process = None


def start_django_log_server():
    global django_server_process
    # Change to the Django app directory
    django_app_dir = os.path.join('src')
    if not os.path.exists(django_app_dir):
        print(f"Error: Django app directory '{django_app_dir}' does not exist.")
        return

    os.chdir(django_app_dir)

    # Run Django log server in a new window
    django_server_process = subprocess.Popen('start cmd /k python manage.py runserver 0.0.0.0:8000', shell=True)
def stop_django_server():
    global django_server_process

    subprocess.Popen.kill(django_server_process)
    if django_server_process:
        print("server stoped")
        django_server_process.terminate()
        time.sleep(1)  # wait for process to terminate
    # Terminate Django server

    # Close the Django log server window
    if django_server_process:
        for proc in psutil.process_iter():
            if proc.name() == "cmd.exe" and "- python manage.py runserver" in " ".join(proc.cmdline()):
                proc.terminate()
    subprocess.run(['taskkill', '/f', '/im', 'python.exe'], shell=True)

if __name__ == "__main__":
    start_django_log_server()


    choice = input("Press Enter to stop the Django server: ")

    def savePage(url, pagepath='page'):
        def savenRename(soup, pagefolder, session, url, tag, inner):
            if not os.path.exists(pagefolder): # create only once
                os.mkdir(pagefolder)
            for res in soup.findAll(tag):   # images, css, etc..
                if res.has_attr(inner): # check inner tag (file object) MUST exists  
                    try:
                        filename, ext = os.path.splitext(os.path.basename(res[inner])) # get name and extension
                        try:
                            filename = re.sub(r'\W+', '', filename) + ext # clean special chars from name
                        except SyntaxWarning:
                            ...
                        fileurl = urljoin(url, res.get(inner))
                        filepath = os.path.join(pagefolder, filename)
                        # rename html ref so can move html and folder of files anywhere
                        res[inner] = os.path.join(os.path.basename(pagefolder), filename)
                        if not os.path.isfile(filepath): # was not downloaded
                            with open(filepath, 'wb') as file:
                                filebin = session.get(fileurl)
                                file.write(filebin.content)
                    except Exception as exc:
                        print(exc, file=sys.stderr)
        session = requests.Session()
        #... whatever other requests config you need here
        response = session.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        pagepath = r"D:\financail\django\Financial-v2\docs" + "\\" + pagepath
        path, _ = os.path.splitext(pagepath)
        pagefolder = r"D:\financail\django\Financial-v2\docs\files" # page contents folder
        # pagefolder = 'files' # page contents folder
        tags_inner = {'img': 'src', 'link': 'href', 'script': 'src'} # tag&inner tags to grab
        for tag, inner in tags_inner.items(): # saves resource files and rename refs
            savenRename(soup, pagefolder, session, url, tag, inner)
        with open(path+'.html', 'wb') as file: # saves modified html doc
            file.write(soup.prettify('utf-8'))

    print("---------------------------------------------------------------------")
    cuts_str = str(input("Enter the cut codes that you have added:"))

    cuts_list = [i.strip() for i in cuts_str.split(',')]

    for cut_code in cuts_list:
        if len(cut_code) == 4:
            savePage(f'http://localhost:8000/cut/{cut_code}/', cut_code)
            print(f"\33[32m[{cut_code}] : download finished.\033[0m ")
        else:
            print(f"\33[33m[{cut_code}] : Invalid code!\033[0m ")

    subprocess.run("git add -A", shell=True)
    subprocess.run("dir", shell=True)
    today = str(date.today())
    subprocess.run(f'git commit -m "auto commit {today}" ', shell=True)
    subprocess.run("git push", shell=True)
    stop_django_server()

