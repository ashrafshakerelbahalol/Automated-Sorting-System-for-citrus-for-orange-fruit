import tkinter as tk
import time
from tkinter import ttk
from tkinter import Toplevel, Canvas
from tkinter import *

import cv2
from PIL import Image, ImageTk
from customtkinter import *
import matplotlib.pyplot as plt
from background import background_removel
from detect import detection_oranges
from size import size_oranges
from color import color_oranges
from automatic import automtic_oranges
app = CTk()
app.config ( bg="#fcfefd")
set_appearance_mode("DARK")
app.title("Automated Sorting System for citrus")
app.geometry("1150x700")
app.resizable(False, False)

def HistoryWindow():
    # Create a Toplevel window
    history_window = Toplevel(app)
    # Set the window size
    history_window.geometry("1000x400")
    # Set the window title
    history_window.title("History")
    # Create a canvas widget with a large width and height
    canvas = Canvas(history_window)

    # Create a frame to hold the content of history window
    table_frame = tk.Frame(canvas)
    table_frame.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    hscrollbar = ttk.Scrollbar(history_window, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=hscrollbar.set)
    hscrollbar.pack(side="bottom", fill="x")

    # Pack the canvas widget
    canvas.pack(side="left", fill="x", expand=True)

    # Set the canvas scrolling region to the size of the table frame
    canvas.create_window((0, 0), window=table_frame, anchor="nw")
    table_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    Label(table_frame, text="History").pack()
    table = []
    # Open the file for reading
    with open("table_values.txt", 'r') as f:
        # Read each line in the file

        for line in f:
            # Remove any leading or trailing whitespace from the line
            line = line.strip()
            if line.startswith("C:")or line.startswith("D:")or line.startswith("E:")or line.startswith("F:")\
                    or line.startswith("G:"):
                if table!=[]:
                   table1= ttk.Treeview(table_frame)
                   # Define the columns of the table
                   table1["columns"] = ("name", "class", "size", "area", "color index", "blemish area")

                   # Format the columns
                   table1.column("#0", width=0, stretch=tk.NO)
                   table1.column("name", width=50)
                   table1.column("class", width=60)
                   table1.column("size", width=50, anchor=tk.CENTER)
                   table1.column("area", width=50)
                   table1.column("color index", width=90)
                   table1.column("blemish area", width=90)

                   # Create headings for each column
                   table1.heading("name", text="name")
                   table1.heading("class", text="class")
                   table1.heading("size", text="size")
                   table1.heading("area", text="area")
                   table1.heading("color index", text="color index")
                   table1.heading("blemish area", text="blemish area")
                   table1.place(x=10, y=610)

                   for row in table:
                      table1.insert("", tk.END, values=("", "", row[2], "", row[4],""))
                   table1.pack(side=LEFT)
                   Label(table_frame,text="&&").pack(side=LEFT)
                   # Add color to the rows
                   table1.tag_configure("oddrow", background="#fcfe90")
                   table1.tag_configure("evenrow", background="#ffffff")
                   for i, item in enumerate(table1.get_children()):
                       if i % 2 == 0:
                           table1.item(item, tags=("evenrow",))
                       else:
                           table1.item(item, tags=("oddrow",))
                   table = []
                Imgpath = Image.open(line)
                Imgpath = Imgpath.resize((200, 200))
                my_image2 = ImageTk.PhotoImage(Imgpath)
                label = Label(table_frame, image=my_image2)
                label.image = my_image2

                label.pack(side=LEFT)
            else:
               # Split the line into values using whitespace as a delimiter
               values = line.split()
               # Convert the values to strings using a list comprehension
               row = [str(value) for value in values]
               # Add the row to the table list
               table.append(row)

    table1 = ttk.Treeview(table_frame)
    # Define the columns of the table
    table1["columns"] = ("name", "class", "size", "area", "color index", "blemish area")

    # Format the columns
    table1.column("#0", width=0, stretch=tk.NO)
    table1.column("name", width=50)
    table1.column("class", width=60)
    table1.column("size", width=50, anchor=tk.CENTER)
    table1.column("area", width=50)
    table1.column("color index", width=90)
    table1.column("blemish area", width=90)

    # Create headings for each column
    table1.heading("name", text="name")
    table1.heading("class", text="class")
    table1.heading("size", text="size")
    table1.heading("area", text="area")
    table1.heading("color index", text="color index")
    table1.heading("blemish area", text="blemish area")
    table1.place(x=10, y=610)

    for row in table:
        table1.insert("", tk.END, values=("", "", row[2], "", row[4],""))
    table1.pack(side=LEFT)
    # Add color to the rows
    table1.tag_configure("oddrow", background="#fcfe90")
    table1.tag_configure("evenrow", background="#ffffff")
    for i, item in enumerate(table1.get_children()):
        if i % 2 == 0:
            table1.item(item, tags=("evenrow",))
        else:
            table1.item(item, tags=("oddrow",))
    history_window.mainloop()
