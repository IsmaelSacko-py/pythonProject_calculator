import customtkinter as ctk
# from tkinter import *
from datetime import datetime
from PIL import Image
# import pickle

class CalculatorHistory:
    

    def __init__(self, calculator, gui):
        self.__gui = gui
        self.__calculator = calculator
        self.__history_block_color = '#273238'
        self.__history_bg_color = '#e0e0e0'

        # self.__label_frame.pack()
        # gui.configure(bg = 'green')

    #     self.__resultat_block = []


    def __show_history_calcul(self, id):
        self.__quit_history()
        calculs_effectued = self.__read_history_file()
        calcul_effectued = calculs_effectued[id]
        self.__calculator.screenCalculator(calcul_effectued[0])
        self.__calculator.affiche_resultat(calcul_effectued[1])
    
    def __delete_calcul_in_calculator_history(self, id):
        # pass
        calculs_effectued = self.__read_history_file()
        calculs_effectued.pop(id)
        # print(f'historique = {calculs_effectued}')
        with open("calculator_history.txt", "w") as f:
            for calcul in calculs_effectued:
                f.write(f"{'#'.join(calcul)}\n")
        self.__historyDiv.destroy()
        self.show_history_block(self.__gui)



    def __create_block_history(self, id, calcul : tuple):

        # maintenant = datetime.now()
        # # maintenant.
        # jour, mois, annee = maintenant.second, maintenant.strftime('%B'), maintenant.year
        # date = f"{jour}  {mois[:3]}.  {annee}"
        # print(f'temps = {date}')
        self.__main_div = ctk.CTkFrame(self.__label_frame, fg_color='white', border_color= 'white', corner_radius=0, width = 345, height = 105)
        self.__main_div.pack(anchor = 'center', pady = (3, 0))
        self.__main_div.pack_propagate(False)
        # divCalcul._set_appearance_mode('dark')

        self.__divCalcul = ctk.CTkFrame(self.__main_div, corner_radius=0, width = 327, height = 100)
        self.__divCalcul.pack(expand = 1, pady = (1, 1))
        self.__divCalcul.pack_propagate(False)


        self.__divScreen = ctk.CTkFrame(self.__divCalcul, corner_radius=0, width = 325, height = 75)
        self.__divScreen.pack(anchor = 'center')
        self.__divScreen.pack_propagate(False)

        self.__screen = ctk.CTkTextbox(self.__divScreen, fg_color=self.__history_block_color, corner_radius=0, width = 345, height = 75, font = ('Times new roman', 18, 'bold'))
        self.__screen.pack(anchor = 'center')
        self.__divScreen.pack_propagate(False)
        # self.__resultat_block.append((f'{i} x 10', i*10))
        self.__screen.insert('1.0', f'{calcul[0]} \n\n')
        # screen.insert('end', ' ')
        self.__screen.tag_config("droite", justify="right")
        self.__screen.insert("insert", f'{calcul[1]}', "droite")

        self.__div = ctk.CTkFrame(self.__divCalcul, width = 325, height = 50, corner_radius=0, fg_color=self.__history_block_color)
        self.__div.pack_propagate(False)
        self.__div.pack()

        self.__divDate = ctk.CTkFrame(self.__div, fg_color=self.__history_block_color, corner_radius=0, width = 120, height = 40)
        self.__divDate.pack(side = 'left')
        self.__divDate.pack_propagate(False)
        self.__label_date = ctk.CTkLabel(self.__divDate, text = f'{calcul[2]}', font = ('Times new roman', 15, 'bold'))
        self.__label_date.pack()

        self.__divAction = ctk.CTkFrame(self.__div, fg_color=self.__history_block_color, corner_radius=0, width = 120, height = 40)
        # self.__divAction.pack_propagate(False)
        self.__divAction.pack(side = 'right')

        self.__image_delete = ctk.CTkImage(Image.open('Images/delete1.png'), size = (15, 15))
        self.__image_modify = ctk.CTkImage(Image.open('Images/pencil1.png'), size = (15, 15))

        self.__delete_button = ctk.CTkButton(self.__divAction, fg_color=self.__history_block_color, text = '', corner_radius=0, width = 30, height = 20, image= self.__image_delete, command = lambda id = id: self.__delete_calcul_in_calculator_history(id))
        # self.__delete_button = ctk.CTkButton(self.__divAction, fg_color='yellow', text = '', corner_radius=0, width = 30, height = 20, image= self.__image_delete, command = lambda id = id: self.__show_history_calcul(id))
        self.__delete_button.grid(row = 0, column = 0)

        self.__modify_button = ctk.CTkButton(self.__divAction, fg_color=self.__history_block_color, text= '', corner_radius=0, width = 30, height = 20, image= self.__image_modify, command = lambda id = id: self.__show_history_calcul(id))
        self.__modify_button.grid(row = 0, column = 1)

        # self.__history_blocks.append(self.__main_div)


    def save_operation(self, calcul : tuple):
        maintenant = datetime.now()
        # maintenant.
        jour, mois, annee = maintenant.day, maintenant.strftime('%B'), maintenant.year
        date = f"{jour} {mois[:3]}. {annee}"
        with open('calculator_history.txt', 'a+', encoding='UTF-8') as f:
            calcul = f"{calcul[0]}#{calcul[1]}#{date}\n"
            f.write(calcul)

    def __quit_history(self):
        self.__historyDiv.destroy()

        # self.__calculator.__calculator_buttons = list()
        self.__calculator.create_calculator_interface()
    
    def __read_history_file(self):
        with open('calculator_history.txt', 'r', encoding='UTF-8') as f:
            calculs_effectued = reversed(f.readlines())
            calculs_effectued = [(calcul.strip().split('#')) for calcul in calculs_effectued]
        return calculs_effectued
        


    def show_history_block(self, gui):
        # app = ctk.CTkToplevel()
        # app.title("scientific calculator by SACKO Ismael".upper())

        # app.geometry("350x550")
        # app.resizable(width = False, height= False)
        # app.configure(bg = 'red')
        # app._set_appearance_mode('dark')
        

        self.__historyDiv = ctk.CTkFrame(gui, corner_radius = 0)
        self.__historyDiv.pack(expand = 1)

        self.__frame_text = ctk.CTkFrame(self.__historyDiv, fg_color = 'light blue', corner_radius = 0, width=350, height=50)
        self.__frame_text.pack()
        self.__frame_text.pack_propagate(False)

        self.__back_image = ctk.CTkImage(Image.open('Images/back.png'), size = (20, 20))
        self.__back_button = ctk.CTkButton(self.__frame_text, text = '', width = 20, image = self.__back_image, fg_color= 'light blue', height = 10, command = self.__quit_history)
        self.__back_button.pack(side = 'left')

        self.__historyLabel = ctk.CTkLabel(self.__frame_text, text = 'Historique des calculs', height = 10, text_color = "black", font = ("Times new roman", 20, 'bold'))
        self.__historyLabel.pack(side = 'left', padx = (20, 0))
        
        self.__label_frame = ctk.CTkScrollableFrame(self.__historyDiv, width = 350, height = 550, fg_color = self.__history_bg_color, corner_radius = 0, border_width = 0)

        self.__label_frame.pack(padx = 2, pady =0)

        calculs_effectued = self.__read_history_file()
            # calculs_effectued = [tuple(calcul) for calcul in calculs_effectued]
            # print((calculs_effectued))
        for id, calcul in enumerate(calculs_effectued):
            self.__create_block_history(id, calcul)
            # print(f'{operation} - {type(operation)}')
        # app.mainloop()




# gui = ctk.CTk()
# gui.title("scientific calculator by SACKO Ismael".upper())
# gui.geometry("350x550")
# gui.resizable(width = False, height= False)
# gui.configure(bg = 'red')


# calculator = CalculatorHistory()
# calculator.show_history_block()

# gui.mainloop()