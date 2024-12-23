import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox
import platform

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
# All Variables Used

first_equation_result_label = None
second_equation_result_label = None
third_equation_result_label = None
gravity_equation_result_label = None
first_equation_calculate_button = None
second_equation_calculate_button = None
third_equation_calculate_button = None
gravity_equation_calculate_button = None
entry_list_1 = []
entry_list_2 = []
entry_list_3 = []
entry_list_4 = []

first_equation_label_widget = None
first_equation_label_widget2 = None
first_equation_label_widget3 = None

second_equation_label_widget = None
second_equation_label_widget2 = None
second_equation_label_widget3 = None

third_equation_label_widget = None
third_equation_label_widget2 = None
third_equation_label_widget3 = None

gravity_equation_label_widget = None
gravity_equation_label_widget2 = None
gravity_equation_label_widget3 = None

entry = None
first_entry_x = 0.64
second_entry_x = 0.77
third_entry_x = 0.9
button_x = 0.5
result_x = 0.8
main_frame = ctk.CTkFrame(root, corner_radius=5, width=1200, height=70,fg_color="#07B6FF")
main_frame.place(relx=0.08, rely=0.13,)
main_frame2 = ctk.CTkFrame(root, corner_radius=5, width=1200, height=70,fg_color="teal")
main_frame2.place(relx=0.08, rely=0.33,)  
main_frame3 = ctk.CTkFrame(root, corner_radius=5, width=1200, height=70,fg_color="#D18A00")
main_frame3.place(relx=0.08, rely=0.53,) 
main_frame4 = ctk.CTkFrame(root, corner_radius=5, width=1200, height=70,fg_color="#2A5900")
main_frame4.place(relx=0.08, rely=0.73,) 
first_equation_selected_value = ctk.StringVar(value="")
second_equation_selected_value = ctk.StringVar(value="")
third_equation_selected_value = ctk.StringVar(value="")
gravity_equation_selected_value = ctk.StringVar(value="")
first_equation_value_options = ["Final Velocity (vf)", "Initial Velocity (vi)", "Acceleration (a)", "Time (t)"]
second_equation_value_options = ["Distance (d)", "Initial Velocity (vi)", "Acceleration (a)", "Time (t)"]
third_equation_value_options = ["Distance (d)", "Initial Velocity (vi)", "Final Velocity (vf)", "Acceleration (a)"]
gravity_equation_value_options = ["Force (f)", "First Mass (m1)", "Second Mass (m2)", "Radius (r)"]

first_equation_dropdown = None
second_equation_dropdown = None
third_equation_dropdown = None
gravity_equation_dropdown = None
    # Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Define the window dimensions (optional; can be the full screen size)
window_width = screen_width
window_height = screen_height

# Calculate position to center the window or slightly offset to the left
x_position = (screen_width - window_width) // 2 -9  # Adjust -50 to move it slightly left
y_position = (screen_height - window_height) // 2 - 50
# All Functions
def check_fields(value):
    text1 = entry_list_1[0].get().strip()
    text2 = entry_list_1[1].get().strip()
    text3 = entry_list_1[2].get().strip()

    if text1 and text2 and text3:
        calculate_first_equation_motion(value)

def check_fields_2(value):
    text1 = entry_list_2[0].get().strip()
    text2 = entry_list_2[1].get().strip()
    text3 = entry_list_2[2].get().strip()

    if text1 and text2 and text3:
        calculate_second_equation_motion(value)

def check_fields_3(value):
    text1 = entry_list_3[0].get().strip()
    text2 = entry_list_3[1].get().strip()
    text3 = entry_list_3[2].get().strip()

    if text1 and text2 and text3:
        calculate_third_equation_motion(value)
        
def check_fields_4(value):
    text1 = entry_list_4[0].get().strip()
    text2 = entry_list_4[1].get().strip()
    text3 = entry_list_4[2].get().strip()

    if text1 and text2 and text3:
        gravity_equation_motion(value)

def calculate_first_equation_motion(value):
    global first_equation_result_label
    global first_equation_selected_value 
    global first_equation_calculate_button  
    try:
        if first_equation_result_label != None:
           first_equation_result_label.destroy()
        # value = first_equation_selected_value.get()

        if value.lower() == "final velocity (vf)".lower():
            vi = float(entry_list_1[0].get())
            a = float(entry_list_1[1].get())
            t = float(entry_list_1[2].get())
            vf = vi + a * t
            first_equation_result_label = ctk.CTkLabel(main_frame, text=f"Final Velocity = {vf:.2f} m/s", font=("Arial", 16, "bold"))
            first_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
            print(f"Result is :{vf:.2f} m/s " )

        elif value.lower() == "initial velocity (vi)".lower():
            vf = float(entry_list_1[0].get())
            a = float(entry_list_1[1].get())
            t = float(entry_list_1[2].get())
            vi = vf - a * t
            first_equation_result_label = ctk.CTkLabel(main_frame, text=f"Initial Velocity = {vi:.2f} m/s", font=("Arial", 16, "bold"))
            first_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "acceleration (a)".lower():
            vi = float(entry_list_1[0].get())
            vf = float(entry_list_1[1].get())
            t = float(entry_list_1[2].get())
            a = (vf - vi) / t
            first_equation_result_label = ctk.CTkLabel(main_frame, text=f"Acceleration = {a:.2f} m/s²", font=("Arial", 16, "bold"))
            first_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "time (t)".lower():
            vi = float(entry_list_1[0].get())
            vf = float(entry_list_1[1].get())
            a = float(entry_list_1[2].get())
            t = (vf - vi) / a
            first_equation_result_label = ctk.CTkLabel(main_frame, text=f"Time = {t:.2f} seconds", font=("Arial", 16, "bold"))
            first_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
        first_equation_calculate_button.destroy()
    except ValueError:
        if first_equation_result_label is not None:
            first_equation_result_label.destroy()
        first_equation_result_label = ctk.CTkLabel(main_frame, text="Error: Please enter valid numbers", font=("Arial", 16, "bold"))
        first_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
 
