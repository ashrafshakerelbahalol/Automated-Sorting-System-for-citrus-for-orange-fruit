import tkinter as tk
import time
from tkinter import ttk
from tkinter import Toplevel, Canvas
from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *
import matplotlib.pyplot as plt

app = CTk()
app.config ( bg="#5d3891")
set_appearance_mode("DARK")
app.title("Automated Sorting System for citrus")
app.geometry("1000x700")
app.resizable(False, False)
def button_callback():
    # Create a Toplevel window
    new_window = Toplevel(app)
    # Set the window size
    new_window.geometry("300x300")
    # Set the window title
    new_window.title("New Window")
    new_window.mainloop()
def open_image():
    # Create a Toplevel window
    new_window = Toplevel(app)
    # Set the window size
    new_window.geometry("800x600")
    # Set the window title
    new_window.title("New Window")
    Img = Image.open(path)
    my_image2 = CTkImage(light_image=Img, size=(800, 600))
    CTkLabel(new_window, image=my_image2, text="").place(x=0, y=0)
    new_window.mainloop()
def read_img():
    global Img, path
    path = filedialog.askopenfilename(initialdir='/', title='Select the Image',filetypes=(('imagefiles', '.png'), ('imagefiles', '.jpg')))
    Img = Image.open(path)
    my_image2 = CTkImage(light_image= Img, size=(250, 200))
    CTkLabel(frame1, image=my_image2,text="").place(x=0, y=0)


def start_flow():


    global my_list
    my_list = [["N4","premium", 29, 36,70], ["N3","class 1", 57, 66,30], ["N&7","class 3", 80, 90,30], ["NM#9","class 2", 80, 90,30]]
    table1 = ttk.Treeview(app)

    # Define the columns of the table
    table1["columns"] = ("name","class", "size", "area", "blemish area")

    # Format the columns
    table1.column("#0", width=0, stretch=tk.NO)
    table1.column("name", width=50)
    table1.column("class", width=60)
    table1.column("size", width=50, anchor=tk.CENTER)
    table1.column("area", width=50)
    table1.column("blemish area", width=90)

    # Create headings for each column
    table1.heading("name", text="name")
    table1.heading("class", text="class")
    table1.heading("size", text="size")
    table1.heading("area", text="area")
    table1.heading("blemish area", text="blemish area")



    for row in my_list:
        table1.insert("", tk.END, values=(row[0], row[1], row[2], row[3],row[4]))


    # Add color to the rows
    table1.tag_configure("oddrow", background="#f0f0ff")
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
        if row[1]=="class 1":
            class1=class1+1
        if row[1]=="class 2":
            class2=class2+1
        if row[1]=="class 3":
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
      CTkLabel(app, image=my_image3, text="").place(x=240, y=489)
    except Exception as e:
      print(e)

    ################################################


    # Add data to the table

    for row in my_list:
        table2.insert("", tk.END, text=i, values=(row[0], row[1], row[2], row[3],row[4]))
        i = 1 + i
    # Add color to the rows
    table2.tag_configure("oddrow", background="#f0f0ff")
    table2.tag_configure("evenrow", background="#ffffff")
    for i, item in enumerate(table2.get_children()):
        if i % 2 == 0:
            table2.item(item, tags=("evenrow",))
        else:
            table2.item(item, tags=("oddrow",))
    # Pack the table into the window
    table2.place(x=640, y=610)
    #
    values_list = []
    for item in table2.get_children():
        values = []
        for value in table2.item(item)['values']:
            values.append(value)
        values_list.append(values)

    # Print the list of values
    print(values_list)

    premium = 0
    class1 = 0
    class2 = 0
    class3 = 0
    for row in values_list:
        if row[1]=="premium":
            premium=premium+1
        if row[1]=="class 1":
            class1=class1+1
        if row[1]=="class 2":
            class2=class2+1
        if row[1]=="class 3":
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
        CTkLabel(app, image=my_image3, text="").place(x=760, y=489)
    except Exception as e:
        print(e)
##buttons##
button2 = CTkButton(app, text="history", command=button_callback, fg_color="dark orange",text_color="#000000"
                    , bg_color= "#5d3891" ,hover_color="#e8e2e2")
