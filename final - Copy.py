from pathlib import Path
from tkinter import *
import customtkinter
import ctypes as ct
import sys

ship = []
total_cost_list = []
nen = []

#DARK TITLE BAR (EXTRA)
def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def display_stat():
    cost_final = total_cost_list[0]
    name1 = nen[0]
    email1 = nen[1]
    number1 = nen[2]
    ship_name = ship[0]
    cursor.execute("INSERT INTO customers (names, emails, numbers, ships, costs) VALUES (?,?,?,?,?)", (name1, email1, number1, ship_name, cost_final))
    connect.commit()
    cursor.execute("SELECT * FROM customers")
    print(cursor.fetchall())

def book_page():
    try:
        window.destroy()
    except:
        window2.destroy()
    #else:

        #window3.destroy()
    finally:
        try:
            window3.destroy()
        except:
            pass
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        window4 = Tk()
        dark_title_bar(window4)

        window4.geometry("1471x740")
        window4.configure(bg = "#FFFFFF")

        canvas4 = Canvas(
            window4,
            bg = "#000000",
            height = 740,
            width = 1471,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        ftable4=Frame(canvas4)
        sbHorizontalScrollBar = Scrollbar(window4)
        sbVerticalScrollBar = Scrollbar(window4)
        def updateScrollRegion():
            canvas4.update_idletasks()
            canvas4.config(scrollregion=ftable4.bbox())

        def createScrollableContainer():
            canvas4.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
            sbHorizontalScrollBar.config(orient=HORIZONTAL, command=canvas4.xview)
            sbVerticalScrollBar.config(orient=VERTICAL, command=canvas4.yview)

            sbHorizontalScrollBar.pack(fill=X, side=BOTTOM, expand=FALSE)
            sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
            canvas4.pack(fill=BOTH, side=LEFT, expand=TRUE)
            canvas4.create_window(0, 0, window=ftable4, anchor=NW)
        canvas4.bind('<Configure>', lambda _: canvas4.config(scrollregion=canvas4.bbox('all')))

        canvas4.place(x = 100, y = 100)
        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas4.create_image(
            0,
            0,
            image=image_image_4,anchor='nw'
        )
        
        
        def update_entry(x):
            aa=''
            places = ['Earth', 'Moon','Mars', 'Jupiter', 'Europa', 'Ganymede', 'Saturn','Titan', 'Uranus']
            aa=places[x]
            return aa
            
        
        '''entry_1 = Entry(
            bd=0,
            bg="#000000",
            highlightthickness=3,
            fg='white',
            font=("Montserrat",20),
        )
        entry_1.place(
            x=533.0,
            y=205.0,
            width=374.0,
            height=46.0
        )
        '''
        def update(x):
            send(update_entry(x))
            
        
        button_1= PhotoImage(file=r".\assets\Earth.png")
        b1=customtkinter.CTkButton(master=window4, image=button_1, text="EARTH", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(0))
        b1_window=canvas4.create_window(420,280, anchor="nw", window=b1)
        
        button_2= PhotoImage(file=r".\assets\Moon.png")
        b2=customtkinter.CTkButton(master=window4, image=button_2, text="MOON", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(1))
        b2_window=canvas4.create_window(570,310, anchor="nw", window=b2)
        
        button_3= PhotoImage(file=r".\assets\Mars.png")
        b3=customtkinter.CTkButton(master=window4, image=button_3, text="MARS", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(2))
        b3_window=canvas4.create_window(710,280, anchor="nw", window=b3)
        
        button_4= PhotoImage(file=r".\assets\Jupiter.png")
        b4=customtkinter.CTkButton(master=window4, image=button_4, text="JUPITER", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(3))
        b4_window=canvas4.create_window(850,280, anchor="nw", window=b4)
        
        button_5= PhotoImage(file=r".\assets\Europa.png")
        b5=customtkinter.CTkButton(master=window4, image=button_5, text="EUROPA", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(4))
        b5_window=canvas4.create_window(290,480, anchor="nw", window=b5)
        
        button_6= PhotoImage(file=r".\assets\Ganymede.png")
        b6=customtkinter.CTkButton(master=window4, image=button_6, text="GANYMEDE", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(5))
        b6_window=canvas4.create_window(440,480, anchor="nw", window=b6)
        
        button_7= PhotoImage(file=r".\assets\Saturn.png")
        b7=customtkinter.CTkButton(master=window4, image=button_7, text="SATURN", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(6))
        b7_window=canvas4.create_window(580,500, anchor="nw", window=b7)
        
        button_8= PhotoImage(file=r".\assets\Titan.png")
        b8=customtkinter.CTkButton(master=window4, image=button_8, text="TITAN", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(7))
        b8_window=canvas4.create_window(800,480, anchor="nw", window=b8)
        
        button_9= PhotoImage(file=r".\assets\Uranus.png")
        b9=customtkinter.CTkButton(master=window4, image=button_9, text="URANUS", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                  hover_color="black",command=lambda: update(8))
        b9_window=canvas4.create_window(950,480, anchor="nw", window=b9)
        
        def send(aa):
            current_destination = aa
            places = ['Earth', 'Moon','Mars', 'Jupiter', 'Europa', 'Ganymede', 'Saturn','Titan', 'Uranus']
            if current_destination not in places:
                label_not = Label(window4, text="THE PLACE YOU ENTERED IS NOT THERE YOU FOOL!").place( 
                x=900.0,
                y=200.0)
            else:
                window4.destroy()
                #starting final destination code here
                OUTPUT_PATH = Path(__file__).parent
                ASSETS_PATH = OUTPUT_PATH / Path("./assets")


                def relative_to_assets(path: str) -> Path:
                    return ASSETS_PATH / Path(path)

                window5 = Tk()
                dark_title_bar(window5)
                window5.geometry("1440x720")
                window5.configure(bg = "#000000")
                canvas5 = Canvas(
                    window5,
                    bg = "#000000",
                    height = 720,
                    width = 1440,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge"
                )
                ftable5=Frame(canvas5)
                sbHorizontalScrollBar = Scrollbar(window5)
                sbVerticalScrollBar = Scrollbar(window5)
                def updateScrollRegion():
                    canvas5.update_idletasks()
                    canvas5.config(scrollregion=ftable5.bbox())

                def createScrollableContainer():
                    canvas5.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
                    sbHorizontalScrollBar.config(orient=HORIZONTAL, command=canvas5.xview)
                    sbVerticalScrollBar.config(orient=VERTICAL, command=canvas5.yview)

                    sbHorizontalScrollBar.pack(fill=X, side=BOTTOM, expand=FALSE)
                    sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
                    canvas5.pack(fill=BOTH, side=LEFT, expand=TRUE)
                    canvas5.create_window(0, 0, window=ftable5, anchor=NW)
                canvas5.bind('<Configure>', lambda _: canvas5.config(scrollregion=canvas5.bbox('all')))

                canvas5.place(x = 0, y = 0)
                image_image_5 = PhotoImage(
                    file=relative_to_assets("image_5.png"))
                image_5 = canvas5.create_image(
                    0,
                    0,
                    image=image_image_5,anchor='nw'
                )
                
                def update_entry2(x):
                    aaa=''
                    places = ['Earth', 'Moon','Mars', 'Jupiter', 'Europa', 'Ganymede', 'Saturn','Titan', 'Uranus']
                    aaa=places[x]
                    return aaa
                
                def update2(x):
                    send2(update_entry2(x))      
                
                button_1= PhotoImage(file=r".\assets\Earth.png")
                b1=customtkinter.CTkButton(master=window5, image=button_1, text='EARTH', width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(0))
                b1_window=canvas5.create_window(420,280, anchor="nw", window=b1)
                
                button_2= PhotoImage(file=r".\assets\Moon.png")
                b2=customtkinter.CTkButton(master=window5, image=button_2, text="MOON", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(1))
                b2_window=canvas5.create_window(570,310, anchor="nw", window=b2)
                
                button_3= PhotoImage(file=r".\assets\Mars.png")
                b3=customtkinter.CTkButton(master=window5, image=button_3, text="MARS", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(2))
                b3_window=canvas5.create_window(710,280, anchor="nw", window=b3)
                
                button_4= PhotoImage(file=r".\assets\Jupiter.png")
                b4=customtkinter.CTkButton(master=window5, image=button_4, text="JUPITER", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(3))
                b4_window=canvas5.create_window(850,280, anchor="nw", window=b4)
                
                button_5= PhotoImage(file=r".\assets\Europa.png")
                b5=customtkinter.CTkButton(master=window5, image=button_5, text="EUROPA", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(4))
                b5_window=canvas5.create_window(290,480, anchor="nw", window=b5)
                
                button_6= PhotoImage(file=r".\assets\Ganymede.png")
                b6=customtkinter.CTkButton(master=window5, image=button_6, text="GANYMEDE", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(5))
                b6_window=canvas5.create_window(440,480, anchor="nw", window=b6)
                
                button_7= PhotoImage(file=r".\assets\Saturn.png")
                b7=customtkinter.CTkButton(master=window5, image=button_7, text="SATURN", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(6))
                b7_window=canvas5.create_window(580,500, anchor="nw", window=b7)
                
                button_8= PhotoImage(file=r".\assets\Titan.png")
                b8=customtkinter.CTkButton(master=window5, image=button_8, text="TITAN", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(7))
                b8_window=canvas5.create_window(800,480, anchor="nw", window=b8)
                
                button_9= PhotoImage(file=r".\assets\Uranus.png")
                b9=customtkinter.CTkButton(master=window5, image=button_9, text="URANUS", width=10,corner_radius=10,bg_color="black",fg_color="black", height=10, compound="top",
                                          hover_color="black",command=lambda: update2(8))
                b9_window=canvas5.create_window(950,480, anchor="nw", window=b9)
                
                def send2(aaa):
                    final_destination=aaa
                    places = ['Earth', 'Moon','Mars', 'Jupiter', 'Europa', 'Ganymede', 'Saturn','Titan', 'Uranus']
                    if final_destination not in places:
                        label_not_2 = Label(window5, text="THE PLACE YOU ENTERED IS NOT THERE YOU FOOL!").place( 
                        x=920.0,
                        y=150.0)
                    elif current_destination==final_destination:
                        label_not_3=Label(window5,text='You Have Selected The Same Destination Again!!',foreground='Red',background='black',font=('Impact',30)).place(x=300.0,y=220.0)
                    else:
                        #starting the ship selection page
                        window5.destroy()
                        from pathlib import Path
                        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

                        OUTPUT_PATH = Path(__file__).parent
                        ASSETS_PATH = OUTPUT_PATH / Path("./assets")

                        def relative_to_assets(path: str) -> Path:
                            return ASSETS_PATH / Path(path)

                        window6 = Tk()
                        dark_title_bar(window6)
                        window6.geometry("1423x566")
                        window6.configure(bg = "#FFFFFF")

                        canvas6 = Canvas(
                            window6,
                            bg = "#FFFFFF",
                            height = 566,
                            width = 1423,
                            bd = 0,
                            highlightthickness = 0,
                            relief = "ridge"
                        )

                        canvas6.place(x = 0, y = 0)
                        image_image_6 = PhotoImage(
                            file=relative_to_assets("image_6.png"))
                        image_6 = canvas6.create_image(
                            711.0,
                            283.0,
                            image=image_image_6
                        )

                        def ship_1():
                            #starting login page 1
                            window6.destroy()
                            ship.append("Millenium Falcon")
                            
                            OUTPUT_PATH = Path(__file__).parent
                            ASSETS_PATH = OUTPUT_PATH / Path("./assets")


                            def relative_to_assets(path: str) -> Path:
                                return ASSETS_PATH / Path(path)


                            window7 = Tk()
                            dark_title_bar(window7)
                            window7.geometry("1190x708")
                            window7.configure(bg = "#FFFFFF")


                            canvas7 = Canvas(
                                window7,
                                bg = "#FFFFFF",
                                height = 708,
                                width = 1190,
                                bd = 0,
                                highlightthickness = 0,
                                relief = "ridge"
                            )

                            canvas7.place(x = 0, y = 0)
                            image_image_7 = PhotoImage(
                                file=relative_to_assets("image_7.png"))
                            image_7 = canvas7.create_image(
                                595.0,
                                354.0,
                                image=image_image_7
                            )

                            entry_image3 = PhotoImage(
                                file=relative_to_assets("entry_3.png"))
                            entry_bg3 = canvas7.create_image(
                                565.0,
                                157.5,
                                image=entry_image3
                            )
                            entry3 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                            )
                            entry3.place(
                                x=399.0,
                                y=134.0,
                                width=332.0,
                                height=45.0
                            )

                            entry_image4 = PhotoImage(
                                file=relative_to_assets("entry_4.png"))
                            entry_bg4 = canvas7.create_image(
                                565.0,
                                250.5,
                                image=entry_image3
                            )
                            entry4 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                            )
                            entry4.place(
                                x=399.0,
                                y=227.0,
                                width=332.0,
                                height=45.0
                            )

                            entry_image5 = PhotoImage(
                                file=relative_to_assets("entry_5.png"))
                            entry_bg5 = canvas7.create_image(
                                562.0,
                                348.0,
                                image=entry_image3
                            )
                            entry5 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                                show='*',
                            )
                            entry5.place(
                                x=393.0,
                                y=323.0,
                                width=338.0,
                                height=48.0
                            )
                            

                            def login_button():
                                special_chars = ['-', '@', '!', '#', '$', '%', '^', '&', "*", '()', "=", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '>', '<', '', '+']
                                special_chars_2=['!','-','#', '$', '%', '^', '&', "*", '()', "=",',', '>', '<','+']
                                special_chars_3=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                                check1 = None
                                check2 = None
                                check3 = None
                                
                                name1 = entry3.get()                                
                                email1 = entry4.get()                               
                                socialsecurity1 = int(entry5.get())
                                nen.append(name1)
                                nen.append(email1)
                                nen.append(socialsecurity1)
                                #Checking for errors in name, email and social security number. Blank fields will also result in an error
                                for i in name1:
                                    if i in special_chars or i in special_chars_2:
                                        check1 = True
                                for j in email1:
                                    if j in special_chars_2:
                                        check2 = True
                                for k in str(socialsecurity1):
                                    if k in special_chars_3 or k in special_chars_2:
                                        check3 = True


                                if check1 == True:
                                    lne = Label(window7,text='Incorrect Name Please Try Again').place(x=750,y=140)
                                elif check2 == True:
                                    label_email_error=Label(window7,text='Incorrect Mail ID Please Try Again').place(x=750,y=200)
                                elif check3 == True:
                                    label_ss_error=Label(window7,text='Incorrect Social Security Number Please Try Again').place(x=750,y=320)
                                elif name1 =='':
                                    label_blank_error=Label(window7,text='Please fill out this field').place(x=750,y=140)
                                elif email1 =='':
                                    label_blank_errorr=Label(window7,text='Please fill out this field').place(x=750,y=200)
                                elif socialsecurity1 == '':
                                    label_blank_errorr=Label(window7,text='Please fill out this field').place(x=750,y=320)
                                else:
                                    window7.destroy()
                                    
                                    #Bill Page Starting from here
                                    
                                    OUTPUT_PATH = Path(__file__).parent
                                    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


                                    def relative_to_assets(path: str) -> Path:
                                        return ASSETS_PATH / Path(path)

                                    global window8
                                    window8 = Tk()
                                    dark_title_bar(window8)
                                    
                                    

                                    window8.geometry("1440x780")
                                    window8.configure(bg = "#000000")
                                    
                                    #setting up the billing system from here onwards
                                    
                                    total_cost=0
                                    #diving costs into two
                                    first_cost=0
                                    second_cost=0
                                    #spaceship cost and destination cost
                                    falcon_cost=5000
                                    
                                    if current_destination == 'Earth':
                                        first_cost=500
                                    elif current_destination == 'Moon':
                                        first_cost=300
                                    elif current_destination == 'Mars':
                                        first_cost=450
                                    elif current_destination == 'Jupiter':
                                        first_cost=600
                                    elif current_destination == 'Europa':
                                        first_cost=700
                                    elif current_destination == 'Ganymede':
                                        first_cost=650
                                    elif current_destination == 'Saturn':
                                        first_cost=700
                                    elif current_destination == 'Titan':
                                        first_cost=750
                                    elif current_destination == 'Uranus':
                                        first_cost=900
                                    
                                    if final_destination == 'Earth':
                                        second_cost=500
                                    elif final_destination == 'Moon':
                                        second_cost=300
                                    elif final_destination == 'Mars':
                                        second_cost=450
                                    elif final_destination == 'Jupiter':
                                        second_cost=600
                                    elif final_destination == 'Europa':
                                        second_cost=700
                                    elif final_destination == 'Ganymede':
                                        second_cost=650
                                    elif final_destination == 'Saturn':
                                        second_cost=700
                                    elif final_destination == 'Titan':
                                        second_cost=750
                                    elif final_destination == 'Uranus':
                                        second_cost=900
                                    
                                    #total cost will be set here   
                                    total_cost= falcon_cost + first_cost + second_cost
                                    total_cost_list.append(total_cost)
                                              


                                    canvas8 = Canvas(
                                        window8,
                                        bg = "#FFFFFF",
                                        height = 780,
                                        width = 1440,
                                        bd = 0,
                                        highlightthickness = 0,
                                        relief = "ridge"
                                    )

                                    canvas8.place(x = 0, y = 0)
                                    image_image_8 = PhotoImage(
                                        file=relative_to_assets("image_8.png"))
                                    image_8 = canvas8.create_image(
                                        720.0,
                                        390.0,
                                        image=image_image_8
                                    )
                                    
                                    
                                    
                                    button5=customtkinter.CTkButton(master=window8 ,text="EXIT",text_font=('Helvetica',10,'bold'),text_color='white',border_width=1,border_color='white',width=110,corner_radius=0,bg_color="black",fg_color="maroon", height=39, compound="right",
                                                                    hover_color="red",command=lambda: window8.destroy())
                                    button5_window=canvas8.create_window(1299,700, anchor="nw", window=button5)
                                    entry_image_10 = PhotoImage(
                                        file=relative_to_assets("entry_6.png"))
                                    entry_bg_10 = canvas8.create_image(
                                        603.0,
                                        439.0,
                                        image=entry_image_10
                                    )
                                    entry_6 = Entry(
                                        bd=0,
                                        bg="#F5F5F6",
                                        highlightthickness=3,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_6.place(
                                        x=403.0,
                                        y=405.0,
                                        width=400.0,
                                        height=66.0
                                    )
                                    #inserting name of passenger
                                   
                                    entry_6.insert(0,name1)
                                    entry_6.config(state='readonly')

                                    entry_image_7 = PhotoImage(
                                        file=relative_to_assets("entry_7.png"))
                                    entry_bg_7 = canvas8.create_image(
                                        675.0,
                                        526.5,
                                        image=entry_image_7
                                    )
                                    entry_7 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_7.place(
                                        x=547.0,
                                        y=507.0,
                                        width=256.0,
                                        height=36.0
                                    )
                                    #inserting current destination
                                    entry_7.insert(0,current_destination)
                                    entry_7.config(state='readonly')

                                    entry_image_8 = PhotoImage(
                                        file=relative_to_assets("entry_8.png"))
                                    entry_bg_8 = canvas8.create_image(
                                        648.5,
                                        579.5,
                                        image=entry_image_8
                                    )
                                    entry_8 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_8.place(
                                        x=494.0,
                                        y=558.0,
                                        width=309.0,
                                        height=41.0
                                    )
                                    #inserting final destination
                                    entry_8.insert(0,final_destination)
                                    entry_8.config(state='readonly')


                                    entry_image_9 = PhotoImage(
                                        file=relative_to_assets("entry_9.png"))
                                    entry_bg_9 = canvas8.create_image(
                                        663.5,
                                        636.0,
                                        image=entry_image_9
                                    )
                                    entry_9 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_9.place(
                                        x=524.0,
                                        y=614.0,
                                        width=279.0,
                                        height=42.0
                                    )
                                    #Inserting Name of the ship
                                    entry_9.insert(0,'Millennium Falcon')
                                    entry_9.config(state='readonly')

                                    entry_image_10 = PhotoImage(
                                        file=relative_to_assets("entry_10.png"))
                                    entry_bg_10 = canvas8.create_image(
                                        654.5,
                                        735.0,
                                        image=entry_image_10
                                    )
                                    entry_10 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_10.place(
                                        x=506.0,
                                        y=711.0,
                                        width=297.0,
                                        height=46.0
                                    )
                                
                                    #Inserting Total Cost 
                                    entry_10.insert(0,total_cost)
                                    entry_10.config(state='readonly')




                                    window8.title('UAC Bill Page')
                                    
                                    window8.mainloop()     
                            button_image_18 = PhotoImage(
                                file=relative_to_assets("button_18.png"))
                            button_18 = Button(
                                image=button_image_18,
                                borderwidth=0,
                                highlightthickness=0,
                                command=login_button,
                                relief="flat"
                            )
                            button_18.place(
                                x=602.0,
                                y=382.0,
                                width=126.0,
                                height=44.0
                            )
                            
                            window7.title('UAC User Login Page')
                            window7.mainloop()

                            
                        def ship_2():
                            window6.destroy()
                            
                            ship.append("Milano")
                            
                            #starting login page 2
                            OUTPUT_PATH = Path(__file__).parent
                            ASSETS_PATH = OUTPUT_PATH / Path("./assets")


                            def relative_to_assets(path: str) -> Path:
                                return ASSETS_PATH / Path(path)


                            window7 = Tk()
                            dark_title_bar(window7)
                            window7.geometry("1190x708")
                            window7.configure(bg = "#FFFFFF")


                            canvas7 = Canvas(
                                window7,
                                bg = "#FFFFFF",
                                height = 708,
                                width = 1190,
                                bd = 0,
                                highlightthickness = 0,
                                relief = "ridge"
                            )

                            canvas7.place(x = 0, y = 0)
                            image_image_7 = PhotoImage(
                                file=relative_to_assets("image_7.png"))
                            image_7 = canvas7.create_image(
                                595.0,
                                354.0,
                                image=image_image_7
                            )

                            entry_image_5 = PhotoImage(
                                file=relative_to_assets("entry_3.png"))
                            entry_bg_5 = canvas7.create_image(
                                565.0,
                                157.5,
                                image=entry_image_5
                            )
                            entry3 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                            )
                            entry3.place(
                                x=399.0,
                                y=134.0,
                                width=332.0,
                                height=45.0
                            )

                            entry_image_4 = PhotoImage(
                                file=relative_to_assets("entry_4.png"))
                            entry_bg_4 = canvas7.create_image(
                                565.0,
                                250.5,
                                image=entry_image_4
                            )
                            entry4 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                            )
                            entry4.place(
                                x=399.0,
                                y=227.0,
                                width=332.0,
                                height=45.0
                            )

                            entry_image_5 = PhotoImage(
                                file=relative_to_assets("entry_5.png"))
                            entry_bg_5 = canvas7.create_image(
                                562.0,
                                348.0,
                                image=entry_image_5
                            )
                            entry5 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                                show='*',
                            )
                            entry5.place(
                                x=393.0,
                                y=323.0,
                                width=338.0,
                                height=48.0
                            )
                            def login_button():
                                special_chars = ['-', '@', '!', '#', '$', '%', '^', '&', "*", '()', "=", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '>', '<', '', '+']
                                special_chars_2=['!','-','#', '$', '%', '^', '&', "*", '()', "=",',', '>', '<','+']
                                special_chars_3=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                                check1 = None
                                check2 = None
                                check3 = None
                                name1 = entry3.get()
                                email1 = entry4.get()
                                socialsecurity1 = entry5.get()
                                nen.append(name1)
                                nen.append(email1)
                                nen.append(socialsecurity1)
                                #Checking for errors in name, email and social security number. Blank fields will also result in an error
                                for i in name1:
                                    if i in special_chars or i in special_chars_2:
                                        check1 = True
                                for j in email1:
                                    if j in special_chars_2:
                                        check2 = True
                                for k in socialsecurity1:
                                    if k in special_chars_3 or k in special_chars_2:
                                        check3 = True

                            


                                if check1 == True:
                                    lne = Label(window7,text='Incorrect Name Please Try Again').place(x=750,y=140)
                                elif check2 == True:
                                    label_email_error=Label(window7,text='Incorrect Mail ID Please Try Again').place(x=750,y=200)
                                elif check3 == True:
                                    label_ss_error=Label(window7,text='Incorrect Social Security Number Please Try Again').place(x=750,y=320)
                                elif name1 =='':
                                    label_blank_error=Label(window7,text='Please fill out this field').place(x=750,y=140)
                                elif email1 =='':
                                    label_blank_errorr=Label(window7,text='Please fill out this field').place(x=750,y=200)
                                elif socialsecurity1 == '':
                                    label_blank_errorr=Label(window7,text='Please fill out this field').place(x=750,y=320)
                                else:
                                    
                                    window7.destroy()
                                    window8 = Tk()
                                    dark_title_bar(window8)
                                    
                                    

                                    window8.geometry("1440x780")
                                    window8.configure(bg = "#FFFFFF")
                                    
                                    #setting up the billing system from here onwards
                                    total_cost=0
                                    #diving costs into two
                                    first_cost=0
                                    second_cost=0
                                    #spaceship cost and destination cost
                                    milano_cost=2500
                                    
                                    
                                   
                                    
                                    if current_destination == 'Earth':
                                        first_cost=400
                                    elif current_destination == 'Moon':
                                        first_cost=200
                                    elif current_destination == 'Mars':
                                        first_cost=350
                                    elif current_destination == 'Jupiter':
                                        first_cost=500
                                    elif current_destination == 'Europa':
                                        first_cost=600
                                    elif current_destination == 'Ganymede':
                                        first_cost=550
                                    elif current_destination == 'Saturn':
                                        first_cost=600
                                    elif current_destination == 'Titan':
                                        first_cost=650
                                    elif current_destination == 'Uranus':
                                        first_cost=800
                                    
                                    if final_destination == 'Earth':
                                        second_cost=400
                                    elif final_destination == 'Moon':
                                        second_cost=200
                                    elif final_destination == 'Mars':
                                        second_cost=350
                                    elif final_destination == 'Jupiter':
                                        second_cost=500
                                    elif final_destination == 'Europa':
                                        second_cost=600
                                    elif final_destination == 'Ganymede':
                                        second_cost=550
                                    elif final_destination == 'Saturn':
                                        second_cost=600
                                    elif final_destination == 'Titan':
                                        second_cost=650
                                    elif final_destination == 'Uranus':
                                        second_cost=800
                                    
                                    #total cost will be set here    
                                    total_cost=milano_cost + first_cost + second_cost
                                    total_cost_list.append(total_cost)
                                    canvas8 = Canvas(
                                        window8,
                                        bg = "#FFFFFF",
                                        height = 780,
                                        width = 1440,
                                        bd = 0,
                                        highlightthickness = 0,
                                        relief = "ridge"
                                    )

                                    canvas8.place(x = 0, y = 0)
                                    image_image_8 = PhotoImage(
                                        file=relative_to_assets("image_8.png"))
                                    image_8 = canvas8.create_image(
                                        720.0,
                                        390.0,
                                        image=image_image_8
                                    )
                                    
                                   
                                    
                                    button5=customtkinter.CTkButton(master=window8 ,text="EXIT",text_font=('Helvetica',10,'bold'),text_color='white',border_width=1,border_color='white',width=110,corner_radius=0,bg_color="black",fg_color="maroon", height=39, compound="right",
                                                                    hover_color="red",command=lambda: window8.destroy())
                                    button5_window=canvas8.create_window(1299,700, anchor="nw", window=button5)
                                    
                                    entry_image_10 = PhotoImage(
                                        file=relative_to_assets("entry_6.png"))
                                    entry_bg_10 = canvas8.create_image(
                                        603.0,
                                        439.0,
                                        image=entry_image_10
                                    )
                                    entry_6 = Entry(
                                        bd=0,
                                        bg="#F5F5F6",
                                        highlightthickness=3,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_6.place(
                                        x=403.0,
                                        y=405.0,
                                        width=400.0,
                                        height=66.0
                                    )
                                    #inserting name of passenger
                                   
                                    entry_6.insert(0,name1)
                                    entry_6.config(state='readonly')

                                    entry_image_7 = PhotoImage(
                                        file=relative_to_assets("entry_7.png"))
                                    entry_bg_7 = canvas8.create_image(
                                        675.0,
                                        526.5,
                                        image=entry_image_7
                                    )
                                    entry_7 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_7.place(
                                        x=547.0,
                                        y=507.0,
                                        width=256.0,
                                        height=36.0
                                    )
                                    #inserting current destination
                                    entry_7.insert(0,current_destination)
                                    entry_7.config(state='readonly')

                                    entry_image_8 = PhotoImage(
                                        file=relative_to_assets("entry_8.png"))
                                    entry_bg_8 = canvas8.create_image(
                                        648.5,
                                        579.5,
                                        image=entry_image_8
                                    )
                                    entry_8 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_8.place(
                                        x=494.0,
                                        y=558.0,
                                        width=309.0,
                                        height=41.0
                                    )
                                    #inserting final destination
                                    entry_8.insert(0,final_destination)
                                    entry_8.config(state='readonly')


                                    entry_image_9 = PhotoImage(
                                        file=relative_to_assets("entry_9.png"))
                                    entry_bg_9 = canvas8.create_image(
                                        663.5,
                                        636.0,
                                        image=entry_image_9
                                    )
                                    entry_9 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_9.place(
                                        x=524.0,
                                        y=614.0,
                                        width=279.0,
                                        height=42.0
                                    )
                                    #Inserting Name of the ship
                                    entry_9.insert(0,'Milano')
                                    entry_9.config(state='readonly')

                                    entry_image_10 = PhotoImage(
                                        file=relative_to_assets("entry_10.png"))
                                    entry_bg_10 = canvas8.create_image(
                                        654.5,
                                        735.0,
                                        image=entry_image_10
                                    )
                                    entry_10 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_10.place(
                                        x=506.0,
                                        y=711.0,
                                        width=297.0,
                                        height=46.0
                                    )
            
                                    
                                    #Inserting Total Cost 
                                    entry_10.insert(0,total_cost)
                                    entry_10.config(state='readonly')


                                    window8.title('UAC Bill Page')
                                    
                                    window8.mainloop()

                            button_image_18 = PhotoImage(
                                file=relative_to_assets("button_18.png"))
                            button_18 = Button(
                                image=button_image_18,
                                borderwidth=0,
                                highlightthickness=0,
                                command=login_button,
                                relief="flat"
                            )
                            button_18.place(
                                x=602.0,
                                y=382.0,
                                width=126.0,
                                height=44.0
                            )
                            
                            window7.title('UAC User Login Page')
                            window7.mainloop()
                            
                        def ship_3():
                            window6.destroy()
                            ship.append("Enterprise")
                            
                            OUTPUT_PATH = Path(__file__).parent
                            ASSETS_PATH = OUTPUT_PATH / Path("./assets")
                            def relative_to_assets(path: str) -> Path:
                                return ASSETS_PATH / Path(path)
                            window7 = Tk()
                            dark_title_bar(window7)

                            window7.geometry("1190x708")
                            window7.configure(bg = "#FFFFFF")


                            canvas7 = Canvas(
                                window7,
                                bg = "#FFFFFF",
                                height = 708,
                                width = 1190,
                                bd = 0,
                                highlightthickness = 0,
                                relief = "ridge"
                            )

                            canvas7.place(x = 0, y = 0)
                            image_image_7 = PhotoImage(
                                file=relative_to_assets("image_7.png"))
                            image_7 = canvas7.create_image(
                                595.0,
                                354.0,
                                image=image_image_7
                            )

                            entry_image_5 = PhotoImage(
                                file=relative_to_assets("entry_3.png"))
                            entry_bg_5 = canvas7.create_image(
                                565.0,
                                157.5,
                                image=entry_image_5
                            )
                            entry3 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                            )
                            entry3.place(
                                x=399.0,
                                y=134.0,
                                width=332.0,
                                height=45.0
                            )

                            entry_image_4 = PhotoImage(
                                file=relative_to_assets("entry_4.png"))
                            entry_bg_4 = canvas7.create_image(
                                565.0,
                                250.5,
                                image=entry_image_4
                            )
                            entry4 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                            )
                            entry4.place(
                                x=399.0,
                                y=227.0,
                                width=332.0,
                                height=45.0
                            )

                            entry_image_5 = PhotoImage(
                                file=relative_to_assets("entry_5.png"))
                            entry_bg_5 = canvas7.create_image(
                                562.0,
                                348.0,
                                image=entry_image_5
                            )
                            entry5 = Entry(
                                bd=0,
                                bg="#000000",
                                highlightthickness=3,
                                fg='white',
                                font=("Montserrat",20),
                                show='*',
                            )
                            entry5.place(
                                x=393.0,
                                y=323.0,
                                width=338.0,
                                height=48.0
                            )
                            def login_button():
                                special_chars = ['-', '@', '!', '#', '$', '%', '^', '&', "*", '()', "=", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '>', '<', '', '+']
                                special_chars_2=['!','-','#', '$', '%', '^', '&', "*", '()', "=",',', '>', '<','+']
                                special_chars_3=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                                check1 = None
                                check2 = None
                                check3 = None
                                name1 = entry3.get()
                                email1 = entry4.get()
                                socialsecurity1 = entry5.get()
                                nen.append(name1)
                                nen.append(email1)
                                nen.append(socialsecurity1)
                                #Checking for errors in name, email and social security number. Blank fields will also result in an error
                                for i in name1:
                                    if i in special_chars or i in special_chars_2:
                                        check1 = True
                                for j in email1:
                                    if j in special_chars_2:
                                        check2 = True
                                for k in socialsecurity1:
                                    if k in special_chars_3 or k in special_chars_2:
                                        check3 = True

                                if check1 == True:
                                    lne = Label(window7,text='Incorrect Name Please Try Again').place(x=750,y=140)
                                elif check2 == True:
                                    label_email_error=Label(window7,text='Incorrect Mail ID Please Try Again').place(x=750,y=200)
                                elif check3 == True:
                                    label_ss_error=Label(window7,text='Incorrect Social Security Number Please Try Again').place(x=750,y=320)
                                elif name1 =='':
                                    label_blank_error=Label(window7,text='Please fill out this field').place(x=750,y=140)
                                elif email1 =='':
                                    label_blank_errorr=Label(window7,text='Please fill out this field').place(x=750,y=200)
                                elif socialsecurity1 == '':
                                    label_blank_errorr=Label(window7,text='Please fill out this field').place(x=750,y=320)
                                else:
                                    window7.destroy()
                                    window8 = Tk()
                                    dark_title_bar(window8)
                                    

                                    window8.geometry("1440x780")
                                    window8.configure(bg = "#FFFFFF")
                                    
                                    #setting up the billing system from here onwards
                                    total_cost=0
                                    #diving costs into two
                                    first_cost=0
                                    second_cost=0
                                    #spaceship cost and destination cost
                                    enterprise_cost=1000
                                    Earth_cost=300
                                    Moon_cost=100
                                    Mars_cost=250
                                    Jupiter_cost=400
                                    Europa_cost=500
                                    Ganymede_cost=450
                                    Saturn_cost=500
                                    Titan_cost=550
                                    Uranus_cost=700
                                    
                                    if current_destination == 'Earth':
                                        first_cost=300
                                    elif current_destination == 'Moon':
                                        first_cost=100
                                    elif current_destination == 'Mars':
                                        first_cost=250
                                    elif current_destination == 'Jupiter':
                                        first_cost=400
                                    elif current_destination == 'Europa':
                                        first_cost=500
                                    elif current_destination == 'Ganymede':
                                        first_cost=450
                                    elif current_destination == 'Saturn':
                                        first_cost=500
                                    elif current_destination == 'Titan':
                                        first_cost=550
                                    elif current_destination == 'Uranus':
                                        first_cost=700
                                    
                                    if final_destination == 'Earth':
                                        second_cost=300
                                    elif final_destination == 'Moon':
                                        second_cost=100
                                    elif final_destination == 'Mars':
                                        second_cost=250
                                    elif final_destination == 'Jupiter':
                                        second_cost=400
                                    elif final_destination == 'Europa':
                                        second_cost=500
                                    elif final_destination == 'Ganymede':
                                        second_cost=450
                                    elif final_destination == 'Saturn':
                                        second_cost=500
                                    elif final_destination == 'Titan':
                                        second_cost=450
                                    elif final_destination == 'Uranus':
                                        second_cost=700
                                    
                                    #total cost will be set here    
                                    total_cost=enterprise_cost + first_cost + second_cost
                                    total_cost_list.append(total_cost) 
                                    canvas8 = Canvas(
                                        window8,
                                        bg = "#FFFFFF",
                                        height = 780,
                                        width = 1440,
                                        bd = 0,
                                        highlightthickness = 0,
                                        relief = "ridge"
                                    )

                                    canvas8.place(x = 0, y = 0)
                                    image_image_8 = PhotoImage(
                                        file=relative_to_assets("image_8.png"))
                                    image_8 = canvas8.create_image(
                                        720.0,
                                        390.0,
                                        image=image_image_8
                                    )
                                    

                                    
                                    button5=customtkinter.CTkButton(master=window8 ,text="EXIT",text_font=('Helvetica',10,'bold'),text_color='white',border_width=1,border_color='white',width=110,corner_radius=0,bg_color="black",fg_color="maroon", height=39, compound="right",
                                                                    hover_color="red",command=lambda: window8.destroy())
                                    button5_window=canvas8.create_window(1299,700, anchor="nw", window=button5)

                                    entry_image_10 = PhotoImage(
                                        file=relative_to_assets("entry_6.png"))
                                    entry_bg_10 = canvas8.create_image(
                                        603.0,
                                        439.0,
                                        image=entry_image_10
                                    )
                                    entry_6 = Entry(
                                        bd=0,
                                        bg="#F5F5F6",
                                        highlightthickness=3,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_6.place(
                                        x=403.0,
                                        y=405.0
                                    )
                                    #inserting name of passenger
                                   
                                    entry_6.insert(0,name1)
                                    entry_6.config(state='readonly')

                                    entry_image_7 = PhotoImage(
                                        file=relative_to_assets("entry_7.png"))
                                    entry_bg_7 = canvas8.create_image(
                                        675.0,
                                        526.5,
                                        image=entry_image_7
                                    )
                                    entry_7 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_7.place(
                                        x=547.0,
                                        y=507.0
                                    )
                                    #inserting current destination
                                    entry_7.insert(0,current_destination)
                                    entry_7.config(state='readonly')

                                    entry_image_8 = PhotoImage(
                                        file=relative_to_assets("entry_8.png"))
                                    entry_bg_8 = canvas8.create_image(
                                        648.5,
                                        579.5,
                                        image=entry_image_8
                                    )
                                    entry_8 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_8.place(
                                        x=494.0,
                                        y=558.0,
                                        width=309.0,
                                        height=41.0
                                    )
                                    #inserting final destination
                                    entry_8.insert(0,final_destination)
                                    entry_8.config(state='readonly')


                                    entry_image_9 = PhotoImage(
                                        file=relative_to_assets("entry_9.png"))
                                    entry_bg_9 = canvas8.create_image(
                                        663.5,
                                        636.0,
                                        image=entry_image_9
                                    )
                                    entry_9 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_9.place(
                                        x=524.0,
                                        y=614.0
                                    )
                                    #Inserting Name of the ship
                                    entry_9.insert(0,'Enterprise')
                                    entry_9.config(state='readonly')

                                    entry_image_10 = PhotoImage(
                                        file=relative_to_assets("entry_10.png"))
                                    entry_bg_10 = canvas8.create_image(
                                        654.5,
                                        735.0,
                                        image=entry_image_10
                                    )
                                    entry_10 = Entry(
                                        bd=0,
                                        bg="#000000",
                                        highlightthickness=2,
                                        fg='black',
                                        font=("Montserrat",20),
                                    )
                                    entry_10.place(
                                        x=506.0,
                                        y=711.0
                                    )
                                    #Inserting Total Cost 
                                    entry_10.insert(0,total_cost)
                                    entry_10.config(state='readonly')
                                    window8.title('UAC Bill Page')
                                    
                                    window8.mainloop()

                            button_image_18 = PhotoImage(
                                file=relative_to_assets("button_18.png"))
                            button_18 = Button(
                                image=button_image_18,
                                borderwidth=0,
                                highlightthickness=0,
                                command=login_button,
                                relief="flat"
                            )
                            button_18.place(
                                x=602.0,
                                y=382.0,
                                width=126.0,
                                height=44.0
                            )
                            
                            window7.title('UAC User Login Page')
                            window7.mainloop()    
                            


                        button_image_15 = PhotoImage(
                            file=relative_to_assets("button_15.png"))
                        button_15 = Button(
                            image=button_image_15,
                            borderwidth=0,
                            highlightthickness=0,
                            command=ship_1,
                            relief="flat"
                        )
                        button_15.place(
                            x=27.0,
                            y=474.0,
                            width=420.0,
                            height=76.0
                        )

                        button_image_16 = PhotoImage(
                            file=relative_to_assets("button_16.png"))
                        button_16 = Button(
                            image=button_image_16,
                            borderwidth=0,
                            highlightthickness=0,
                            command=ship_2,
                            relief="flat"
                        )
                        button_16.place(
                            x=501.0,
                            y=474.0,
                            width=420.0,
                            height=76.0
                        )

                        button_image_17 = PhotoImage(
                            file=relative_to_assets("button_17.png"))
                        button_17 = Button(
                            image=button_image_17,
                            borderwidth=0,
                            highlightthickness=0,
                            command=ship_3,
                            relief="flat"
                        )
                        button_17.place(
                            x=986.0,
                            y=474.0,
                            width=420.0,
                            height=76.0
                        )
                        
                        window6.title('UAC Ship Selection Process')
                        window6.mainloop()


                        
                        



                '''button_image_14 = PhotoImage(
                    file=relative_to_assets("button_14.png"))
                button_14 = Button(
                    image=button_image_14,
                    borderwidth=0,
                    highlightthickness=0,
                    command=send2,
                    relief="flat"
                )
                button_14.place(
                    x=914.0,
                    y=193.99998474121094,
                    width=98.0,
                    height=46.0
                )'''
                createScrollableContainer()
                window5.title('UAC Final Destination Page')
               
                window5.mainloop()

                
        
        '''button_image_13=PhotoImage(file=relative_to_assets("button_13.png"))
        button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=send,
            relief="flat"
        )
        button_13.place(
            x=914.0,
            y=220.0,
            width=89.0,
            height=33.0
        )'''



        createScrollableContainer()
        window4.title('UAC Current Destination Page')
        window4.mainloop()
        

   
    

def home_page():
    try:
        window2.destroy()
    except:
        window3.destroy()
    window.__init__()
    window.geometry("1471x720")
    dark_title_bar(window)

    window.configure(bg = "#FFFFFF")

    canvas_2 = Canvas(window,bg = "#FFFFFF",height = 653,width = 1471,bd = 0,highlightthickness = 0,relief = "ridge")

    ftable=Frame(canvas_2)

    sbHorizontalScrollBar = Scrollbar(window)

    sbVerticalScrollBar = Scrollbar(window)
    def updateScrollRegion():
        canvas_2.update_idletasks()
        canvas_2.config(scrollregion=ftable.bbox())

    def createScrollableContainer():
        
        canvas_2.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
        sbHorizontalScrollBar.config(orient=HORIZONTAL, command=canvas_2.xview)
        sbVerticalScrollBar.config(orient=VERTICAL, command=canvas_2.yview)

        sbHorizontalScrollBar.pack(fill=X, side=BOTTOM, expand=FALSE)
        sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas_2.pack(fill=BOTH, side=LEFT, expand=TRUE)
        canvas_2.create_window(0, 0, window=ftable_2, anchor=NW)
    canvas_2.bind('<Configure>', lambda _: canvas_2.config(scrollregion=canvas_2.bbox('all')))

    canvas_2.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas_2.create_image(735.0,1457.0,image=image_image_1)


    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=more_page,relief="flat")
    button_1.place(x=1244,y=0)
    button_image_6 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=book_page,relief='flat')
    button_2.place(x=1059,y=0)
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=about_page,relief="flat")
    button_3.place(x=904,y=0)
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    
    button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: print("button_4 clicked"),relief="flat")
    button_4.place(x=749,y=0)
    createScrollableContainer()


    window.title('UAC User Home Page')
    window.mainloop()