def calculate_second_equation_motion(value):
    global second_equation_result_label  
    global second_equation_calculate_button
    try:
        second_equation_result_label.destroy()
        # value = second_equation_selected_value.get()
        if value.lower() == "distance (d)".lower():                
            vi = float(entry_list_2[0].get())
            a = float(entry_list_2[1].get())
            t = float(entry_list_2[2].get())
            s = vi * t + 0.5 * a * t ** 2
            second_equation_result_label = ctk.CTkLabel(main_frame2, text=f"Distance = {s:.2f} meter", font=("Arial", 16, "bold"))
            second_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "initial velocity (vi)".lower():
            s = float(entry_list_2[0].get())
            a = float(entry_list_2[1].get())
            t = float(entry_list_2[2].get())
            vi = (s - 0.5 * a * t ** 2) / t
            second_equation_result_label = ctk.CTkLabel(main_frame2, text=f"Initial Velocity = {vi:.2f} m/s", font=("Arial", 16, "bold"))
            second_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "acceleration (a)".lower():
            s = float(entry_list_2[0].get())
            vi = float(entry_list_2[1].get())
            t = float(entry_list_2[2].get())
            a = (2 * (s - vi * t)) / (t ** 2)
            second_equation_result_label =ctk.CTkLabel(main_frame2, text=f"Acceleration = {a:.2f} m/s²", font=("Arial", 16, "bold"))
            second_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "time (t)".lower():
            s = float(entry_list_2[0].get())
            vi = float(entry_list_2[1].get())
            a = float(entry_list_2[2].get())
            t = (math.sqrt(vi ** 2 + 2 * a * s) - vi) / a
            second_equation_result_label = ctk.CTkLabel(main_frame2, text=f"Time = {t:.2f} seconds", font=("Arial", 16, "bold"))
            second_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
        second_equation_calculate_button.destroy()
    except ValueError:
        if second_equation_result_label is not None:
            second_equation_result_label.destroy()
        second_equation_result_label = ctk.CTkLabel(main_frame2, text="Error: Please enter valid numbers", font=("Arial", 16, "bold"))
        second_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
        
def calculate_third_equation_motion(value):
    global third_equation_result_label 
    global third_equation_calculate_button 
    try:
        third_equation_result_label.destroy()
        # value = third_equation_selected_value.get()
        if value.lower() == "distance (d)".lower():                
            vi = float(entry_list_3[0].get())
            vf = float(entry_list_3[1].get())
            a = float(entry_list_3[2].get())
            s = (vf ** 2 - vi ** 2) / (2 * a)
            third_equation_result_label = ctk.CTkLabel(main_frame3, text=f"Distance = {s:.2f} meter", font=("Arial", 16, "bold"))
            third_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "initial velocity (vi)".lower():
            s = float(entry_list_3[0].get())
            vf = float(entry_list_3[1].get())
            a = float(entry_list_3[2].get())
            vi =  math.sqrt(vf ** 2 - 2 * a * s)
            third_equation_result_label = ctk.CTkLabel(main_frame3, text=f"Initial Velocity = {vi:.2f} m/s", font=("Arial", 16, "bold"))
            third_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "acceleration (a)".lower():
            s = float(entry_list_3[0].get())
            vi = float(entry_list_3[1].get())
            vf = float(entry_list_3[2].get())
            a = (vf ** 2 - vi ** 2) / (2 * s)
            third_equation_result_label = ctk.CTkLabel(main_frame3, text=f"Acceleration = {a:.2f} m/s²", font=("Arial", 16, "bold"))
            third_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "final velocity (vf)".lower():
            s = float(entry_list_3[0].get())
            vi = float(entry_list_3[1].get())
            a = float(entry_list_3[2].get())
            vf = math.sqrt(vi ** 2 + 2 * a * s)
            third_equation_result_label = ctk.CTkLabel(main_frame3, text=f"Final Velocity = {vf:.2f} m/s", font=("Arial", 16, "bold"))
            third_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
        third_equation_calculate_button.destroy()
    except ValueError:
        if third_equation_result_label is not None:
            third_equation_result_label.destroy()
        third_equation_result_label = ctk.CTkLabel(main_frame3, text="Error: Please enter valid numbers", font=("Arial", 16, "bold"))
        third_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
   
