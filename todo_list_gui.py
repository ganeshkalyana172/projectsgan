import json
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

DATA = Path(__file__).with_name("todo_tasks.json")
def load_tasks():
    try:
        result = json.loads(DATA.read_text(encoding="utf-8"))
        return result if isinstance(result, list) else []
    except (OSError, json.JSONDecodeError): return []
def save_tasks():
    try: DATA.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
    except OSError as e: messagebox.showerror("Save error", str(e))
def refresh():
    task_list.delete(0, tk.END)
    for t in tasks: task_list.insert(tk.END, f"{'[✓]' if t['done'] else '[ ]'} {t['text']}")
def add(event=None):
    value = entry.get().strip()
    if not value: messagebox.showinfo("Notice", "Enter a task first."); return
    tasks.append({"text": value, "done": False}); entry.delete(0, tk.END); refresh(); save_tasks()
def selected():
    sel = task_list.curselection()
    if not sel: messagebox.showinfo("Notice", "Select a task first."); return None
    return sel[0]
def toggle():
    i = selected()
    if i is not None: tasks[i]["done"] = not tasks[i]["done"]; refresh(); task_list.selection_set(i); save_tasks()
def delete():
    i = selected()
    if i is not None: tasks.pop(i); refresh(); save_tasks()

root = tk.Tk(); root.title("My To-Do List"); root.geometry("440x500")
tasks = load_tasks()
tk.Label(root, text="MY TO-DO LIST", font=("Arial", 18, "bold")).pack(pady=15)
row = tk.Frame(root); row.pack(fill="x", padx=15)
entry = tk.Entry(row, font=("Arial", 12)); entry.pack(side="left", fill="x", expand=True, ipady=6); entry.bind("<Return>", add)
tk.Button(row, text="Add", command=add).pack(side="left", padx=7)
task_list = tk.Listbox(root, font=("Arial", 12)); task_list.pack(fill="both", expand=True, padx=15, pady=12)
buttons = tk.Frame(root); buttons.pack(pady=8)
tk.Button(buttons, text="Complete / Undo", command=toggle).pack(side="left", padx=4)
tk.Button(buttons, text="Delete", command=delete).pack(side="left", padx=4)
tk.Button(buttons, text="Refresh", command=refresh).pack(side="left", padx=4)
refresh(); root.mainloop()