def more_page():
    try:
        window2.destroy()
    except:
        window.destroy()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    global window3
    window3 = Tk()
    dark_title_bar(window3)

    window3.geometry("1440x720")
    window3.configure(bg = "#FFFFFF")


    canvas_3 = Canvas(
    window3,
    bg = "#FFFFFF",
    height = 720,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    ftable_3=Frame(canvas_3)
    sbHorizontalScrollBar = Scrollbar(window3)
    sbVerticalScrollBar = Scrollbar(window3)

    def updateScrollRegion():
        canvas_3.update_idletasks()
        canvas_3.config(scrollregion=ftable_3.bbox())

    def createScrollableContainer():
        canvas_3.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
        sbHorizontalScrollBar.config(orient=HORIZONTAL, command=canvas_3.xview)
        sbVerticalScrollBar.config(orient=VERTICAL, command=canvas_3.yview)

        sbHorizontalScrollBar.pack(fill=X, side=BOTTOM, expand=FALSE)
        sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas_3.pack(fill=BOTH, side=LEFT, expand=TRUE)
        canvas_3.create_window(0, 0, window=ftable_3, anchor=NW)

    canvas_3.bind('<Configure>', lambda _: canvas_3.config(scrollregion=canvas_3.bbox('all')))
    canvas_3.place(x = 0, y = 0)
    image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_3 = canvas_3.create_image(
    720.0,
    1608.0,
    image=image_image_3
    )

    button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
    button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=home_page,
    relief="flat"
    )
    button_9.place(
    x=749,
    y=0
    )

    button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
    button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=about_page,
    relief="flat"
    )
    button_10.place(
    x=904,
    y=0
    )

    button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=book_page,
    relief="flat"
    )
    button_11.place(
    x=1059,
    y=0
    )

    button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
    button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
    )
    button_12.place(
    x=1244,
    y=0
    )

    createScrollableContainer()
    window3.title('UAC Projects Page')
    window3.mainloop()

