from calculator_history import *
import math




class Calculator:
        # 0xE2 0x88 0x9B ∛

    def __init__(self, gui : ctk.CTk, title = 'SC BY ISMAEL SACKO'):

        self.__gui = gui
        self.__gui.title(title)

        #Les labels de chaque bouttons
        self.__labels_buttons = {'SHIFT' : 'SHIFT', 'Rad' : 'Rad(', 'sin' : 'sin(', 'cos' : 'cos(', 'tan' : 'tan(', 
                        'x^-1' : '^(-1)', '√' : '√(', 'e^x' : 'e^(', 'x^2' : '^(2)', 'x^y' : '^(', 
                        'ln' : 'ln(', 'log' : 'log(', 'hyp' : '', '(' : '(', ')' : ')', 
                        'mod' : 'mod', '+/-' : '', 'π' : 'π', '' : '', 'M+' : '', 
                        '7' : '7', '8' : '8','9' : '9', 'DEL' : 'DEL', 'AC' : 'AC',
                        '4' : '4', '5' : '5', '6' : '6', 'x' : 'x', '/' : '/', 
                        '1' : '1', '2' : '2', '3' : '3', '-' : '-','+' : '+',
                        '0' : '0', '.' : '.', 'Exp' : 'E', 'Ans' : 'Ans', '=' : '='}

        #Les labels de chaque bouttons lorsque la touche shift est enfoncée
        self.__labels_buttons_shift = {'SHIFT' : 'SHIFT', 'Rad' : 'Rad(', 'sin⁻¹' : 'sin⁻¹(', 'cos⁻¹' : 'cos⁻¹(', 'tan⁻¹' : 'tan⁻¹(', 
                        'x!' : '!', '∛' : '∛(', 'e^x' : 'e^(', 'x^3' : '^(3)', 'x^y' : '^(', 
                        'ln' : 'ln(', '10^y' : '10^(', 'hyp' : '', '(' : '(', ')' : ')', 
                        'mod' : 'mod', '+/-' : '', 'π' : 'π', 'M-' : '', 'M+' : '', 
                        '7' : '7', '8' : '8','9' : '9', 'DEL' : 'DEL', 'AC' : 'AC',
                        '4' : '4', '5' : '5', '6' : '6', 'x' : 'x', '/' : '/', 
                        '1' : '1', '2' : '2', '3' : '3', '-' : '-','+' : '+',
                        '0' : '0', '.' : '.', 'e' : 'e', 'PreAns' : 'PreAns', 'History' : 'History'}
        


        self.__enregistre_resultat = None
        # self.test = 'Hello'
        # print(f'{len(labels_buttons)} - {len(labels_buttons_shift)}')
        self.__history_calculator = CalculatorHistory(self, self.__gui)

        self.__fileName = 'calculator_history.txt'

        list_buttons = []

    @property
    def fileName(self):
        return self.__fileName


    def create_calculator_interface(self):
        """Crée l'interface graphique dde la calculatrice"""
        self.__div = ctk.CTkFrame(self.__gui, width= 328, height= 104, fg_color='white', corner_radius = 0)
        self.__div.pack_propagate(False)
        self.__div.pack(expand = 0, pady = (10, 0))

        self.__divScreen = ctk.CTkFrame(self.__div, fg_color='blue', width= 324, corner_radius = 0, height= 100)
        self.__divScreen.pack_propagate(False)
        self.__divScreen.pack(expand = 1, pady = (0, 0))


        self.__screenCalculator = ctk.CTkEntry(self.__divScreen, width = 325, height= 32, fg_color = 'black', corner_radius = 0, font = ('Times new roman', 15, 'bold'), border_width=0, border_color = 'white', text_color = 'white')
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

        self.create_calculator_touch()

    

    def create_calculator_touch(self):
        """Ajoute les bouttons de la calculatrice en mode tactile"""
        ligne, colonne = 0, 0
        self.__calculator_buttons = list()
        self.__press_touch_shift = False
        self.__press_egal_touch = False
        for label_button in self.__labels_buttons:
            if colonne > 4:
                ligne += 1
                colonne = 0
            button = ctk.CTkButton(self.__divButtons, width= 60, height = 45, text = label_button, font = ('Times new roman', 14, 'bold'), command = lambda label_button = label_button: self.showText(self.__labels_buttons[label_button]))
            button.grid(row = ligne, column = colonne, padx = (0, 5), pady = (5, 0))
            self.__calculator_buttons.append(button)
            # button.bind("<Button-1>", lambda label_button = label_button: print(f'l = {label_button}'))
            colonne += 1

    def __get_value_in_file(self, row : int, span: int = 1 ):
        """

        Args:
            row (int): _description_
            span (int, optional): _description_. Defaults to 1.

        Returns:
            _type_: _description_
        """        
        history_file = f'{os.getcwd()}/{self.fileName}'
        if os.path.exists(history_file) and len(self.__history_calculator.read_history_file()):
            print('Ce fichier existe')
            calculs_effectued = self.__history_calculator.read_history_file()
            print(f'calculs_effectued = {calculs_effectued}')
            try:
                print(f' row = {row} et span = {span}')
                return calculs_effectued[row][span]
            except IndexError:
                return ''
        return ''


    def __effectue_calcul(self):
        """Evalue et effectue le calcul de l'expression saisie

        Returns:
            float | int | Any: Resultat du calcul
        """

        # Contiendra tous les termes du calcul à effectuer
        operations_terms = []
        valeur_saisie = self.__screenCalculator.get()

        term = ''

        '''
            L'objectif ici est de séparé  la saisie en termes pour pouvoir effectué le calcul
            Pour cela on utilise une boucle while qui va parcourir chaque caractère de la saisie
            si un caractère defini est détecté, c'est que le terme est fini donc il est ajouté
            à la liste des termes

        '''
        for value in valeur_saisie: 
            
            if value not in ['+', '-', '/', 'x', '(', '^', 'E']:
                term += value
            else:

                operations_terms.append(term)
                operations_terms.append(value)
                term = ''
        # On ajoute le dernier terme (qui n'a pas été ajouté dans la boucle)
        operations_terms.append(term)

        # Pour chaque touche spéciale,  on associe la fonction correspondante
        functions_speciales = {'Rad' : 'math.radians', 'sin' : 'math.sin', 'cos' : 'math.cos', 'tan' : 'math.tan',
                            'ln' : 'math.log', 'log' : 'math.log10', '√' : 'math.sqrt', 'π' : 'math.pi', 'e' : 'math.e',
                            'Rad' : 'math.radians', '∛' : 'math.cbrt', 'x' : '*', '^' : '**', 'PreAns' : f'{self.__get_value_in_file(row = 1)}', 
                            'Ans' : f'{self.__get_value_in_file(row = 0)}', 'E' : '*10**', 'cos⁻¹':'math.acos', 'sin⁻¹':'math.asin', 'tan⁻¹':'math.atan'}
        


        operations_terms_tampon = list()

        for operation in operations_terms:
            '''
                Pour chaque terme faisant parti du calcul, l'on verifie s'il s'agit d'une touche spéciale.
                Si c'est le cas, on la remplace par la fonction mathématique associée. 
                Sinon, une exception est lévée signifiant qu'il ne s'agit pas d'une touche spéciale.
            '''
            try:
                operations_terms_tampon.append(functions_speciales[operation])
            except KeyError:
                operations_terms_tampon.append(operation)

        operations_terms = operations_terms_tampon

        operations_terms = [f"math.factorial({val.replace('!', '')})" if '!' in val else val for val in operations_terms]

        screen_value = "".join(operations_terms)
        screen_value = screen_value.replace('mod', '%')

        try:
            Resultat = eval(screen_value)
        except:
            Resultat = ''
            self.affiche_resultat(Resultat = Resultat)

            return 0
        if isinstance(Resultat, (float, int)) : self.affiche_resultat(Resultat = Resultat)
        print('return 1')
        return Resultat
        # return self.simple_calculate(screen_value)  

    def affiche_resultat(self, Resultat):
        """Affiche tout simplement le resultat passé en paramètre

        Args:
            Resultat (foat): Resultat du calcul
        """
        self.__screenResultat.configure(state='normal')

        self.__screenResultat.delete('1.0', 'end')
        for i in range(2):
            self.__screenResultat.insert('end', '\n')
        self.__screenResultat.tag_config("droite", justify="right")
        self.__screenResultat.insert("insert", f"{Resultat}", "droite")
        self.__screenResultat.configure(state='disabled')


    
    def showText(self, label_button:str):
        """Affiche la touche saisie

        Args:
            label_button (str): Le texte assoié à la touche
        """
        global __enregistre_resultat, __press_egal_touch, __press_touch_shift, __calculator_buttons, colonne, ligne
        # print(label_button.isdigit())


        #permet d'obtenir la position du curseur pour ensuite  effacer ou afficher du texte qu'a partir de l'endroit ou se trouve le curseur
        cursor_position = self.__screenCalculator.index('insert')
        print(f'position du curseur = {cursor_position}')
        # __effectue_calcul(label_button)

        screen_value = ''

        match label_button:
            case 'AC':
                self.__screenCalculator.delete('0', 'end')
                self.__effectue_calcul()
                self.__screenResultat.configure(state='normal')
                self.__screenResultat.delete('1.0', 'end')
                self.__screenResultat.configure(state='disabled')

            case 'DEL':
                # screenCalculator.configure(state='normal')
                # size_text = len(screenCalculator.get())
                special_func = ['Rad(', 'sin(', 'cos(', 'tan(', 'ln(', 'log(', '√(', 'mod', 'Ans', 'PreAns', 'sin⁻¹(', 'cos⁻¹(', 'tan⁻¹(', '∛(']
                val = self.__screenCalculator.get()

                print(f'position du curseur dans DEL= {cursor_position} - long de val = {len(val)-4}')
                # print(f'val a supp = {val} - long val = {len(val)} - val inversee = {val[cursor_position-i:cursor_position]}')

                # print(f"valeur a supprimee = {val[:4:-1]}")
                for i in range(2, 7):
                    if val[cursor_position-i:cursor_position] in special_func:
                        self.__screenCalculator.delete(cursor_position-i, cursor_position)
                        break

                else:
                    self.__screenCalculator.delete(cursor_position-1, cursor_position)

                self.__effectue_calcul()

            case 'SHIFT':
                self.__press_touch_shift = not self.__press_touch_shift
                
                for button in self.__calculator_buttons:
                    button.configure(text = '')

                new_labels_buttons = self.__labels_buttons_shift if self.__press_touch_shift else self.__labels_buttons
                for button, label_button in zip(self.__calculator_buttons, new_labels_buttons.keys()):
                    button.configure(text = label_button, command = lambda label_button = label_button: self.showText(new_labels_buttons[label_button]))

            case 'Ans' :
                if self.__press_egal_touch:
                    self.__screenCalculator.delete('0', 'end')
                    self.__screenCalculator.insert('0', 'Ans')
                else:
                    self.__screenCalculator.insert(cursor_position, 'Ans')
                self.__effectue_calcul()

                
            
            case '=' : 
                verif_resultat = self.__effectue_calcul()
                self.__press_egal_touch = not self.__press_egal_touch
                
                # if self.__screenCalculator.get() and self.__screenResultat.get('1.0', 'end-1c').strip():
                #     self.__history_calculator.save_operation((self.__screenCalculator.get(), self.__screenResultat.get('1.0', 'end-1c').strip()))
                
                

                # self.__enregistre_resultat = self.__screenResultat.get('1.0', 'end-1c').strip()


                if self.__screenCalculator.get():
                    if not verif_resultat:
                        print('Syntaxe erreur')
                        self.affiche_resultat(Resultat='Erreur de syntaxe')
                    else:
                        # print(f'verif_resultat = {self.__screenCalculator.get()} - __get_value_in_file = {self.__get_value_in_file(position = 0)[0]}')
                        if not len(self.__history_calculator.read_history_file()):
                            self.__history_calculator.save_operation((self.__screenCalculator.get(), self.__screenResultat.get('1.0', 'end-1c').strip()))

                        elif self.__screenCalculator.get() != self.__get_value_in_file(row = 0, span = 0):
                            print(f'hello {self.__screenCalculator.get()}  {self.__get_value_in_file(row = 0, span = 0)}')
                            self.__history_calculator.save_operation((self.__screenCalculator.get(), self.__screenResultat.get('1.0', 'end-1c').strip()))

                else:
                    self.affiche_resultat(Resultat = 'Saisie vide')
                # self.__effectue_calcul()  
            case 'History':
                print('history')
                self.__div.destroy()
                self.__divCalculator.destroy()

                self.__history_calculator.show_history_block(self.__gui)
            case _:

                if self.__press_egal_touch:
                    if label_button in ['+', '-', '/', 'x']:
                        self.__screenCalculator.delete('0', 'end')
                        self.__screenCalculator.insert('0', f'Ans{label_button}')
                    else:
                        self.__screenCalculator.delete('0', 'end')
                        self.__screenCalculator.insert('0', label_button)
                        self.__effectue_calcul()
                    self.__press_egal_touch = not self.__press_egal_touch
                    

                else:
                    self.__screenCalculator.insert(f"{cursor_position}", label_button)
                    self.__effectue_calcul()