def open_image():
    # Create a Toplevel window
    new_window = Toplevel(app)
    # Set the window size
    new_window.geometry("1000x750")
    # Set the window title
    new_window.title("New Window")

    new_window.resizable(False, False)
    Img = Image.open(path)
    my_image2 = CTkImage(light_image=Img,size=(800,600))
    CTkLabel(new_window, image=my_image2, text="").place(x=0, y=0)
    new_window.mainloop()
def read_img():
    global Img, path
    path = filedialog.askopenfilename(initialdir='/', title='Select the Image',filetypes=(('imagefiles', '.png'), ('imagefiles', '.jpg'), ('imagefiles', '.bmp')))
    Img = Image.open(path)
    my_image2 = CTkImage(light_image= Img, size=(350, 300))
    CTkLabel(frame1, image=my_image2,text="").place(x=0, y=0)
    return path

def backgroundRemovel():
    # Perform orange detection
    img = background_removel(path)

    # Save the detection result to a file
    cv2.imwrite("background_removel.jpg", img)
    Img = Image.open("background_removel.jpg")

    # Display the detection result in Tkinter
    my_image3 = CTkImage(light_image=Img, size=(350, 300))
    CTkLabel(frame2, image=my_image3, text="").place(x=0, y=0)
def detectImage():
    # Perform orange detection
    img = detection_oranges(path)
    #ImageTk.PhotoImage(img)
    # Save the detection result to a file
    cv2.imwrite("detection_result.jpg", img)
    Img = Image.open("detection_result.jpg")

    # Display the detection result in Tkinter
    my_image3 = CTkImage(light_image=Img, size=(350, 300))
    CTkLabel(frame2, image=my_image3, text="").place(x=0, y=0)
def colorIndex():
    # Perform orange detection
    img = color_oranges(path)

    # Save the detection result to a file
    cv2.imwrite("color_oranges.jpg", img)
    Img = Image.open("color_oranges.jpg")

    # Display the detection result in Tkinter
    my_image3 = CTkImage(light_image=Img, size=(350, 300))
    CTkLabel(frame2, image=my_image3, text="").place(x=0, y=0)
def sizeOranges():
    # Perform orange detection
    img = size_oranges(path)

    # Save the detection result to a file
    cv2.imwrite("size_oranges.jpg", img)
    Img = Image.open("size_oranges.jpg")

    # Display the detection result in Tkinter
    my_image3 = CTkImage(light_image=Img, size=(350, 300))
    CTkLabel(frame2, image=my_image3, text="").place(x=0, y=0)

