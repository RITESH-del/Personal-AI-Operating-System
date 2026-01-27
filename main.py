import os
import subprocess
import platform
from app.gui import SearchBar

WHITELIST = ["notepad", "chrome", "calc", "spotify", "microsoft Edge"]

def launch_application(app_name: str):
    current_os = platform.system()

    if app_name.lower() in WHITELIST:

        try:
            if current_os == 'Windows':
                subprocess.Popen(["start", app_name], shell=True)
            elif current_os == 'Darwin':
                subprocess.Popen(["open", "-a", app_name])
            else:
                subprocess.Popen(["xdg-open", app_name])

            return f"Successfully sent launch command for {app_name}."
        except Exception as e:
            return f"Failed to open {app_name}. Error {str(e)}"
    else:
        return f"Permission Denied: That application is not on the approved list."



def main():
    app = SearchBar()
    app.run()
    # launch_application("calc")



if __name__ == "__main__":
    main()