def about_page():
    try:
        window.destroy()
    except:
        window3.destroy()
        
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    global window2
    window2 = Tk()
    dark_title_bar(window2)
    window2.geometry("1440x720")
    window2.configure(bg = "#FFFFFF")


    canvas_2 = Canvas(
    window2,
    bg = "#FFFFFF",
    height = 720,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    ftable_2=Frame(canvas_2)
    sbHorizontalScrollBar = Scrollbar(window2)
    sbVerticalScrollBar = Scrollbar(window2)

    def updateScrollRegion():
        canvas_2.update_idletasks()
        canvas_2.config(scrollregion=ftable_2.bbox())

    def createScrollableContainer():
        canvas_2.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
        sbHorizontalScrollBar.config(orient=HORIZONTAL, command=canvas_2.xview)
        sbVerticalScrollBar.config(orient=VERTICAL, command=canvas_2.yview)

        sbHorizontalScrollBar.pack(fill=X, side=BOTTOM, expand=FALSE)
        sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas_2.pack(fill=BOTH, side=LEFT, expand=TRUE)
        canvas_2.create_window(0, 0, window=ftable_2, anchor=NW)

    canvas_2.bind('<Configure>', lambda _: canvas_2.config(scrollregion=canvas_2.bbox('all')))

    canvas_2.place(x = 0, y = 0)
    image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_1 = canvas_2.create_image(
    720.0,
    1925.0,
    image=image_image_2
    )

    button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
    button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=home_page,
    relief="flat"
    )
    button_5.place(
    x=749.0,
    y=0.0
    )

    button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
    button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
    )
    button_6.place(
    x=904.0,
    y=0.0
    )

    button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
    button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=book_page,
    relief="flat"
    )
    button_7.place(
    x=1059.0,
    y=0
    )

    button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
    button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=more_page,
    relief="flat"
    )
    button_8.place(
    x=1244.0,
    y=0.0
    )
    createScrollableContainer()
    window2.title('UAC About Page')
    window2.mainloop()
   