def gravity_equation_motion(value):
    global gravity_equation_result_label  
    global gravity_equation_calculate_button
    try:
        gravity_equation_result_label.destroy()
        # value = gravity_equation_selected_value.get()
        G = 6.67430e-11
        if value.lower() == "force (f)".lower():                
            m1 = float(entry_list_4[0].get())
            m2 = float(entry_list_4[1].get())
            r = float(entry_list_4[2].get())
            F = G * (m1 * m2) / r ** 2
            gravity_equation_result_label = ctk.CTkLabel(main_frame4, text=f"Force = {F:.2e} N", font=("Arial", 16, "bold"))
            gravity_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "first mass (m1)".lower():
            F = float(entry_list_4[0].get())
            m2 = float(entry_list_4[1].get())
            r = float(entry_list_4[2].get())
            m1 = (F * r ** 2) / (G * m2)
            gravity_equation_result_label = ctk.CTkLabel(main_frame4, text=f"First Mass = {m1:.2f} kg", font=("Arial", 16, "bold"))
            gravity_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "second mass (m2)".lower():
            F = float(entry_list_4[0].get())
            m1 = float(entry_list_4[1].get())
            r = float(entry_list_4[2].get())
            m2 = (F * r ** 2) / (G * m1)
            gravity_equation_result_label = ctk.CTkLabel(main_frame4, text=f"Second Mass = {m2:.2f} kg", font=("Arial", 16, "bold"))
            gravity_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')

        elif value.lower() == "radius (r)".lower():
            F = float(entry_list_4[0].get())
            m1 = float(entry_list_4[1].get())
            m2 = float(entry_list_4[2].get())
            r = math.sqrt(G * (m1 * m2) / F)
            gravity_equation_result_label =ctk.CTkLabel(main_frame4, text=f"Radius = {r:.2f} m", font=("Arial", 16, "bold"))
            gravity_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
        gravity_equation_calculate_button.destroy()
    except ValueError:
        if gravity_equation_result_label is not None:
            gravity_equation_result_label.destroy()
        gravity_equation_result_label = ctk.CTkLabel(main_frame4, text="Error: Please enter valid numbers", font=("Arial", 16, "bold"))
        gravity_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')  
        
def first_equation_label_widget_update_fields(*args):
    global first_equation_result_label
    global gravity_equation_result_label
    global second_equation_result_label
    global third_equation_result_label
    global first_equation_label_widget
    global first_equation_calculate_button
    global second_equation_calculate_button
    global third_equation_calculate_button
    global gravity_equation_calculate_button            
    global main_frame
    
    global entry_list_2
    global entry_list_3
    global entry_list_4
    global entry_list_1
    
    global second_equation_label_widget
    global second_equation_label_widget2
    global second_equation_label_widget3

    global third_equation_label_widget
    global third_equation_label_widget2
    global third_equation_label_widget3
    
    global gravity_equation_label_widget
    global gravity_equation_label_widget2
    global gravity_equation_label_widget3
    
    global second_equation_selected_value
    global third_equation_selected_value
    global gravity_equation_selected_value 
    global first_equation_selected_value 
    # if first_equation_result_label != None:
    #     first_equation_result_label.destroy()
    if third_equation_label_widget != None:    
       third_equation_result_label.destroy()
    if second_equation_result_label != None:
        second_equation_result_label.destroy()
    if gravity_equation_result_label != None:
        gravity_equation_result_label.destroy()
    main_frame.configure(root, corner_radius=5, width=1200, height=150,fg_color="#07B6FF")
    if first_equation_label_widget != None:
      first_equation_label_widget.destroy()
    value = first_equation_selected_value.get()


    if second_equation_label_widget != None:
        second_equation_label_widget.destroy()
        second_equation_label_widget2.destroy()
        second_equation_label_widget3.destroy()
        second_equation_selected_value.set("")
            
    if third_equation_label_widget != None:
        third_equation_label_widget.destroy()
        third_equation_label_widget2.destroy()
        third_equation_label_widget3.destroy()
        third_equation_selected_value.set("")

    if gravity_equation_label_widget != None:
        gravity_equation_label_widget.destroy()
        gravity_equation_label_widget2.destroy()
        gravity_equation_label_widget3.destroy()
        gravity_equation_selected_value.set("")

        
    if entry_list_1 :
        entry_list_1[0].delete(0, ctk.END)
        entry_list_1[1].delete(0, ctk.END)
        entry_list_1[2].delete(0, ctk.END)  
              
    if entry_list_2 :
        entry_list_2[0].destroy()
        entry_list_2[1].destroy()
        entry_list_2[2].destroy()
        entry_list_2 = []

       
        
    if entry_list_3:
        entry_list_3[0].destroy()
        entry_list_3[1].destroy()
        entry_list_3[2].destroy()
        entry_list_3 = []

        
    if entry_list_4:
        entry_list_4[0].destroy()
        entry_list_4[1].destroy()
        entry_list_4[2].destroy()
        entry_list_4 = []

    if first_equation_calculate_button != None:
      first_equation_calculate_button.destroy()
    if second_equation_calculate_button != None :
        second_equation_calculate_button.destroy()
    if third_equation_calculate_button != None:
        third_equation_calculate_button.destroy()
    if gravity_equation_calculate_button != None:
        gravity_equation_calculate_button.destroy()                   
    if value.lower() == "final velocity (vf)".lower():
        display_input_fields(["Initial Velocity (m/s)","Acceleration (m/s²)","Time (s)"],main_frame,value)
    elif value.lower() == "initial velocity (vi)".lower():
            display_input_fields(["Final Velocity (m/s)","Acceleration (m/s²)","Time (s)"],main_frame,value)
    elif value.lower() == "acceleration (a)".lower():
           display_input_fields(["Initial Velocity (m/s)","Final Velocity (m/s)","Time (s)"],main_frame,value)
    elif value.lower() == "time (t)".lower():
        display_input_fields(["Initial Velocity (m/s)","Final Velocity (m/s)","Acceleration (m/s²)"],main_frame,value)

    if third_equation_label_widget != None:    
       third_equation_result_label.destroy()
    if second_equation_result_label != None:
        second_equation_result_label.destroy()
    if gravity_equation_result_label != None:
        gravity_equation_result_label.destroy()
    first_equation_calculate_button = ctk.CTkButton(main_frame, text=f"Calculate {value}",command=lambda: calculate_first_equation_motion(value), corner_radius=20,height=40)
    first_equation_calculate_button.place(relx=button_x, rely=0.8, anchor='center') 
    first_equation_result_label = ctk.CTkLabel(main_frame, text="Result will be displayed here", font=("Arial", 16, "bold"))
    first_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')    
    # second_equation_result_label = ctk.CTkLabel(main_frame2, text="Result will be displayed here", font=("Arial", 16, "bold"))
   