button4 = CTkButton(app, text="detect orange", fg_color="dark orange",text_color="#000000"
                    , bg_color="#5d3891"  ,hover_color="#e8e2e2")
button5 = CTkButton(app, text="classify orange", fg_color="dark orange",text_color="#000000"
                    , bg_color="#5d3891"  ,hover_color="#e8e2e2")
button6 = CTkButton(app, text="sort healthy",  fg_color="dark orange",text_color="#000000"
                   , bg_color="#5d3891"   ,hover_color="#e8e2e2")
button3 = CTkButton(app, text="automatic",command=start_flow,  fg_color="dark orange",text_color="#000000"
                    , bg_color="#5d3891" ,hover_color="#e8e2e2")
button1 = CTkButton(app, text="read image", command=read_img, fg_color="dark orange",text_color="#000000"
                    , bg_color="#5d3891" ,hover_color="#e8e2e2")
button7 = CTkButton(app, text="input image", command=open_image, fg_color="dark orange",text_color="#000000"
                    , bg_color="#5d3891" ,hover_color="#e8e2e2")
button1.place(x=400, y=150)
button2.place(x=400, y=200)
button3.place(x=400, y=250)
button4.place(x=400, y=300)
button5.place(x=400, y=350)
button6.place(x=400, y=400)
button7.place(x=100, y=410)
##frames
frame1 = CTkFrame(app,width=250,height=200,bg_color="#5d3891")
frame1.place(x=50, y=200)
frame2 = CTkFrame(app,width=250,height=200,bg_color="#5d3891")
frame2.place(x=600, y=200)

##ctkimage
#logo
my_image1 = CTkImage(light_image= Image.open("Automated Sorting System for citrus for orange fruit.png"), size=(100, 100))
image_label1 = CTkLabel(app, image=my_image1,text="").place(x=10,y=10)

##labels
label1 = CTkLabel(app, text="input image" ,bg_color="#5d3891",text_color=("#f5f5f5","#f5f5f5"))
label1.place(x=50,y=170)
label2 = CTkLabel(app, text="result image" ,bg_color="#5d3891",text_color=("#f5f5f5","#f5f5f5"))
label2.place(x=600, y=170)
label3 = CTkLabel(app, text="result for current image" ,bg_color="#5d3891",text_color=("#f5f5f5","#f5f5f5"))
label3.place(x=30,y=670)
label4 = CTkLabel(app, text="result for all previous image" ,bg_color="#5d3891",text_color=("#f5f5f5","#f5f5f5"))
label4.place(x=550,y=670)
##the output
# Create a Canvas widget
canvas =Canvas(app, width=1500, height=3 ,bg="#f5f5f5")
canvas.place(x=0,y=600)
# Draw a line on the canvas
line = canvas.create_line(0,380, 1000, 380)

table1 = ttk.Treeview(app)

# Define the columns of the table
table1["columns"] = ("name", "class", "size", "area", "blemish area")

# Format the columns
table1.column("#0", width=0, stretch=tk.NO)
table1.column("name", width=50)
table1.column("class", width=50)
table1.column("size", width=50, anchor=tk.CENTER)
table1.column("area", width=50)
table1.column("blemish area", width=100)

# Create headings for each column
table1.heading("name", text="name")
table1.heading("class", text="class")
table1.heading("size", text="size")
table1.heading("area", text="area")
table1.heading("blemish area", text="blemish area")
table1.place(x=10, y=610)


table2 = ttk.Treeview(app)

# Define the columns of the table
table2["columns"] = ("name", "class", "size", "area", "blemish area")

# Format the columns
table2.column("#0", width=0, stretch=tk.NO)
table2.column("name", width=50)
table2.column("class", width=60)
table2.column("size", width=50, anchor=tk.CENTER)
table2.column("area", width=50)
table2.column("blemish area", width=100)

# Create headings for each column
table2.heading("name", text="name")
table2.heading("class", text="class")
table2.heading("size", text="size")
table2.heading("area", text="area")
table2.heading("blemish area", text="blemish area")
table2.place(x=630, y=610)


app.mainloop()
