import os
from datetime import date
import subprocess
import time
import psutil

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
        print("roooo")
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
    subprocess.run("git add .", shell=True)
    subprocess.run("ls", shell=True)
    today = str(date.today())
    subprocess.run(f'git commit -m "auto commit {today}" ', shell=True)
    subprocess.run("git push", shell=True)
    stop_django_server()