def second_equation_label_widget_update_fields(*args):
    global first_equation_result_label
    global gravity_equation_result_label
    global second_equation_result_label
    global third_equation_result_label
    global second_equation_label_widget
    global second_equation_calculate_button
    global third_equation_calculate_button
    global first_equation_calculate_button
    global gravity_equation_calculate_button
    global main_frame2
    
    global entry_list_2
    global entry_list_3
    global entry_list_4
    global entry_list_1

    global first_equation_label_widget
    global first_equation_label_widget2
    global first_equation_label_widget3

    global third_equation_label_widget
    global third_equation_label_widget2
    global third_equation_label_widget3
    
    global gravity_equation_label_widget
    global gravity_equation_label_widget2
    global gravity_equation_label_widget3
    
    global first_equation_selected_value
    global third_equation_selected_value
    global gravity_equation_selected_value

    main_frame2.configure(root, corner_radius=5, width=1200, height=150,fg_color="teal")    
    if second_equation_label_widget != None:
      second_equation_label_widget.destroy()
        

    value = second_equation_selected_value.get()
    
    if first_equation_result_label != None:
        first_equation_result_label.destroy()
    if third_equation_label_widget != None:    
       third_equation_result_label.destroy()
    # if second_equation_result_label != None:
    #     second_equation_result_label.destroy()
    if gravity_equation_result_label != None:
        gravity_equation_result_label.destroy()
        
    if first_equation_label_widget != None:
        
        first_equation_label_widget.destroy()
        first_equation_label_widget2.destroy()
        first_equation_label_widget3.destroy()
        if first_equation_selected_value != "":
         first_equation_selected_value.set("")
            
    if third_equation_label_widget != None:
        third_equation_label_widget.destroy()
        third_equation_label_widget2.destroy()
        third_equation_label_widget3.destroy()
        third_equation_selected_value.set("")

    if gravity_equation_label_widget != None:
        gravity_equation_label_widget.destroy()
        gravity_equation_label_widget2.destroy()
        gravity_equation_label_widget3.destroy()
        gravity_equation_selected_value.set("")
        
    if entry_list_2 :
        entry_list_2[0].delete(0, ctk.END)
        entry_list_2[1].delete(0, ctk.END)
        entry_list_2[2].delete(0, ctk.END)
        
    if entry_list_1 :
        entry_list_1[0].destroy()
        entry_list_1[1].destroy()
        entry_list_1[2].destroy()
        entry_list_1 = []
        
    if entry_list_3:
        entry_list_3[0].destroy()
        entry_list_3[1].destroy()
        entry_list_3[2].destroy()
        entry_list_3 = []
        
    if entry_list_4:
        entry_list_4[0].destroy()
        entry_list_4[1].destroy()
        entry_list_4[2].destroy()
        entry_list_4 = []      
    if first_equation_calculate_button != None:
      first_equation_calculate_button.destroy()
    if second_equation_calculate_button != None :
        second_equation_calculate_button.destroy()
    if third_equation_calculate_button != None:
        third_equation_calculate_button.destroy()
    if gravity_equation_calculate_button != None:
        gravity_equation_calculate_button.destroy()            
    if value.lower() == "distance (d)".lower():
        display_input_fields_second(["Initial Velocity (m/s)","Acceleration (m/s²)","Time (s)"],main_frame2,value)
    elif value.lower() == "initial velocity (vi)".lower():
            display_input_fields_second(["Total  Distance  (m)","Acceleration (m/s²)","Time (s)"],main_frame2,value)
    elif value.lower() == "acceleration (a)".lower():
           display_input_fields_second(["Total  Distance  (m)","Initial Velocity (m/s)","Time (s)"],main_frame2,value)
    elif value.lower() == "time (t)".lower():
        display_input_fields_second(["Total  Distance  (m)","Initial Velocity (m/s)","Acceleration (m/s²)"],main_frame2,value)
    second_equation_calculate_button = ctk.CTkButton(main_frame2, text=f"Calculate {value}", command=lambda:calculate_second_equation_motion(value),corner_radius=20,height=40 )
    second_equation_calculate_button.place(relx=button_x, rely=0.8, anchor='center')    
    second_equation_result_label =ctk.CTkLabel(main_frame2, text="Result will be displayed here", font=("Arial", 16, "bold"))
    second_equation_result_label.place(relx=result_x, rely=0.8, anchor='center')
    if first_equation_result_label != None:
        first_equation_result_label.destroy()
    if third_equation_label_widget != None:    
       third_equation_result_label.destroy()
    # if second_equation_result_label != None:
    #     second_equation_result_label.destroy()
    if gravity_equation_result_label != None:
        gravity_equation_result_label.destroy()

