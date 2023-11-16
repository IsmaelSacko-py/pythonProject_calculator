# import math

# # number = [4, 2, 7]
# # # test = lambda e = number: 0 if not e else e[0] - test(e[1:])
# # def test(N, liste = number):
# #     if len(liste) == 1:
# #         return 0
# #     print(f'Valeur = {liste[0]}')
# #     return liste[0] - test(liste[1:])
# # chaine = ''
# # for i in range(10):
# #     chaine+='o'

# # print(math.exp(3))

# # x = "x"
# x = "x"
# y = "y"  # Remplacez "y" par le chiffre que vous souhaitez afficher en exposant

# # Créez un dictionnaire de remplacement pour les chiffres en exposant
# exposant_dict = {str(i): chr(0x2070 + i) for i in range(10)}

# # Utilisez le dictionnaire de remplacement pour créer l'exposant en haut
# exposant_y = y.translate(str.maketrans(exposant_dict))

# expression = f"{x}{y}{exposant_y}"

# 	# 0xE2 0x88 0x9B

# a = False
# a = not a
# print(a)
# a = not a
# print(a)
import customtkinter as ctk
from tkinter import *
import math
from datetime import datetime
from PIL import Image, ImageTk

maintenant = datetime.now()
# maintenant.
jour, mois, annee = maintenant.day, maintenant.strftime('%B'), maintenant.year
date = f"{jour}  {mois[:3]}.  {annee}"

gui = ctk.CTk()
gui.title("Historique des calculs".upper())
gui.geometry("350x550")
gui.resizable(width = False, height= False)
# gui._set_appearance_mode('dark')
label_frame = ctk.CTkScrollableFrame(gui, width = 350, height = 550, border_width = 0)
label_frame.pack()

resultat_block = []
def showCalcul(id):
    print(f'calcul = {resultat_block[id]}')

for i in range(10):
    main_div = ctk.CTkFrame(label_frame, fg_color='white', border_color= 'white', corner_radius=0, width = 345, height = 105)
    main_div.pack(anchor = 'center', pady = (3, 0))
    main_div.pack_propagate(False)
    # divCalcul._set_appearance_mode('dark')

    divCalcul = ctk.CTkFrame(main_div, fg_color='yellow', corner_radius=0, width = 327, height = 100)
    divCalcul.pack(expand = 1, pady = (1, 1))
    divCalcul.pack_propagate(False)


    divScreen = ctk.CTkFrame(divCalcul, fg_color='red', corner_radius=0, width = 325, height = 75)
    divScreen.pack(anchor = 'center')
    divScreen.pack_propagate(False)

    screen = ctk.CTkTextbox(divScreen, fg_color='gray', corner_radius=0, width = 345, height = 75, font = ('Times new roman', 18, 'bold'))
    screen.pack(anchor = 'center')
    divScreen.pack_propagate(False)
    resultat_block.append((f'{i} x 10', i*10))
    screen.insert('1.0', f'{i} x 10 \n\n')
    # screen.insert('end', ' ')
    screen.tag_config("droite", justify="right")
    screen.insert("insert", f'{i*10}', "droite")

    div = ctk.CTkFrame(divCalcul, width = 325, height = 30, corner_radius=0, fg_color='green')
    div.pack_propagate(False)
    div.pack()

    divDate = ctk.CTkFrame(div, fg_color='blue', corner_radius=0, width = 120, height = 30)
    divDate.pack(side = 'left')
    divDate.pack_propagate(False)
    label_date = ctk.CTkLabel(divDate, text = date, fg_color='blue', font = ('Times new roman', 15, 'bold'))
    label_date.pack()

    divAction = ctk.CTkFrame(div, fg_color='blue', corner_radius=0, width = 120, height = 30)
    # divAction.pack_propagate(False)
    divAction.pack(side = 'right')

    image_delete = ctk.CTkImage(Image.open('Images/delete.png'), size = (20, 20))
    image_modify = ctk.CTkImage(Image.open('Images/pencil.png'), size = (20, 20))

    delete_button = ctk.CTkButton(divAction, fg_color='yellow', text = '', corner_radius=0, width = 30, height = 20, image= image_delete, command = lambda id = i: showCalcul(id))
    delete_button.grid(row = 0, column = 0)

    modify_button = ctk.CTkButton(divAction, fg_color='yellow', text= '', corner_radius=0, width = 30, height = 20, image= image_modify, command = lambda id = i: showCalcul(id))
    modify_button.grid(row = 0, column = 1)

    # label_delete = Label(divAction, width = 75, height = 20, text = '🗑')
    # label_delete.grid(row = 0, column = 0)
    # label_modify = Label(divAction, width = 75, height = 20, text = '✏')
    # label_modify.grid(row = 0, column = 1)
    # divDate = Button(div)
    # button.grid()


# gui.mainloop()
l = ['3!', '4', '5!', '55']

for i, val in enumerate(l):
    if '!' in val:
        l[i] = f"math.factorial({val.replace('!', '')})"

print(l)
