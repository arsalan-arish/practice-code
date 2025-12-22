import tkinter as tk

# ------------------------------- MODEL -------------------------------

class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, text):
        self.tasks.append(text)


# ------------------------------- VIEW --------------------------------

class MainView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.listbox = tk.Listbox(self)
        self.add_btn = tk.Button(self, text="Add Task")

        self.listbox.pack(fill="both", expand=True)
        self.add_btn.pack(pady=5)

    def add_to_list(self, text):
        self.listbox.insert("end", text)



class AddTaskDialog(tk.Toplevel): # Modal Window
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Task")

        self.value = tk.StringVar()

        tk.Label(self, text="Task name:").pack(pady=5)
        self.entry = tk.Entry(self, textvariable=self.value)
        self.entry.pack(padx=10)

        self.ok = tk.Button(self, text="OK")
        self.ok.pack(pady=5)

        self.entry.focus_set()     # keyboard goes here
        self.grab_set()            # modal window


# ------------------------------- CONTROLLER -----------------------------

class App: # controller is a functionality exposing class/object
    def __init__(self, parent):
        self.model = TaskModel()
        self.view = MainView(parent)
        self.view.pack(fill="both", expand=True)

        self.view.add_btn.config(command=self.open_dialog)

    def open_dialog(self):
        dialog = AddTaskDialog(self.view)

        # disable OK if entry empty (variable tracing)
        dialog.ok.config(state="disabled")

        def on_change(*_):
            dialog.ok.config(state="normal" if dialog.value.get().strip() else "disabled")

        dialog.value.trace_add("write", on_change)

        dialog.ok.config(
            command=lambda: self.confirm(dialog)
        )
        root.bind("<Return>", self.confirm(dialog))

    def confirm(self, dialog):
        text = dialog.value.get()
        self.model.add_task(text)
        self.view.add_to_list(text)
        dialog.destroy()


# ---------------- START APP ----------------
root = tk.Tk()
root.title("Task App")
root.geometry("300x300")

app = App(root)

root.mainloop()