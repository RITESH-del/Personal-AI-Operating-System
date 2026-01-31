import platform
import subprocess
import  os
from datetime import datetime
from typing import List


class Tool:
   # Class-level list to store instances
   _instances = []

   def __init__(self, name, description, args, func):
       self.name = name
       self.description = description
       self.args = args
       self.func = func
       Tool._instances.append(self)


   @classmethod
   def get_all_instances(cls):
        return cls._instances
   


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
    
    def get_current_time():
        now = datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

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


tools = Tool.get_all_instances()
