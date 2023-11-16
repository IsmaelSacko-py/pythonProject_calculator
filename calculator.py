from calculator_history import *
import math




class Calculator:
        # 0xE2 0x88 0x9B ∛

    def __init__(self, gui : ctk.CTk, title = 'SC BY ISMAEL SACKO'):

        self.__gui = gui
        self.__gui.title(title)
        self.__labels_buttons = {'SHIFT' : 'SHIFT', 'Rad' : 'Rad(', 'sin' : 'sin(', 'cos' : 'cos(', 'tan' : 'tan(', 
                        'x^-1' : '^(-1)', '√' : '√(', 'e^x' : 'e^(', 'x^2' : '^(2)', 'x^y' : '^(', 
                        'ln' : 'ln(', 'log' : 'log(', 'hyp' : '', '(' : '(', ')' : ')', 
                        'mod' : 'mod', '+/-' : '', 'π' : 'π', '' : '', 'M+' : '', 
                        '7' : '7', '8' : '8','9' : '9', 'DEL' : 'DEL', 'AC' : 'AC',
                        '4' : '4', '5' : '5', '6' : '6', 'x' : 'x', '/' : '/', 
                        '1' : '1', '2' : '2', '3' : '3', '-' : '-','+' : '+',
                        '0' : '0', '.' : '.', 'Exp' : 'E', 'Ans' : 'Ans', '=' : '='}

        self.__labels_buttons_shift = {'SHIFT' : 'SHIFT', 'Rad' : 'Rad(', 'sin⁻¹' : 'sin⁻¹(', 'cos⁻¹' : 'cos⁻¹(', 'tan⁻¹' : 'tan⁻¹(', 
                        'x!' : '!', '∛' : '∛(', 'e^x' : 'e^(', 'x^3' : '^(3)', 'x^y' : '^(', 
                        'ln' : 'ln(', '10^y' : '10^(', 'hyp' : '', '(' : '(', ')' : ')', 
                        'mod' : 'mod', '+/-' : '', 'π' : 'π', '' : '', 'M+' : '', 
                        '7' : '7', '8' : '8','9' : '9', 'DEL' : 'DEL', 'AC' : 'AC',
                        '4' : '4', '5' : '5', '6' : '6', 'x' : 'x', '/' : '/', 
                        '1' : '1', '2' : '2', '3' : '3', '-' : '-','+' : '+',
                        '0' : '0', '.' : '.', 'e' : 'e', 'PreAns' : 'PreAns', 'History' : 'History'}
        

        self.__history_calculator = CalculatorHistory()
        self.__calculator_buttons = list()

        self.__enregistre_resultat = None
        self.__press_touch_schift = False
        self.__press_egal_touch = False
        # print(f'{len(labels_buttons)} - {len(labels_buttons_shift)}')

        list_buttons = []


    def create_calculator_interface(self):
        self.__div = ctk.CTkFrame(self.__gui, width= 328, height= 104, fg_color='white', corner_radius = 0)
        self.__div.pack_propagate(False)
        self.__div.pack(expand = 0, pady = (10, 0))

        self.__divScreen = ctk.CTkFrame(self.__div, fg_color='blue', width= 324, corner_radius = 0, height= 100)
        self.__divScreen.pack_propagate(False)
        self.__divScreen.pack(expand = 1, pady = (0, 0))


        self.__screenCalculator = ctk.CTkEntry(self.__divScreen, width = 325, height= 30, fg_color = 'black', corner_radius = 0, font = ('Times new roman', 15, 'bold'), border_width=0, border_color = 'white', text_color = 'white')
        self.__screenCalculator.bind('<Key>', lambda event: 'break')
        self.__screenCalculator.pack(padx = (0, 0))
        self.__screenCalculator.focus()


        self.__screenResultat = ctk.CTkTextbox(self.__divScreen, width = 325, height = 80, fg_color = 'black', corner_radius = 0, font = ('Arial', 15, 'bold'), text_color='white', state = 'disabled')
        # self.__screenResultat.pack_propagate(False)
        # scBar.pack_forget()
        self.__screenResultat.pack(pady = (0, 0))


        self.__divCalculator = ctk.CTkFrame(self.__gui, width= 400, height= 380, fg_color = 'white', corner_radius = 0)
        # self.__divCalculator.pack_propagate(False)
        # self.__divCalculator.configure(fg_color = 'blue')
        self.__divCalculator.pack(expand = 0)


        self.__divButtons = ctk.CTkFrame(self.__divCalculator, width = 323, height = 405, fg_color = 'green', corner_radius = 0)
        self.__divButtons.configure(fg_color = 'white')
        self.__divButtons.grid_propagate(False)
        self.__divButtons.grid(padx = (3, 0))

        self.__create_calculator_touch()


    def __create_calculator_touch(self):
        ligne, colonne = 0, 0

        for label_button in self.__labels_buttons:
            if colonne > 4:
                ligne += 1
                colonne = 0
            button = ctk.CTkButton(self.__divButtons, width= 60, height = 45, text = label_button, font = ('Times new roman', 14, 'bold'), command = lambda label_button = label_button: self.showText(self.__labels_buttons[label_button]))
            button.grid(row = ligne, column = colonne, padx = (0, 5), pady = (5, 0))
            self.__calculator_buttons.append(button)
            # button.bind("<Button-1>", lambda label_button = label_button: print(f'l = {label_button}'))
            colonne += 1



    def __verif_expression(self):
        position, i = 0, 0
        operations_terms = []
        operations = []
        valeur_saisie = self.__screenCalculator.get()

        term = ''
        for value in valeur_saisie: 
            
            if value not in ['+', '-', '/', 'x', '(', '^', 'E']:
                term += value
            else:
                # print(f'valeur saisie gg = {screenCalculator.get()}')

                operations_terms.append(term)
                operations_terms.append(value)
                term = ''

        operations_terms.append(term)
        functions_speciales = {'Rad' : 'math.radians', 'sin' : 'math.sin', 'cos' : 'math.cos', 'tan' : 'math.tan',
                            'ln' : 'math.log', 'log' : 'math.log10', '√' : 'math.sqrt', 'π' : 'math.pi', 'e' : 'math.e',
                            'Rad' : 'math.radians', '∛' : 'math.cbrt', 'x' : '*', '^' : '**', 'Ans' : f'{self.__enregistre_resultat}', 
                            'E' : '*10**', 'cos⁻¹':'math.acos', 'sin⁻¹':'math.asin', 'tan⁻¹':'math.atan'}
        
        print(f'val = {[val for val in operations_terms]}')
        print(f'operations_terms = {operations_terms}')
        operations_terms = [functions_speciales[func] if func in functions_speciales.keys() else func for func in operations_terms]
        operations_terms = [f"math.factorial({val.replace('!', '')})" if '!' in val else val for val in operations_terms]
        print(f'operations_terms = {operations_terms}')


        # operations_terms = [val.replace(val[:3], functions_speciales[val[:3]]) if val and val[:3] in functions_speciales.keys() else val for val in operations_terms]
        # operations_terms = [val.replace(val[:2], functions_speciales[val[:2]]) if val and val[:2] in functions_speciales.keys() else val for val in operations_terms]
        # operations_terms = [val.replace(val[0], functions_speciales[val[0]]) if val and val[0] in functions_speciales.keys() else val for val in operations_terms]

        screen_value = "".join(operations_terms)
        screen_value = screen_value.replace('mod', '%')
        return self.simple_calculate(screen_value)  



        

    # i = 0
    def simple_calculate(self, screen_value):
        '''Permet de faire des calculs simples'''
        global affiche_resultat

        print(f'screen_value = {screen_value}')
        def affiche_resultat(Resultat):
            self.__screenResultat.configure(state='normal')

            self.__screenResultat.delete('1.0', 'end')
            for i in range(2):
                self.__screenResultat.insert('end', '\n')
            self.__screenResultat.tag_config("droite", justify="right")
            self.__screenResultat.insert("insert", f"{Resultat}", "droite")
            self.__screenResultat.configure(state='disabled')

        # if screen_value:
        try:
            Resultat = eval(screen_value)
        except:
            Resultat = ''
            affiche_resultat(Resultat = Resultat)
            # screenResultat.configure(state='normal')
            # screenResultat.delete('1.0', 'end')
            # screenResultat.configure(state='disabled')
            

            print('return 0')
            return 0
        if isinstance(Resultat, (float, int)) : affiche_resultat(Resultat = Resultat)
        print('return 1')
        return 1
        
        # else:
        #     if button_clicker == '=' : affiche_resultat(Resultat = "Saisie vide")

    
    def showText(self, label_button:str):
        global __enregistre_resultat, __press_egal_touch, __press_touch_schift, __calculator_buttons, colonne, ligne
        # print(label_button.isdigit())


        #permet d'obtenir la position du curseur pour ensuite  effacer ou afficher du texte qu'a partir de l'endroit ou se trouve le curseur
        cursor_position = self.__screenCalculator.index('insert')
        print(f'position du curseur = {cursor_position}')
        # __verif_expression(label_button)

        screen_value = ''

        match label_button:
            case 'AC':
                self.__screenCalculator.delete('0', 'end')
                self.__verif_expression()
                self.__screenResultat.configure(state='normal')
                self.__screenResultat.delete('1.0', 'end')
                self.__screenResultat.configure(state='disabled')

            case 'DEL':
                # screenCalculator.configure(state='normal')
                # size_text = len(screenCalculator.get())
                special_func = ['Rad(', 'sin(', 'cos(', 'tan(', 'ln(', 'log(', '√(', 'mod', 'Ans']
                val = self.__screenCalculator.get()
                print(f'position du curseur dans DEL= {cursor_position} - long de val = {len(val)-4}')
                # print(f'val a supp = {val} - long val = {len(val)} - val inversee = {val[cursor_position-i:cursor_position]}')

                # print(f"valeur a supprimee = {val[:4:-1]}")
                for i in range(2, 5):
                    if val[cursor_position-i:cursor_position] in special_func:
                        self.__screenCalculator.delete(cursor_position-i, cursor_position)
                        break

                else:
                    self.__screenCalculator.delete(cursor_position-1, cursor_position)

                self.__verif_expression()

            case 'SHIFT':
                self.__press_touch_schift = not self.__press_touch_schift
                for button in self.__calculator_buttons:
                    button.configure(text = '')
                # calculator_buttons = []
                new_labels_buttons = self.__labels_buttons_shift if self.__press_touch_schift else self.__labels_buttons
                for button, label_button in zip(self.__calculator_buttons, new_labels_buttons.keys()):
                    # print(f'label button = {labels_buttons_shift[label_button]}')
                    button.configure(text = label_button, command = lambda label_button = label_button: self.showText(new_labels_buttons[label_button]))

            case 'Ans' :
                if self.__press_egal_touch:
                    self.__screenCalculator.delete('0', 'end')
                    self.__screenCalculator.insert('0', 'Ans')
                else:
                    self.__screenCalculator.insert(cursor_position, 'Ans')

                self.__verif_expression()
                
            
            case '=' : 
                if self.__screenCalculator.get() and self.__screenResultat.get('1.0', 'end-1c').strip():
                    self.__history_calculator.save_operation((self.__screenCalculator.get(), self.__screenResultat.get('1.0', 'end-1c').strip()))
                
                
                verif_resultat = self.__verif_expression()

                self.__enregistre_resultat = self.__screenResultat.get('1.0', 'end-1c').strip()
                self.__press_egal_touch = not self.__press_egal_touch


                if self.__screenCalculator.get():
                    if not verif_resultat:
                        print('Syntaxe erreur')
                        affiche_resultat(Resultat='Erreur de syntaxe')
                else:
                    affiche_resultat(Resultat = 'Saisie vide')
                # self.__verif_expression()  
            case 'History':
                print('history')
                self.__history_calculator.show_history_block()
            case _:

                if self.__press_egal_touch:
                    if label_button in ['+', '-', '/', 'x']:
                        self.__screenCalculator.delete('0', 'end')
                        self.__screenCalculator.insert('0', f'Ans{label_button}')
                    else:
                        self.__screenCalculator.delete('0', 'end')
                        self.__screenCalculator.insert('0', label_button)
                    self.__press_egal_touch = not self.__press_egal_touch
                    

                else:
                    self.__screenCalculator.insert(f"{cursor_position}", label_button)
                    self.__verif_expression()





print(math.asin(-1))