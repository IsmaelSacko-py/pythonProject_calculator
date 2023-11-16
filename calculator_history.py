import customtkinter as ctk
# from tkinter import *
from datetime import datetime
from PIL import Image
import pickle

class CalculatorHistory:
    

    # def __init__(self):

        # self.__label_frame.pack()
        # gui.configure(bg = 'green')

    #     self.__resultat_block = []


    # def showCalcul(self, id):
    #     print(f'calcul = {self.__resultat_block[id]}')


    def __create_block_history(self, operation : tuple):

        # maintenant = datetime.now()
        # # maintenant.
        # jour, mois, annee = maintenant.second, maintenant.strftime('%B'), maintenant.year
        # date = f"{jour}  {mois[:3]}.  {annee}"
        # print(f'temps = {date}')
        self.__main_div = ctk.CTkFrame(self.__label_frame, fg_color='white', border_color= 'white', corner_radius=0, width = 345, height = 105)
        self.__main_div.pack(anchor = 'center', pady = (3, 0))
        self.__main_div.pack_propagate(False)
        # divCalcul._set_appearance_mode('dark')

        self.__divCalcul = ctk.CTkFrame(self.__main_div, fg_color='yellow', corner_radius=0, width = 327, height = 100)
        self.__divCalcul.pack(expand = 1, pady = (1, 1))
        self.__divCalcul.pack_propagate(False)


        self.__divScreen = ctk.CTkFrame(self.__divCalcul, fg_color='red', corner_radius=0, width = 325, height = 75)
        self.__divScreen.pack(anchor = 'center')
        self.__divScreen.pack_propagate(False)

        self.__screen = ctk.CTkTextbox(self.__divScreen, fg_color='gray', corner_radius=0, width = 345, height = 75, font = ('Times new roman', 18, 'bold'))
        self.__screen.pack(anchor = 'center')
        self.__divScreen.pack_propagate(False)
        # self.__resultat_block.append((f'{i} x 10', i*10))
        self.__screen.insert('1.0', f'{operation[0]} \n\n')
        # screen.insert('end', ' ')
        self.__screen.tag_config("droite", justify="right")
        self.__screen.insert("insert", f'{operation[1]}', "droite")

        self.__div = ctk.CTkFrame(self.__divCalcul, width = 325, height = 30, corner_radius=0, fg_color='green')
        self.__div.pack_propagate(False)
        self.__div.pack()

        self.__divDate = ctk.CTkFrame(self.__div, fg_color='blue', corner_radius=0, width = 120, height = 30)
        self.__divDate.pack(side = 'left')
        self.__divDate.pack_propagate(False)
        self.__label_date = ctk.CTkLabel(self.__divDate, text = f'{operation[2]}', fg_color='blue', font = ('Times new roman', 15, 'bold'))
        self.__label_date.pack()

        self.__divAction = ctk.CTkFrame(self.__div, fg_color='blue', corner_radius=0, width = 120, height = 30)
        # self.__divAction.pack_propagate(False)
        self.__divAction.pack(side = 'right')

        self.__image_delete = ctk.CTkImage(Image.open('Images/delete.png'), size = (20, 20))
        self.__image_modify = ctk.CTkImage(Image.open('Images/pencil.png'), size = (20, 20))

        self.__delete_button = ctk.CTkButton(self.__divAction, fg_color='yellow', text = '', corner_radius=0, width = 30, height = 20, image= self.__image_delete, command = lambda id = 1: self.showCalcul(id))
        self.__delete_button.grid(row = 0, column = 0)

        self.__modify_button = ctk.CTkButton(self.__divAction, fg_color='yellow', text= '', corner_radius=0, width = 30, height = 20, image= self.__image_modify, command = lambda id = 1: self.showCalcul(id))
        self.__modify_button.grid(row = 0, column = 1)

        # self.__history_blocks.append(self.__main_div)

        print(f'liste des blocks 1')

    def save_operation(self, operation : tuple):
        maintenant = datetime.now()
        # maintenant.
        jour, mois, annee = maintenant.day, maintenant.strftime('%B'), maintenant.year
        date = f"{jour} {mois[:3]}. {annee}"
        with open('calculator_history.txt', 'a+', encoding='UTF-8') as f:
            operation = f"{operation[0]}#{operation[1]}#{date}\n"
            f.write(operation)


    def show_history_block(self):
        app = ctk.CTkToplevel()
        app.title("scientific calculator by SACKO Ismael".upper())

        app.geometry("350x550")
        app.resizable(width = False, height= False)
        app.configure(bg = 'red')
        app._set_appearance_mode('light')
        
        self.__label_frame = ctk.CTkScrollableFrame(app, width = 350, height = 550, border_width = 0)

        self.__label_frame.pack()

        with open('calculator_history.txt', 'r', encoding='UTF-8') as f:
            operations_effectued = reversed(f.readlines())
            operations_effectued = [(operation.strip().split('#')) for operation in operations_effectued]
            # operations_effectued = [tuple(operation) for operation in operations_effectued]
            # print((operations_effectued))
        for operation in operations_effectued:
            self.__create_block_history(operation)
            # print(f'{operation} - {type(operation)}')
        app.mainloop()




# gui = Tk()
# gui.title("scientific calculator by SACKO Ismael".upper())
# gui.geometry("350x550")
# gui.resizable(width = False, height= False)
# gui.configure(bg = 'red')

# def test(gui):
#     gui.configure(bg = 'yellow')




# history = CalculatorHistory(gui)

# # history.__create_block_history(operation = ('2x3', '6'))
# history.show_history_block()

# gui.mainloop()