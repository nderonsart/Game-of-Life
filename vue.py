# Module vue du Jeu de le vie réalisé par Nicolas Deronsart


import jeu_de_la_vie
import menu
import tkinter


class VueJeu:
    ''' Classe qui définie et met en place l'interface graphique du jeu de la vie '''
    
    def __init__(self,lig=15,col=25):
        ''' Constructeur de la classe VueJeu
                Argument: une classe VueJeu et deux entiers lig et col
                Return:
        '''
        
        assert lig>0 and col>0
        
        
        self.__lig=lig
        self.__col=col
        self.__jeu=jeu_de_la_vie.Jeu(self.__lig,self.__col)
        
        self.__vitesse=600
        
        
        self.__fenetre=tkinter.Tk()
        self.__fenetre.title('Le Jeu de la Vie')
                
        
        
        self.__images=[tkinter.PhotoImage(file='img/mort.gif'),tkinter.PhotoImage(file='img/vivant.gif')]
        self.__cases=[]
        for i in range(self.__lig):
            self.__cases.append([])
            for j in range(self.__col):
                if self.__jeu.get_elt(i,j)=='-':
                    self.__cases[i].append(tkinter.Button(self.__fenetre,image=self.__images[0],command=self.creer_commande_changement_etat(i,j)))
                    self.__cases[i][j].grid(row=i,column=j)
                else:
                    self.__cases[i].append(tkinter.Button(self.__fenetre,image=self.__images[1],command=self.creer_commande_changement_etat(i,j)))
                    self.__cases[i][j].grid(row=i,column=j)
        
        
        
        image_logo=tkinter.PhotoImage(file='img/logo.gif')
        tkinter.Label(self.__fenetre,image=image_logo).grid(row=0,column=self.__col)
        
        
        tkinter.Label(self.__fenetre,text='',width=15,font=200).grid(row=1,column=self.__col)
        
        self.__etape=0
        tkinter.Label(self.__fenetre,text='Etape '+str(self.__etape),width=15,font=200).grid(row=2,column=self.__col)
        
        
        self.__arreter=False
        image_start=tkinter.PhotoImage(file='img/start.gif')
        tkinter.Button(self.__fenetre,image=image_start,command=self.start).grid(row=4,column=self.__col)
        
        image_stop=tkinter.PhotoImage(file='img/stop.gif')
        tkinter.Button(self.__fenetre,image=image_stop,command=self.stop).grid(row=4,column=self.__col+1)
        
        
        image_reset=tkinter.PhotoImage(file='img/reset.gif')
        tkinter.Button(self.__fenetre,image=image_reset,command=self.reset).grid(row=6,column=self.__col)
        
        
        image_alea=tkinter.PhotoImage(file='img/alea.gif')
        tkinter.Button(self.__fenetre,image=image_alea,command=self.alea).grid(row=8,column=self.__col)
        
        
        image_moins=tkinter.PhotoImage(file='img/moins.gif')
        tkinter.Button(self.__fenetre,image=image_moins,command=self.dim_vitesse).grid(row=10,column=self.__col)
        
        tkinter.Label(self.__fenetre,text='Vitesse : '+str(110-self.__vitesse//10)+'%').grid(row=11,column=self.__col)
        
        image_plus=tkinter.PhotoImage(file='img/plus.gif')
        tkinter.Button(self.__fenetre,image=image_plus,command=self.aug_vitesse).grid(row=12,column=self.__col)
        
        
        image_menu=tkinter.PhotoImage(file='img/menu.gif')
        tkinter.Button(self.__fenetre,image=image_menu,command=self.retour_menu).grid(row=14,column=self.__col)
        
        image_quitter=tkinter.PhotoImage(file='img/exit.gif')
        tkinter.Button(self.__fenetre,image=image_quitter,command=self.__fenetre.destroy).grid(row=14,column=self.__col+1)
        
        
        
        self.__fenetre.mainloop()
    
    
    def redessine(self):
        ''' Méthode qui redessine la grille
                Argument: une classe redessine
                Return:
        '''
        
        for i in range(self.__lig):
            for j in range(self.__col):
                if self.__jeu.get_elt(i,j)=='-':
                    self.__cases[i][j]['image']=self.__images[0]
                else:
                    self.__cases[i][j]['image']=self.__images[1]
        
        tkinter.Label(self.__fenetre,text='Etape '+str(self.__etape),width=15,font=200).grid(row=2,column=self.__col)
        tkinter.Label(self.__fenetre,text='',width=15,font=200).grid(row=1,column=self.__col)
        
    
    def creer_commande_changement_etat(self,i,j):
        ''' Méthode qui retourne la fonction commande_changement_etat
                Arguments: une classe VueJeu et deux entiers i et j
                Return: une fonctionn
        '''
        
        def commande_changement_etat():
            ''' Fonction qui change l'état de la case aux coordonnées [i][j] '''
            
            self.__jeu.change_etat(i,j)
            self.redessine()
        
        return commande_changement_etat
    
    
    def start(self):
        ''' Méthode qui active l'état en cours du dévellopement de la grille
                Argument: une classe VueJeu
                Return:
        '''
        
        if self.__jeu.est_vide():
            self.__arreter=True
            self.__etape=0
        elif self.__jeu.est_stable():
            tkinter.Label(self.__fenetre,text='Structure Stable',width=15,font=200).grid(row=1,column=self.__col)
            self.__arreter=True
        
        if not self.__arreter:
            self.__jeu.etape_suivante()
            self.__etape+=1
            self.redessine()
            self.__fenetre.after(self.__vitesse,self.start)
        else:
            self.__arreter=False
            

    def stop(self):
        ''' Méthode qui active l'état arrêter le développement de la grille
                Argument: une classe VueJeu
                Return: 
        '''
        
        self.__arreter=True
        
        
    def reset(self):
        ''' Méthode qui remet la grille à 0
                Argument: une classe VueJeu
                Return: 
        '''
        
        self.__jeu.reset_grille()
        self.__etape=0
        
        self.redessine()
    
    
    def alea(self):
        ''' Méthode qui rend aléatoirement un quart des cellules vivantes sur la grille
                Argument: une classe VueJeu
                Return:
        '''
        
        self.__jeu.place_cell_v_alea(self.__jeu.taille()//4)
        self.redessine()
    
    
    def dim_vitesse(self):
        ''' Méthode qui augmente le temps entre chaque étape
                Argument: une classe VueJeu
                Return:
        '''
        
        if self.__vitesse<1000:
            self.__vitesse+=100
        
        tkinter.Label(self.__fenetre,text='Vitesse : '+str(110-self.__vitesse//10)+'%').grid(row=11,column=self.__col)
    
    
    def aug_vitesse(self):
        ''' Méthode qui diminue le temps entre chaque étape
                Argument: une classe VueJeu
                Return:
        '''
        
        if self.__vitesse>100:
            self.__vitesse-=100
        
        tkinter.Label(self.__fenetre,text='Vitesse : '+str(110-self.__vitesse//10)+'%').grid(row=11,column=self.__col)
    
    
    def retour_menu(self):
        ''' Méthode qui ferme la fenêtre et reviens au menu pour sélectionner une nouvelle taille pour la grille
                Argument: une classe VueJeu
                Return:
        '''
        
        self.__fenetre.destroy()
        m=menu.Menu()
        if not m.arreter_jeu():
            VueJeu(m.lig(),m.col())
        


if __name__=='__main__':
    
    m=menu.Menu()
    if not m.arreter_jeu():
        VueJeu(m.lig(),m.col())