def third_equation_label_widget_update_fields(*args):
    global first_equation_result_label
    global gravity_equation_result_label
    global second_equation_result_label
    global third_equation_result_label
    global third_equation_label_widget
    global third_equation_calculate_button
    global first_equation_calculate_button
    global second_equation_calculate_button
    global gravity_equation_calculate_button
    global main_frame3
    
    global entry_list_2
    global entry_list_3
    global entry_list_4
    global entry_list_1

    global first_equation_label_widget
    global first_equation_label_widget2
    global first_equation_label_widget3

    global second_equation_label_widget
    global second_equation_label_widget2
    global second_equation_label_widget3
    
    global gravity_equation_label_widget
    global gravity_equation_label_widget2
    global gravity_equation_label_widget3
    
    global first_equation_selected_value
    global second_equation_selected_value
    global gravity_equation_selected_value
    
    main_frame3.configure(root, corner_radius=5, width=1200, height=150,fg_color="#D18A00")    
    if third_equation_label_widget != None:
      third_equation_label_widget.destroy()
    value = third_equation_selected_value.get()
    if first_equation_result_label != None:
        first_equation_result_label.destroy()
    if third_equation_label_widget != None:    
       third_equation_result_label.destroy()
    if second_equation_result_label != None:
        second_equation_result_label.destroy()
    if gravity_equation_result_label != None:
        gravity_equation_result_label.destroy()
  
    if first_equation_label_widget != None:
        first_equation_label_widget.destroy()
        first_equation_label_widget2.destroy()
        first_equation_label_widget3.destroy()
        first_equation_selected_value.set("")
            
    if second_equation_label_widget != None:
        second_equation_label_widget.destroy()
        second_equation_label_widget2.destroy()
        second_equation_label_widget3.destroy()
        second_equation_selected_value.set("")

    if gravity_equation_label_widget != None:
        gravity_equation_label_widget.destroy()
        gravity_equation_label_widget2.destroy()
        gravity_equation_label_widget3.destroy()
        gravity_equation_selected_value.set("")
  
    if entry_list_3 :
        entry_list_3[0].delete(0, ctk.END)
        entry_list_3[1].delete(0, ctk.END)
        entry_list_3[2].delete(0, ctk.END)
        
    if entry_list_2 :
        entry_list_2[0].destroy()
        entry_list_2[1].destroy()
        entry_list_2[2].destroy()
        entry_list_2 = []
        
    if entry_list_1:
        entry_list_1[0].destroy()
        entry_list_1[1].destroy()
        entry_list_1[2].destroy()
        entry_list_1 = []
        
    if entry_list_4:
        entry_list_4[0].destroy()
        entry_list_4[1].destroy()
        entry_list_4[2].destroy()  
        entry_list_4 = [] 
        
    if first_equation_calculate_button != None:
      first_equation_calculate_button.destroy()
    if second_equation_calculate_button != None :
        second_equation_calculate_button.destroy()
    if third_equation_calculate_button != None:
        third_equation_calculate_button.destroy()
    if gravity_equation_calculate_button != None:
        gravity_equation_calculate_button.destroy()              
    if value.lower() == "distance (d)".lower():
        display_input_fields_third(["Initial Velocity (m/s)","Final Velocity (m/s)","Acceleration (m/s²)"],main_frame3,value)
    elif value.lower() == "initial velocity (vi)".lower():
            display_input_fields_third(["Total  Distance  (m)","Final Velocity (m/s)","Acceleration (m/s²)"],main_frame3,value)
    elif value.lower() == "final velocity (vf)".lower():
           display_input_fields_third(["Total  Distance  (m)","Initial Velocity (m/s)","Acceleration (m/s²)"],main_frame3,value)
    elif value.lower() == "acceleration (a)".lower():
        display_input_fields_third(["Total  Distance  (m)","Initial Velocity (m/s)","Final Velocity (m/s)"],main_frame3,value)
    third_equation_calculate_button = ctk.CTkButton(main_frame3, text=f"Calculate {value}", command=lambda:calculate_third_equation_motion(value), corner_radius=20,height=40)
    third_equation_calculate_button.place(relx=button_x, rely=0.8, anchor='center')    
    third_equation_result_label = ctk.CTkLabel(main_frame3, text="Result will be displayed here", font=("Arial", 16, "bold"))
    third_equation_result_label.place(relx=result_x, rely=0.8, anchor='center') 
    if second_equation_result_label != None:
     second_equation_result_label.destroy() 
    if first_equation_result_label != None:
      first_equation_result_label.destroy()
    if gravity_equation_result_label != None:
      gravity_equation_result_label.destroy()      

