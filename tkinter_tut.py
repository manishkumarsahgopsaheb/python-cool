import tkinter as tk

# creating a window
window = tk.Tk()

# now lets add a widget

# greeting = tk.Label(text="Hello!, this is manish kumar sah")

# The window i have  created this  doesn’t change. i have  just
# created a Label widget, but i haven’t added it to the
# window yet. There are several ways to add widgets to a
# window. Right now, i am going to use the Label widget’s .pack() method:

# greeting.pack()  # so this will add greeting widgets to the window

# ***************working with widgets****************


# Label ----->	A widget used to display text on the screen
# Button ----->	A button that can contain text and can perform an action when clicked
# Entry ----->	A text entry widget that allows only a single line of text
# Text  ------>	A text entry widget that allows multiline text entry
# Frame ---->	A rectangular region used to group related widgets or provide padding between widgets

# Label widgets are used to display text or images
# Label widgets display text with the default system text color and the default text background
# color. these are typically black and white

# we can control the Label text and background colors using the foreground and
# background parameters

# label = tk.Label(text="Hello! Manish",
#                  foreground="white",  # this will set the text color to white
#                  background="black")  # this will set the background color to black

# we can also use color code to put the color
# lets pack this label on window

# label.pack()

# we can also use the short hand for foreground as fg and background as bg

# lets control the width and height of the label

# label = tk.Label(text="Hello! manish",
#                  fg="#ffffff",
#                  bg="#000000",
#                  width="10",
#                  height="10")
# label.pack()

# Tkinter uses text units for width and height measurements of 0 character, instead of
# something like inches, centimeters, or pixels, to ensure consistent behavior
# of the application across platforms.

# *************Button***************

# button = tk.Button(text="click me!",
#                    width="25",
#                    height="5",
#                    fg="blue",
#                    bg="red")
# button.pack()

# ******************getting user input with Entry widgets******************
#
# label = tk.Label(text="Name")
# entry = tk.Entry(text="manish")
# label.pack()
# entry.pack()

# lets use the method of Entry widgets for
#     getting text by .get()
#     deleting text by .delete()
#     inserting text by .insert()

# name = entry.get()
# name = entry.insert(0, "Rohan")

# **************getting multiple user input with text widgets**********

# text_box = tk.Text()
# text_box.pack()

# ****************assigning widgets to Frame with Frame widgets**************

# frame = tk.Frame()
# frame.pack()

# now lets add label into this frame

# label = tk.Label(master=frame, text="Hii This is a label in the frame")
# label.pack()


# To get a feel for how this works, write a script that creates two
# Frame widgets called frame_a and frame_b. In this script, frame_a contains
# a label with the text "I'm in Frame A", and frame_b contains the label
# "I'm in Frame B". Here’s one way to do this:

# frame_a = tk.Frame()
# frame_b = tk.Frame()
#
# label_a = tk.Label(master=frame_a, text="I m in frame A")
# label_a.pack()
#
# label_b = tk.Label(master=frame_b, text="I m in frame B")
# label_b.pack()

# frame_a.pack()
# frame_b.pack()

# if i will reverse the order of packing of frame then their position will also reverse

# frame_b.pack()
# frame_a.pack()

# ******************Adjusting the frame appearance with reliefs******************

# Frame widgets can be configured with a relief attribute that creates a
# border around the frame. You can set relief to be any of the following values:

# tk.FLAT: Has no border effect (the default value).
# tk.SUNKEN: Creates a sunken effect.
# tk.RAISED: Creates a raised effect.
# tk.GROOVE: Creates a grooved border effect.
# tk.RIDGE: Creates a ridged effect.

# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

# **************controlling layout with geometry managers****************

# instead of .pack() we have also two others geometry managers called
# .place() and .grid()
#  lets create three frame and pack them using .pack()

# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack()
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack()

# but problem with this above code is when we maximize the window our frame is not responsive
# so to make it responsive we can use the fill keyword in .pack() to make it responsive


# frame1 = tk.Frame(master=window, height=100, bg="red") # no need to give width because i m going to fill it into x
# # direction
# frame1.pack(fill=tk.X)
#
# frame2 = tk.Frame(master=window, height=50, bg="yellow")
# frame2.pack(fill=tk.X)
#
# frame3 = tk.Frame(master=window, height=25, bg="blue")
# frame3.pack(fill=tk.X)

# now this above code is responsive to x direction
# further we have also tk.Y and tk.BOTH to make it responsive in Y direction and in Both direction respectively

# *************The side keyword argument of .pack() specifies on which side of the window
# the widget should be placed. These are the available options:*********

# tk.TOP
# tk.BOTTOM
# tk.LEFT
# tk.RIGHT

# If you don’t set side, then .pack() will automatically use tk.TOP and place
# new widgets at the top of the window, or at the top-most portion of the
# window that isn’t already occupied by a widget.