def start_flow(path):
    #my_list = [["N4", "premium", 29, 36, 70, 70], ["N3", "class1", 57, 66, 30, 70], ["N&7", "class3", 80, 90, 30, 70],
    #  ["NM#9", "class2", 80, 90, 30, 70], ["NM#9", "class2", 80, 90, 30, 70]]
    sizeList,colorIndexList=automtic_oranges(path)
    my_list = [[0,0,sizeList[i],0, colorIndexList[i]] for i in range(len(sizeList))]
    table1 = ttk.Treeview(app)
    # Open a new file for writing
    with open('table_values.txt', 'a') as f:
        # Write the path to the file
        f.write(str(path) + '\n')
        # Loop through each row in the table
        for row in my_list:
            # Loop through each value in the row
            for value in row:
                # Write the value to the file
                f.write(str(value) + ' ')
            # Write a newline character after each row
            f.write('\n')

    # Define the columns of the table
    table1["columns"] = ("name","class", "size", "area", "color index","blemish area")

    # Format the columns
    table1.column("#0", width=0, stretch=tk.NO)
    table1.column("name", width=50)
    table1.column("class", width=60)
    table1.column("size", width=50, anchor=tk.CENTER)
    table1.column("area", width=50)
    table1.column("color index", width=90)
    table1.column("blemish area", width=90)

    # Create headings for each column
    table1.heading("name", text="name")
    table1.heading("class", text="class")
    table1.heading("size", text="size")
    table1.heading("area", text="area")
    table1.heading("color index", text="color index")
    table1.heading("blemish area", text="blemish area")



    for row in my_list:
        table1.insert("", tk.END, values=("", "", row[2], "",row[4],""))


    # Add color to the rows
    table1.tag_configure("oddrow", background="#fcfe90")
    table1.tag_configure("evenrow", background="#ffffff")
    for i, item in enumerate(table1.get_children()):
        if i % 2 == 0:
            table1.item(item, tags=("evenrow",))
        else:
            table1.item(item, tags=("oddrow",))

    # Pack the table into the window
    table1.place(x=10, y=610)

    ##################################################

    premium = 0
    class1 = 0
    class2 = 0
    class3 = 0
    for row in my_list:
        if row[1]=="premium":
            premium=premium+1
        if row[1]=="class1":
            class1=class1+1
        if row[1]=="class2":
            class2=class2+1
        if row[1]=="class3":
            class3=class3+1
    try:
      # Data for the chart
      labels = ['premium', 'class 1', 'class 2', 'class 3']
      sizes = [premium, class1, class2, class3]

      plt.pie(sizes, labels=labels, labeldistance=1.1, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 18})
      # Add a title
      plt.title('Fruit Distribution', fontsize=20)

      # Save the chart as an image file
      plt.savefig('fruit_distribution2.png')
      plt.close()
      # Define the rectangular region to crop
      my_image3 = CTkImage(light_image=Image.open("fruit_distribution2.png"), size=(290, 180))
      CTkLabel(app, image=my_image3, text="").place(x=310, y=489)
    except Exception as e:
      print(e)

    ################################################
    ################################################

    # Add data to the total results table

    for row in my_list:
        table2.insert ("", tk.END, values=("", "", row[2], "",row[4]))
        i = 1 + i
    # Add color to the rows
    table2.tag_configure("oddrow", background="#fcfe90")
    table2.tag_configure("evenrow", background="#ffffff")
    for i, item in enumerate(table2.get_children()):
        if i % 2 == 0:
            table2.item(item, tags=("evenrow",))
        else:
            table2.item(item, tags=("oddrow",))

    table2.place(x=750, y=610)
    values_list = []
    for item in table2.get_children():
        values = []
        for value in table2.item(item)['values']:
            values.append(value)
        values_list.append(values)

    # Print the list of values
    print(values_list)
    #pie chart for all results
    premium = 0
    class1 = 0
    class2 = 0
    class3 = 0
    for row in values_list:
        if row[1]=="premium":
            premium=premium+1
        if row[1]=="class1":
            class1=class1+1
        if row[1]=="class2":
            class2=class2+1
        if row[1]=="class3":
            class3=class3+1
    try:
        # Data for the chart
        labels = ['premium', 'class 1', 'class 2', 'class 3']
        sizes = [premium, class1, class2, class3]

        plt.pie(sizes, labels=labels, labeldistance=1.1, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 18})
        # Add a title
        plt.title('Fruit Distribution', fontsize=20)

        # Save the chart as an image file
        plt.savefig('fruit_distribution.png')
        plt.close()
        # Define the rectangular region to crop
        my_image3 = CTkImage(light_image=Image.open("fruit_distribution.png"), size=(250, 180))
        CTkLabel(app, image=my_image3, text="").place(x=910, y=489)
    except Exception as e:
        print(e)
##Buttons##
button1 = CTkButton(app, text="read image", command=read_img, fg_color="dark orange",text_color="#000000"
                    , bg_color="#fcfefd" ,hover_color="#e8e2e2")