def gravity_equation_label_widget_update_fields(*args):
    global first_equation_result_label
    global gravity_equation_result_label
    global second_equation_result_label
    global third_equation_result_label
    global gravity_equation_label_widget
    global gravity_equation_calculate_button
    global first_equation_calculate_button
    global second_equation_calculate_button
    global third_equation_calculate_button
    global main_frame4
    global entry_list_2
    global entry_list_3
    global entry_list_4
    global entry_list_1

    global first_equation_label_widget
    global first_equation_label_widget2
    global first_equation_label_widget3

    global second_equation_label_widget
    global second_equation_label_widget2
    global second_equation_label_widget3
    
    global third_equation_label_widget
    global third_equation_label_widget2
    global third_equation_label_widget3
    
    global first_equation_selected_value
    global second_equation_selected_value
    global third_equation_selected_value
    
    main_frame4.configure(root, corner_radius=5, width=1200, height=150,fg_color="#2A5900")     
    if gravity_equation_label_widget != None:
      gravity_equation_label_widget.destroy()
    value = gravity_equation_selected_value.get()
    if first_equation_result_label != None:
        first_equation_result_label.destroy()
    if third_equation_label_widget != None:    
       third_equation_result_label.destroy()
    if second_equation_result_label != None:
        second_equation_result_label.destroy()
    if gravity_equation_result_label != None:
        gravity_equation_result_label.destroy()
         
         
    if first_equation_label_widget != None:
        first_equation_label_widget.destroy()
        first_equation_label_widget2.destroy()
        first_equation_label_widget3.destroy()
        first_equation_selected_value.set("")
            
    if second_equation_label_widget != None:
        second_equation_label_widget.destroy()
        second_equation_label_widget2.destroy()
        second_equation_label_widget3.destroy()
        second_equation_selected_value.set("")

    if third_equation_label_widget != None:
        third_equation_label_widget.destroy()
        third_equation_label_widget2.destroy()
        third_equation_label_widget3.destroy()
        third_equation_selected_value.set("")
        
    if gravity_equation_calculate_button != None:
        gravity_equation_calculate_button.destroy()

    if entry_list_4 :
        entry_list_4[0].delete(0, ctk.END)
        entry_list_4[1].delete(0, ctk.END)
        entry_list_4[2].delete(0, ctk.END)

    if entry_list_2 :
        entry_list_2[0].destroy()
        entry_list_2[1].destroy()
        entry_list_2[2].destroy()
        entry_list_2 = []
        
    if entry_list_3:
        entry_list_3[0].destroy()
        entry_list_3[1].destroy()
        entry_list_3[2].destroy()
        entry_list_3 = []
        
    if entry_list_1:
        entry_list_1[0].destroy()
        entry_list_1[1].destroy()
        entry_list_1[2].destroy()    
        entry_list_1 = []   
        
    if first_equation_calculate_button != None:
      first_equation_calculate_button.destroy()
    if second_equation_calculate_button != None :
        second_equation_calculate_button.destroy()
    if third_equation_calculate_button != None:
        third_equation_calculate_button.destroy()
    if gravity_equation_calculate_button != None:
        gravity_equation_calculate_button.destroy()   
    if value.lower() == "force (f)".lower():
        display_input_fields_gravity(["First Mass (m1)","Second Mass (m2)","Radius (r)"],main_frame4,value)
    elif value.lower() == "first mass (m1)".lower():
            display_input_fields_gravity(["Total  Force  (N)","Second Mass (m2)","Radius (r)"],main_frame4,value)
    elif value.lower() == "second mass (m2)".lower():
           display_input_fields_gravity(["Total  Force  (N)","First   Mass   (m1)","Radius (r)"],main_frame4,value)
    elif value.lower() == "radius (r)".lower():
        display_input_fields_gravity(["Total  Force  (N)","First   Mass   (m1)","Second Mass (m2)"],main_frame4,value)
    gravity_equation_calculate_button = ctk.CTkButton(main_frame4, text=f"Calculate {value}",command=lambda:gravity_equation_motion(value),corner_radius=20,height=40)
    gravity_equation_calculate_button.place(relx=button_x, rely=0.8, anchor='center')    
    gravity_equation_result_label = ctk.CTkLabel(main_frame4, text="Result will be displayed here", font=("Arial", 16, "bold"))
    gravity_equation_result_label.place(relx=result_x, rely=0.8, anchor='center') 
    if second_equation_result_label != None:
       second_equation_result_label.destroy() 
    if first_equation_result_label != None:
       first_equation_result_label.destroy()
    if third_equation_result_label != None:
       third_equation_result_label.destroy()         

