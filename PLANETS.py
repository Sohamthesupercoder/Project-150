from tkinter import *
root = Tk()
root.title("Planet Encyclopedia")
root.geometry("700x700")
root.configure(background = "lightblue")

from PIL import ImageTk , Image

from tkinter import ttk

mercury_img = ImageTk.PhotoImage(Image.open("mercury.jpg"))

earth_img = ImageTk.PhotoImage(Image.open("earth.jpg"))

venus_img = ImageTk.PhotoImage(Image.open("venus.jpg"))


planets = ["Mercury" , "Venus" , "Earth"]


selected = StringVar()


dropdown = ttk.Combobox(root , values = planets , textvariable = selected)
dropdown.place(relx = 0.5 , rely = 0.125 , anchor= CENTER)



label_1 = Label(root , text = "Planet:" , bg = "lightblue")
label_1.place(relx = 0.215 , rely = 0.125 , anchor = CENTER)
Planet_Name_Label = Label(root , text = "" , font = ("courier" , 25 , "bold") , bg = "lightblue")
Planet_Name_Label.place(relx = 0.5 , rely = 0.315 , anchor = CENTER)
Planet_Image_Label = Label(root , bg = "gold2" , highlightthickness = 5 , borderwidth = 2 , relief = SOLID)
Planet_Image_Label.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
Gravity_Radius_Label = Label(root ,font = ("castellar" , 25 , "bold") , bg = "lightblue")
Gravity_Radius_Label.place(relx = 0.5 , rely = 0.75 , anchor = CENTER)
Info_Label = Label(root ,font = ("courier" , 18 , "bold") , bg = "lightblue" , wrap = 450)
Info_Label.place(relx = 0.5 , rely = 0.9 , anchor = CENTER)

def ShowInfo():
    print(selected.get())
    value = selected.get()
    if value == "Mercury":
        Planet_Image_Label["image"] = mercury_img
        Planet_Name_Label["text"] = "Mercury"
        Gravity_Radius_Label["text"] = "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        Info_Label["text"] = "Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"
    elif value == "Venus":
        Planet_Image_Label["image"] = venus_img
        Planet_Name_Label["text"] = "Venus"
        Gravity_Radius_Label["text"] = "Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
        Info_Label["text"] = "Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky."
    elif value == "Earth":
        Planet_Image_Label["image"] = earth_img
        Planet_Name_Label["text"] = "Earth"
        Gravity_Radius_Label["text"] = "Gravity : 9.807 m/s² \n Radius : 6,371 km"
        Info_Label["text"] = "Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."
        
    
        


Show_Button = Button(root , text = "Show Info" , command = ShowInfo)
Show_Button.place(relx = 0.5 , rely = 0.225 , anchor = CENTER)
root.mainloop()