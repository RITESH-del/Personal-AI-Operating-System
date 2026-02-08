import pyautogui
import time
from typing import List, Dict, Any
from .tools import Tool

class ShortcutTool:
    def __init__(self):
        pyautogui.FAILSAFE = True
        self.default_interval = 0.1

    def press_hotkey(self, keys: str):
        """Presses a combination of keys (e.g. 'ctrl+c')."""
        try:
            key_list = [k.strip().lower() for k in keys.split('+')]
            pyautogui.hotkey(*key_list)
            time.sleep(0.5)
            return f"Pressed {keys}"
        except Exception as e:
            return f"Failed {keys}: {e}"

    def type_text(self, text: str):
        """Types text at cursor."""
        try:
            pyautogui.write(text, interval=self.default_interval)
            return f"Typed: {text}"
        except Exception as e:
            return f"Failed typing: {e}"

    def press_key(self, key: str):
        """Press a single key (e.g. 'enter')."""
        try:
            pyautogui.press(key)
            return f"Pressed {key}"
        except Exception as e:
            return f"Failed key {key}: {e}"

    def wait(self, seconds: float):
        """Wait for system/UI response."""
        time.sleep(seconds)
        return f"Waited {seconds}s"

    def mouse_action(self, action: str, x: int = None, y: int = None):
        """Perform mouse actions: click, double_click, right_click, move."""
        try:
            action = action.lower()
            if action == "move":
                pyautogui.moveTo(x, y)
            elif action == "click":
                pyautogui.click(x, y)
            elif action == "double_click":
                pyautogui.doubleClick(x, y)
            elif action == "right_click":
                pyautogui.rightClick(x, y)
            return f"Mouse {action} performed"
        except Exception as e:
            return f"Mouse failed: {e}"

    def run_sequence(self, actions: List[Dict[str, Any]]):
        """
        Runs a list of actions in sequence.
        Example action: {"type": "hotkey", "val": "win+r"}
        Supported types: hotkey, type, key, wait, mouse
        """
        results = []
        for action in actions:
            t = action.get("type")
            v = action.get("val")
            
            if t == "hotkey":
                results.append(self.press_hotkey(v))
            elif t == "type":
                results.append(self.type_text(v))
            elif t == "key":
                results.append(self.press_key(v))
            elif t == "wait":
                results.append(self.wait(float(v)))
            elif t == "mouse":
                results.append(self.mouse_action(v, action.get("x"), action.get("y")))
            elif t == "open":
                results.append(self.open_desktop_app(v))
            
        return "\n".join(results)

    def open_desktop_app(self, text: str):
        """Shortcut to open an app via search."""
        return self.run_sequence([
            {"type": "hotkey", "val": "win+s"},
            {"type": "wait", "val": 0.5},
            {"type": "type", "val": text},
            {"type": "wait", "val": 0.5},
            {"type": "key", "val": "enter"}
        ])

shortcut = ShortcutTool()

# Registrations
Tool(name="Shortcut.press_hotkey", description="Press key combo.", args={"keys": "str"}, func=shortcut.press_hotkey)
Tool(name="Shortcut.type", description="Type text.", args={"text": "str"}, func=shortcut.type_text)
Tool(name="Shortcut.press_key", description="Press single key.", args={"key": "str"}, func=shortcut.press_key)
Tool(name="Shortcut.wait", description="Wait for N seconds.", args={"seconds": "float"}, func=shortcut.wait)
Tool(name="Shortcut.mouse_action", description="Mouse control: move, click, double_click.", args={"action": "str", "x": "int", "y": "int"}, func=shortcut.mouse_action)
Tool(
    name="Shortcut.run_sequence",
    description="""
Execute multiple keyboard/mouse steps.
Use for actions like press, open, and, search, type, write, then.

actions = [
 {"type":"hotkey|type|key|wait|mouse|open","val":string|number}
]
""",
    args={"actions": "List[Step]"},
    func=shortcut.run_sequence
)

Tool(name="Shortcut.open_desktop_app", description="Search and open an app.", args={"text": "str"}, func=shortcut.open_desktop_app)