def display_input_fields(labels,input_frame,value):
    global entry_list_1
    global label_list_1 
    global first_equation_label_widget
    global first_equation_label_widget2
    global first_equation_label_widget3 
    
    if not entry_list_1:

    
        for i, label in enumerate(labels):
            if i == 0:
                first_equation_label_widget = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                first_equation_label_widget.place(relx=first_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame,fg_color='black',border_width=0,)
                entry.place(relx=first_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields(value))
            if i == 1:
                first_equation_label_widget2 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                first_equation_label_widget2.place(relx=second_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame,fg_color='black',border_width=0,)
                entry.place(relx=second_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields(value))
            if i == 2:
                first_equation_label_widget3 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                first_equation_label_widget3.place(relx=third_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame, border_width=0 ,fg_color='black')
                entry.place(relx=third_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields(value))
            entry_list_1.append(entry)
    else :
        first_equation_label_widget.destroy()
        first_equation_label_widget2.destroy()
        first_equation_label_widget3.destroy()
        for i, label in enumerate(labels):
            if i == 0:
                first_equation_label_widget = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                first_equation_label_widget.place(relx=first_entry_x, rely=0.14, anchor='center')
                
            if i == 1:
                first_equation_label_widget2 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                first_equation_label_widget2.place(relx=second_entry_x, rely=0.14, anchor='center')

            if i == 2:
                first_equation_label_widget3 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                first_equation_label_widget3.place(relx=third_entry_x, rely=0.14, anchor='center')
 
def display_input_fields_second(labels,input_frame,value):
    global entry_list_2
    global second_equation_label_widget
    global second_equation_label_widget2
    global second_equation_label_widget3

    


       
    if not entry_list_2:

    
        for i, label in enumerate(labels):
            if i == 0:
                second_equation_label_widget = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                second_equation_label_widget.place(relx=first_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame,fg_color='black',border_width=0,)
                entry.place(relx=first_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_2(value))
            if i == 1:
                second_equation_label_widget2 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                second_equation_label_widget2.place(relx=second_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame,fg_color='black',border_width=0,)
                entry.place(relx=second_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_2(value))
            if i == 2:
                second_equation_label_widget3 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                second_equation_label_widget3.place(relx=third_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame,fg_color='black',border_width=0,)
                entry.place(relx=third_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_2(value))
            entry_list_2.append(entry)
    else :
        second_equation_label_widget.destroy()
        second_equation_label_widget2.destroy()
        second_equation_label_widget3.destroy()
        for i, label in enumerate(labels):
            if i == 0:
                second_equation_label_widget = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                second_equation_label_widget.place(relx=first_entry_x, rely=0.14, anchor='center')
            if i == 1:
                second_equation_label_widget2 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                second_equation_label_widget2.place(relx=second_entry_x, rely=0.14, anchor='center')
            if i == 2:
                second_equation_label_widget3 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                second_equation_label_widget3.place(relx=third_entry_x, rely=0.14, anchor='center')

def display_input_fields_third(labels,input_frame,value):
    global entry_list_3
    global label_list_3
    global third_equation_label_widget
    global third_equation_label_widget2
    global third_equation_label_widget3
    

    
    if not entry_list_3:

        for i, label in enumerate(labels):
            if i == 0:
                third_equation_label_widget = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                third_equation_label_widget.place(relx=first_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame,fg_color='black',border_width=0)
                entry.place(relx=first_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_3(value))
            if i == 1:
                third_equation_label_widget2 =ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                third_equation_label_widget2.place(relx=second_entry_x, rely=0.14, anchor='center')
                entry =  ctk.CTkEntry(input_frame,fg_color='black',border_width=0)
                entry.place(relx=second_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_3(value))
            if i == 2:
                third_equation_label_widget3 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                third_equation_label_widget3.place(relx=third_entry_x, rely=0.14, anchor='center')
                entry =  ctk.CTkEntry(input_frame,fg_color='black',border_width=0)
                entry.place(relx=third_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_3(value))

            entry_list_3.append(entry)
    else :
        third_equation_label_widget.destroy()
        third_equation_label_widget2.destroy()
        third_equation_label_widget3.destroy()
        for i, label in enumerate(labels):
            if i == 0:
                third_equation_label_widget = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                third_equation_label_widget.place(relx=first_entry_x, rely=0.14, anchor='center')
               
            if i == 1:
                third_equation_label_widget2 =ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                third_equation_label_widget2.place(relx=second_entry_x, rely=0.14, anchor='center')
                
            if i == 2:
                third_equation_label_widget3 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                third_equation_label_widget3.place(relx=third_entry_x, rely=0.14, anchor='center')
   