# frame1 = tk.Frame(master=window, height=100, width=200, bg="red") # ydi first frame me height ni denge to initially
# jb code run hoga to 0 height pr window dikhega
# frame1.pack(fill=tk.Y, side=tk.LEFT)

# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.Y, side=tk.LEFT)
#
# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.Y, side=tk.LEFT)

# To make the layout truly responsive, you can set an initial size for
# your frames using the width and height attributes. Then, set the
# fill keyword argument of .pack() to tk.BOTH and set the expand
# keyword argument to True:

# frame1 = tk.Frame(master=window, height=100, width=200, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


# ***********The .place() Geometry Manager****************


# You can use .place() to control the precise location that a widget
# should occupy in a window or Frame. You must provide two keyword
# arguments, x and y, which specify the x- and y-coordinates for
# the top-left corner of the widget. Both x and y are measured in pixels,
# not text units.

# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()
#
# label1 = tk.Label(master=frame, text="I m at a position (0, 0)",
#                   bg="red")
# label1.place(x=0, y=0)
#
# label2 = tk.Label(master=frame, text="I m at  (75, 75)",
#                   bg="yellow")
# label2.place(x=75, y=75)

# .place() is not used often. It has two main drawbacks:
#
# Layout can be difficult to manage with .place(). This is especially
# true if your application has lots of widgets.
# Layouts created with .place() are not responsive. They don’t change as
# the window is resized.


# ***************.grid() geometry manager********************


# The geometry manager you’ll likely use most often is .grid(), which
# provides all the power of .pack() in a format that’s easier to
# understand and maintain.
#
# .grid() works by splitting a window or Frame into rows and columns.
# You specify the location of a widget by calling .grid() and passing
# the row and column indices to the row and column keyword arguments,
# respectively. Both row and column indices start at 0, so a row index
# of 1 and a column index of 2 tells .grid() to place a widget in the
# third column of the second row.

# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=f"Row {i}\ncolumn {j}")
#         label.pack()

# padx adds padding in the horizontal direction.
# pady adds padding in the vertical direction.


# padding jb bhi dena ho to padding .grid ya .pack ya .place me hi
# hi dete hai

# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         # we can also apply padding on label
#         label = tk.Label(master=frame, text=f"Row {i}\ncolumn {j}")
#         label.pack(padx=5, pady=5)

# but it is not responsive to make it responsive do this

# The index of the grid column or row that you want to configure (or a list of indices to configure multiple rows or
# columns at the same time) A keyword argument called weight that determines how the column or row should respond to
# window resizing, relative to the other columns and rows A keyword argument called minsize that sets the minimum
# size of the row height or column width in pixels


#  window.columnconfigure(i, weight=1, minsize=75)
#  window.rowconfigure(i, weight=1, minsize=50)

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#
#     for j in range(3):
#         frame = tk.Frame(master=window,
#                          relief=tk.RAISED,
#                          borderwidth=1)
#         frame.grid(row=i, column=j, padx=5, pady=5)
#
#         label = tk.Label(master=frame, text=f"row {i}\ncolumn {j}")
#         label.pack(padx=5, pady=5)


# By default, widgets are centered in their grid cells. For example,
# the following code creates two Label widgets and places them in a grid
# with one column and two rows:

# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)
#
# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0)
#
# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0)

# You can change the location of each label inside of the grid cell using
# the sticky parameter. sticky accepts a string containing one or more
# of the following letters:
#
# "n" or "N" (north) to align to the top-center part of the cell
# "e" or "E" (east) to align to the right-center side of the cell
# "s" or "S" (south) to align to the bottom-center part of the cell
# "w" or "W" (west) to align to the left-center side of the cell

#            North
#              |
#              |
#     West------------East
#              |
#              |
#            South
#

# this will show the label A and B on the Top

# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)
#
# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0, sticky="n")
#
# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0, sticky="n")

# let me the label on the north-east and another one in south-west

# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)
# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0, sticky="ne")
#
# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0, sticky="sw")


#                   another code


# window.rowconfigure(0, minsize=50)
# window.columnconfigure([0, 1, 2, 3], minsize=50)
#
# label1 = tk.Label(text="1", bg="black", fg="white")
# label2 = tk.Label(text="2", bg="black", fg="white")
# label3 = tk.Label(text="3", bg="black", fg="white")
# label4 = tk.Label(text="4", bg="black", fg="white")
#
# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1, sticky="ew")
# label3.grid(row=0, column=2, sticky="ns")
# label4.grid(row=0, column=3, sticky="nsew")

# comparison between .grid() and .pack()

# in case of .grid() 
#
# sticky="ns"	
# sticky="ew"
# sticky="nsew"

# in case of .pack()

# fill=tk.Y
# fill=tk.X
# fill=tk.BOTH

window.mainloop()

