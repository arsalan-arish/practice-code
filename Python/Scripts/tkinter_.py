"""
Note:
    tk can be replaced by ttk for Frames and Widgets for OS native styling
    root.quit()	Stops the mainloop	Window stays visible, code after mainloop() runs
    root.destroy()	Destroys all widgets and the window	Closes the window immediately, releases resources

    Tkinter is event-driven, not sequential.

    Only the main thread can touch UI and all related to it. Any other thread should not be assigned such responsibility as it is unsafe

    var.trace_add("write", changed) # This function will trace the variable and and call the function 'changed' when the var is written to  

    Custom widgets are combined existing widgets into one reusable unit

MVC Model of creating tkinter programs

    Model View Control -> Create separate classes for the three and distribute functionality.



Root window (and child windows too using child = tk.TopLevel(root))
Frames inside root 
Widgets inside frames (or root)
Layout systems; pack(), grid(), place() Never mix them in the same parent(Root or the Frame)
Root mainloop (event loop)

Modal Window -->
    win = tk.Toplevel(root)
    win.grab_set()        # makes it modal; enforces input focus, so parent can't be clicked
    root.wait_window(win) # optional: pauses your code until the modal closes
    win.destroy()
    

Focus into entry widget -->
    entry.focus_set() # As soon as the window opens


Keyboard binding to a widget -->
    entry.bind("<Return>", submit)
    Global shortcut:
    root.bind("<Control-s>", save)


Widgets -->
    Label()
    Entry()
    Button()
    Menu()

Events -->
    <Button-1>
    <Key>

Event handling methods -->
    keysym (attribute)

Root window functions -->
    title()
    geometry()
    columnconfigure()
    resizable()
    iconbitmap()
    bind()
    register()
    config()
    after()
    quit()

Tkinter Variables --> (.get() and .set() functions can be used to modify the variables)
    StringVar()
    IntVar()
    BooleanVar()
    DoubleVar()
    
Messagebox -->
    showinfo()
    askyesno()

    

    Parameter 	Description
master	The parent container widget (e.g., the main window or a frame) where the button is placed.
command	A function to be called when the button is clicked. The function name should be provided without parentheses (e.g., command=my_function).
text	The text string displayed on the button.
width	The width of the button in characters (for text) or pixels (for images).
height	The height of the button in text lines (for text) or pixels (for images).
bg or background	The normal background color of the button.
fg or foreground	The normal foreground (text) color of the button.
font	The font used for the button's text.
state	Controls the button's interactivity; can be set to NORMAL (default) or DISABLED to gray it out and make it unresponsive.
image	An image to be displayed on the button, instead of or alongside text.
activebackground	The background color when the mouse cursor is over the button.
bd or borderwidth	The width of the border in pixels (default is 2).
padx, pady	Additional padding inside the button, horizontally and vertically.
relief	Specifies the border appearance (e.g., SUNKEN, RAISED, GROOVE, RIDGE).
"""

# Best tkinter format for non OOP

# Root window configurations and references if configged anywhere else

# Peripheral windows configuration 

# Frames configuration with layout hints like frame1 -> grid(3x3)

# Functions and Variables and Threading

# Widgets

# Event Handling/Binding

# Focus configuration



# Best tkinter format for OOP
# MVC (Model, View, Control) Separate classes for all three. View can have more than one class if there are multiple views