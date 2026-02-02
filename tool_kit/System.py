from .tools import Tool
import platform
import subprocess
import  os
from datetime import datetime
from typing import List

class System:

    def launch_application(app_name: List[str]):

        current_os = platform.system()
        results = []

        for app in app_name:
            try:
                if current_os == "Windows":
                    os.startfile(app)
                elif current_os == "Darwin":
                    subprocess.Popen(["open", "-a", app])
                else:
                    subprocess.Popen(["xdg-open", app])

                results.append(f"Launched {app}")
            except Exception as e:
                results.append(f"Failed {app}: {e}")

        return "\n".join(results)
    
    def get_current_time(kwargs = None):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")


    def close_application(app_name: List[str]):
        current_os = platform.system()
        results = []

        for app in app_name:
            try:
                if current_os == "Windows":
                    subprocess.call(["taskkill", "/IM", f"{app}.exe", "/F"])
                elif current_os == "Darwin":
                    subprocess.call(["pkill", app])
                else:
                    subprocess.call(["pkill", app])

                results.append(f"Closed {app}")
            except Exception as e:
                results.append(f"Failed {app}: {e}")

        return "\n".join(results)
    
        # 2. Open URL in browser
    def open_url(url: str):
        import webbrowser
        webbrowser.open(url)
        return f"Opened {url}"


    # 3. Create folder
    def create_folder(path: str):
        os.makedirs(path, exist_ok=True)
        return f"Folder created at {path}"


    # 4. Delete file
    def delete_file(path: str):
        if os.path.exists(path):
            os.remove(path)
            return f"Deleted {path}"
        return "File not found"


    # 5. List files in directory
    def list_files(path: str = "."):
        return os.listdir(path)


    # 6. Get system info
    def get_system_info(kwargs=None):
        return {
            "os": platform.system(),
            "version": platform.version(),
            "machine": platform.machine()
        }


    # 7. Shutdown computer
    def shutdown(kwargs=None):
        current_os = platform.system()
        if current_os == "Windows":
            os.system("shutdown /s /t 1")
        else:
            os.system("shutdown now")
        return "Shutting down..."


    # 8. Restart computer
    def restart(kwargs=None):
        current_os = platform.system()
        if current_os == "Windows":
            os.system("shutdown /r /t 1")
        else:
            os.system("reboot")
        return "Restarting..."


    # 9. Get current directory
    def get_current_directory(kwargs=None):
        return os.getcwd()


    # 10. Create file
    def create_file(path: str):
        open(path, "w").close()
        return f"File created at {path}"


    # 11. Read file
    def read_file(path: str):
        with open(path, "r") as f:
            return f.read()


    # 12. Write to file
    def write_file(path: str, content: str):
        with open(path, "w") as f:
            f.write(content)
        return f"Wrote to {path}"

Tool(
    name="System.launch_application",
    description="launch one or more applications",
    args={"app_name": "List[str]"},
    func=System.launch_application
    )

Tool(
    name="System.get_current_time",
    description="Get current local system time and date. Use when user asks for time or today's date.",
    args=None,
    func = System.get_current_time
)

Tool(
    name="System.close_application",
    description="Close one or more applications",
    args={"app_name": "List[str]"},
    func=System.close_application
)

Tool(
    name="System.open_url",
    description="Open a URL in the browser",
    args={"url": "str"},
    func=System.open_url
)

Tool(
    name="System.create_folder",
    description="Create a folder",
    args={"path": "str"},
    func=System.create_folder
)

Tool(
    name="System.delete_file",
    description="Delete a file",
    args={"path": "str"},
    func=System.delete_file
)

Tool(
    name="System.list_files",
    description="List files in directory",
    args={"path": "str"},
    func=System.list_files
)

Tool(
    name="System.get_system_info",
    description="Get OS and machine info",
    args=None,
    func=System.get_system_info
)

Tool(
    name="System.shutdown",
    description="Shutdown computer",
    args=None,
    func=System.shutdown
)

Tool(
    name="System.restart",
    description="Restart computer",
    args=None,
    func=System.restart
)

Tool(
    name="System.get_current_directory",
    description="Get current working directory",
    args=None,
    func=System.get_current_directory
)

Tool(
    name="System.create_file",
    description="Create a file",
    args={"path": "str"},
    func=System.create_file
)

Tool(
    name="System.read_file",
    description="Read file content",
    args={"path": "str"},
    func=System.read_file
)

Tool(
    name="System.write_file",
    description="Write content to file",
    args={"path": "str", "content": "str"},
    func=System.write_file
)
