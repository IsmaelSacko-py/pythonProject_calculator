from calculator import *

gui = ctk.CTk()
gui.title("scientific calculator by SACKO Ismael".upper())
gui.geometry("350x550")
gui.resizable(width = False, height= False)
gui.configure(bg = 'red')
gui._set_appearance_mode('light')

calculator = Calculator(gui = gui)
calculator.create_calculator_interface()


gui.mainloop()