#End of About Page
#Beginning of projects/more page

window = Tk()
dark_title_bar(window)
window.geometry("1471x753")
window.configure(bg = "#FFFFFF")

canvas_2 = Canvas(window,bg = "#FFFFFF",height = 653,width = 1471,bd = 0,highlightthickness = 0,relief = "ridge")
ftable=Frame(canvas_2)

sbHorizontalScrollBar = Scrollbar(window)

sbVerticalScrollBar = Scrollbar(window)
def updateScrollRegion():
    canvas_2.update_idletasks()
    canvas_2.config(scrollregion=ftable.bbox())

def createScrollableContainer():
    canvas_2.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
    sbHorizontalScrollBar.config(orient=HORIZONTAL, command=canvas_2.xview)
    sbVerticalScrollBar.config(orient=VERTICAL, command=canvas_2.yview)

    sbHorizontalScrollBar.pack(fill=X, side=BOTTOM, expand=FALSE)
    sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
    canvas_2.pack(fill=BOTH, side=LEFT, expand=TRUE)
    canvas_2.create_window(0, 0, window=ftable, anchor=NW)
canvas_2.bind('<Configure>', lambda _: canvas_2.config(scrollregion=canvas_2.bbox('all')))

canvas_2.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas_2.create_image(735.0,1457.0,image=image_image_1)


button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=more_page,relief="flat")
button_1.place(x=1244.0,y=0)
button_image_6 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=book_page,relief="flat")
button_2.place(x=1059.0,y=0)
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=about_page,relief="flat")
button_3.place(x=904.0,y=0)
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: print("button_4 clicked"),relief="flat")
button_4.place(x=749.0,y=0)
createScrollableContainer()


window.title('UAC User Home Page')
window.mainloop()


connect.close()