def display_input_fields_gravity(labels,input_frame,value):
    global entry_list_4
    global gravity_equation_label_widget
    global gravity_equation_label_widget2
    global gravity_equation_label_widget3  
    


    
    if not entry_list_4:
    #     for entry in entry_list_4:
    #         entry.destroy()
    #     entry_list_4 = []  
    # entry_list_4 = []
    
        for i, label in enumerate(labels):
            if i == 0:
                gravity_equation_label_widget = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                gravity_equation_label_widget.place(relx=first_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame,fg_color='black',border_width=0)
                entry.place(relx=first_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_4(value))
            if i == 1:
                gravity_equation_label_widget2 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                gravity_equation_label_widget2.place(relx=second_entry_x, rely=0.14, anchor='center')
                entry =ctk.CTkEntry(input_frame,fg_color='black',border_width=0)
                entry.place(relx=second_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_4(value))
            if i == 2:
                gravity_equation_label_widget3 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                gravity_equation_label_widget3.place(relx=third_entry_x, rely=0.14, anchor='center')
                entry = ctk.CTkEntry(input_frame,fg_color='black',border_width=0)
                entry.place(relx=third_entry_x, rely=0.5, anchor='center')
                entry.bind("<Return>", lambda event, value=value: check_fields_4(value))

            entry_list_4.append(entry)
    else :
        gravity_equation_label_widget.destroy()
        gravity_equation_label_widget2.destroy()
        gravity_equation_label_widget3.destroy()
        for i, label in enumerate(labels):
            if i == 0:
                gravity_equation_label_widget = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                gravity_equation_label_widget.place(relx=first_entry_x, rely=0.14, anchor='center')

            if i == 1:
                gravity_equation_label_widget2 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                gravity_equation_label_widget2.place(relx=second_entry_x, rely=0.14, anchor='center')

            if i == 2:
                gravity_equation_label_widget3 = ctk.CTkLabel(input_frame, text=label, font=("Arial", 14, "bold"))
                gravity_equation_label_widget3.place(relx=third_entry_x, rely=0.14, anchor='center')
        
def display_main_title():
    header_label = ctk.CTkLabel(root, text="GOVT. HIGHER SECONDARY SCHOOL SARAI SALEH HARIPUR", font=("Arial", 40, "bold"))
    header_label.place(relx=0.5, rely=0.05, anchor='center')

def create_formulas_ui(frame,selected_value,value_options,equation_name,equation_y,dropdown_y,label_y,value_dropdown):
    equation1_label = ctk.CTkLabel(frame, text=equation_name, font=("Arial", 25, "bold"))
    equation1_label.place(relx=0.24, rely=equation_y, anchor='center')
    value_label = ctk.CTkLabel(frame, text="Select Value", font=("Arial", 14, "bold"))
    value_label.place(relx=0.5, rely=label_y, anchor='center')
    value_dropdown = ctk.CTkOptionMenu(frame, variable=selected_value, values=value_options ,dropdown_fg_color='black',button_color='black' ,fg_color='black',dropdown_font=("Arial", 14, "bold"))
    value_dropdown.place(relx=0.5, rely=dropdown_y, anchor='center')

def update_formulas_ui(frame,selected_value,value_options,value_dropdown):
    if value_dropdown != None:
       value_dropdown.destroy()
    value_dropdown = ctk.CTkOptionMenu(frame, variable=selected_value, values=value_options ,dropdown_fg_color='black',button_color='black' ,fg_color='black',dropdown_font=("Arial", 14, "bold"))
    value_dropdown.configure(frame)

def terminate_application():
    root.destroy()  # This closes the window
    root.quit()     # This ends the main loop

def confirm_exit():
    # Display the confirmation dialog
    if messagebox.askokcancel("Exit", "Are you sure you want to close?"):
        terminate_application()    

def maximize_window():
    # Check the operating system
    if platform.system() == 'Windows' or platform.system() == 'Linux':
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    elif platform.system() == 'Darwin':  # 'Darwin' refers to macOS
        root.attributes('-fullscreen', True)  # Maximize the window on macOS
# Main Body    
# maximize window
maximize_window()
root.title("Motion Equations and Gravity Calculator")
display_main_title()

# First Equation Of Motion    
create_formulas_ui(main_frame,first_equation_selected_value,first_equation_value_options,"1ST EQUATION OF MOTION",0.5,0.5,0.14,first_equation_dropdown)
first_equation_selected_value.trace("w", first_equation_label_widget_update_fields)
# Second Equation Of Motion 
create_formulas_ui(main_frame2,second_equation_selected_value,second_equation_value_options,"2ND EQUATION OF MOTION",0.5,0.5,0.14,second_equation_dropdown)
second_equation_selected_value.trace("w", second_equation_label_widget_update_fields)
# Third Equation Of Motion 
create_formulas_ui(main_frame3,third_equation_selected_value,third_equation_value_options,"3RD EQUATION OF MOTION",0.5,0.5,0.14,third_equation_dropdown)
third_equation_selected_value.trace("w", third_equation_label_widget_update_fields)
# Gravity Equation  
create_formulas_ui(main_frame4,gravity_equation_selected_value,gravity_equation_value_options,"NEWTON GRAVITATION FORMULA",0.5,0.5,0.14,gravity_equation_dropdown)
gravity_equation_selected_value.trace("w", gravity_equation_label_widget_update_fields)
# Exit Button
exit_button = ctk.CTkButton(root, text=f"Exit", command=confirm_exit, corner_radius=20,height=40,fg_color="red",font=("Arial", 16, "bold"))
exit_button.place(relx=button_x, rely=0.96, anchor='center')
# Developed by Text
developed_by_label = ctk.CTkLabel(root, text=f"Developed by 2nd year Computer Science ", font=("Arial", 16, "bold"))
developed_by_label.place(relx=result_x, rely=0.96, anchor='center') 
# Main Loop
root.mainloop()

