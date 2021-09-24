# Module menu du Jeu de la vie


import tkinter


class Menu:
    ''' Classe qui affiche une fenêtre de menu pour le jeu de la vie '''
    
    def __init__(self):
        ''' Constructeur de la classe Menu
                Argument: une classe Menu
                Return:
        '''
        
        self.__fenetre=tkinter.Tk()
        self.__fenetre.title('Menu')
        
        
        image_logo=tkinter.PhotoImage(file='img/logo.gif')
        logo=tkinter.Label(self.__fenetre,image=image_logo).pack()
        
        
        demande_lig=tkinter.Label(self.__fenetre,text='Combien voulez-vous de lignes dans la grille ?',font=400).pack()
        
        self.__lig=tkinter.StringVar()
        self.__lig.set("15")
        entree_ligne=tkinter.Entry(textvariable=self.__lig,width=3).pack()
        
        
        demande_col=tkinter.Label(self.__fenetre,text='Combien voulez-vous de colonnes dans la grille ?',font=200).pack()
        
        self.__col=tkinter.StringVar()
        self.__col.set("25")
        entree_col=tkinter.Entry(textvariable=self.__col,width=3).pack()
        
        
        valider=tkinter.Button(self.__fenetre,text='Valider',command=self.__fenetre.destroy).pack()
        
        
        self.__arreter_jeu=False
        
        image_quitter=tkinter.PhotoImage(file='img/exit.gif')
        bouton_quitter=tkinter.Button(self.__fenetre,image=image_quitter,command=self.quitter).pack()
        
        
        self.__fenetre.mainloop()
    
    
    def lig(self):
        ''' Méthode qui retourne la valeur choisie pour le nombre de lignes
                Argument: une classe Menu
                Return: un entier
        '''
        
        return int(self.__lig.get())
    
    
    def col(self):
        ''' Méthode qui retourne la valeur choisie pour le nombre de lignes
                Argument: une classe Menu
                Return: un entier
        '''
        
        return int(self.__col.get())
    
    
    def quitter(self):
        ''' Méthode qui ajoute l'argument arreter_jeu à la classe et ferme la fenêtre 
                Argument: une classe Menu
                Return:
        '''
        
        self.__arreter_jeu=True
        
        self.__fenetre.destroy()
        
    
    def arreter_jeu(self):
        ''' Méthode qui retourne la valeur de l'argument arreter_jeu 
                Argument: une classe Menu
                Return: True ou False
        '''
        
        return self.__arreter_jeu