button2 = CTkButton(app, text="history", command=HistoryWindow, fg_color="dark orange", text_color="#000000"
                    , bg_color= "#fcfefd", hover_color="#e8e2e2")
button3 = CTkButton(app, text="automatic",command=lambda: start_flow(path) ,fg_color="dark orange",text_color="#000000"
                    , bg_color="#fcfefd" ,hover_color="#e8e2e2")
button4 = CTkButton(app, text="detect oranges",command=detectImage, fg_color="dark orange",text_color="#000000"
                    , bg_color="#fcfefd"  ,hover_color="#e8e2e2")
button5 = CTkButton(app, text="background removel",command=backgroundRemovel, fg_color="dark orange",text_color="#000000"
                    , bg_color="#fcfefd"  ,hover_color="#e8e2e2")
button6 = CTkButton(app, text="color index",command=colorIndex , fg_color="dark orange",text_color="#000000"
                   , bg_color="#fcfefd"   ,hover_color="#e8e2e2")
button7 = CTkButton(app, text="size oranges",command=sizeOranges , fg_color="dark orange",text_color="#000000"
                   , bg_color="#fcfefd"   ,hover_color="#e8e2e2")

button1.place(x=500, y=130)
button2.place(x=500, y=180)
button3.place(x=500, y=230)
button4.place(x=500, y=280)
button5.place(x=500, y=330)
button6.place(x=500, y=380)
button7.place(x=500, y=430)
##frames
frame1 = CTkFrame(app,width=350,height=300,bg_color="#fcfefd")
frame1.place(x=30, y=150)
frame2 = CTkFrame(app,width=350,height=300,bg_color="#fcfefd")
frame2.place(x=770, y=150)

##ctkimage
#logo
my_image1 = CTkImage(light_image= Image.open("logo.png"), size=(100,100))
image_label1 = CTkLabel(app, image=my_image1,text="").place(x=5,y=4)

##labels
label1 = CTkLabel(app, text="input image" ,bg_color="#fcfefd",text_color=("#000000","#000000"))
label1.place(x=10,y=120)
label2 = CTkLabel(app, text="result image" ,bg_color="#fcfefd",text_color=("#000000","#000000"))
label2.place(x=750, y=120)
label3 = CTkLabel(app, text="result for current image" ,bg_color="#fcfefd",text_color=("#000000","#000000"))
label3.place(x=30,y=670)
label4 = CTkLabel(app, text="result for all previous images" ,bg_color="#fcfefd",text_color=("#000000","#000000"))
label4.place(x=630,y=670)
##the output
# Create a Canvas widget
canvas =Canvas(app, width=1500, height=3 ,bg="#f5f5f5")
canvas.place(x=0,y=600)
# Draw a line on the canvas
line = canvas.create_line(0,380, 1000, 380)

table1 = ttk.Treeview(app)

# Define the columns of the table
table1["columns"] = ("name", "class", "size", "area", "color index", "blemish area")

# Format the columns
table1.column("#0", width=0, stretch=tk.NO)
table1.column("name", width=50)
table1.column("class", width=60)
table1.column("size", width=50, anchor=tk.CENTER)
table1.column("area", width=50)
table1.column("color index", width=90)
table1.column("blemish area", width=90)

# Create headings for each column
table1.heading("name", text="name")
table1.heading("class", text="class")
table1.heading("size", text="size")
table1.heading("area", text="area")
table1.heading("color index", text="color index")
table1.heading("blemish area", text="blemish area")



table2 = ttk.Treeview(app)

# Define the columns of the table
table2["columns"] = ("name", "class", "size", "area", "color index", "blemish area")

# Format the columns
table2.column("#0", width=0, stretch=tk.NO)
table2.column("name", width=50)
table2.column("class", width=60)
table2.column("size", width=50, anchor=tk.CENTER)
table2.column("area", width=50)
table2.column("color index", width=90)
table2.column("blemish area", width=90)

# Create headings for each column
table2.heading("name", text="name")
table2.heading("class", text="class")
table2.heading("size", text="size")
table2.heading("area", text="area")
table2.heading("color index", text="color index")
table2.heading("blemish area", text="blemish area")



app.mainloop()
