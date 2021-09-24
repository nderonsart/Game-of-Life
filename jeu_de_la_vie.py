# Module jeu_de_la_vie du Jeu de le vie réalisé par Nicolas Deronsart


from random import randint



class Jeu:
    ''' Classe qui définie un jeu de la vie '''
    
    def __init__(self,lig,col,grille=[]):
        ''' Constructeur de la classe Jeu
                Arguments: une classe Jeu et deux entiers lig et col
                Return:
        '''
        
        assert lig>0 and col>0
        
        self.__lig=lig
        self.__col=col
        
        if grille!=[]:
            self.__grille=grille
            
        else:
            self.__grille=[]
        
            for i in range(self.__lig):
                self.__grille.append([])
                for j in range(self.__col):
                    self.__grille[i].append('-')
        
        self.__etape=0
    
    
    def affiche_grille(self):
        ''' Méthode qui affiche la grille
                Argument: une classe Jeu
                Return:
        '''
        
        for i in range(self.__lig):                
            aff='| '
            for j in range(self.__col):
                aff+=self.__grille[i][j]+' | '
            print(aff)
    
    
    def get_adj(self,l,c):
        ''' Méthode qui retourne le nombre de cellule vivante adjacente de la cellule dont on a entré les coordonnées
                Arguments: une classe Vie et deux entiers l et c
                Return: un entier
        '''
        
        assert l>=0 and l<self.__lig and c>=0 and c<self.__col
        
        cpt=0
        
        for i in range(-1,2):
            for j in range(-1,2):
                if i==0 and j==0:
                    pass
                else:
                    if l+i>=0 and l+i<self.__lig and c+j>=0 and c+j<self.__col:
                        if self.__grille[l+i][c+j]=='*':
                            cpt+=1
        
        return cpt
    
    
    def etape_suivante(self):
        ''' Méthode qui applique l'étape suivante selon la grille actuelle
                Argument: une classe Jeu
                Return: 
        '''
        
        self.__etape+=1
        
        suite=[]
        for i in range(self.__lig):
            suite.append([])
            for j in range(self.__col):
                suite[i].append(self.__grille[i][j])

        
        for i in range(self.__lig):
            for j in range(self.__col):
                
                if self.__grille[i][j]=='-':
                    if self.get_adj(i,j)==3:
                        suite[i][j]='*'
                
                elif self.__grille[i][j]=='*':
                    if self.get_adj(i,j)<2 or self.get_adj(i,j)>3:
                        suite[i][j]='-'
        
        self.__grille=suite
    
    
    def taille(self):
        ''' Méthode qui retourne le nombre de case dans la grille
                Argument: une classe jeu
                Return: un entier
        '''
        
        return self.__lig*self.__col
        
    
    def place_cell_v_alea(self,n):
        ''' Méthode qui ajoute des cellules vivantes aléatoirement dans la grille
                Arguments: une classe Jeu et un entier n
                Return:
        '''
        
        assert n<=self.taille()
        
        if n>=self.taille()-self.nbr_cell_v():
            n=self.taille()-self.nbr_cell_v()
        
        for num in range(n):
            i=randint(0,self.__lig-1)
            j=randint(0,self.__col-1)
            while (self.__grille[i][j]=='*'):
                i=randint(0,self.__lig-1)
                j=randint(0,self.__col-1)
            self.__grille[i][j]='*'
    
    
    def nbr_cell_v(self):
        ''' Méthode qui retourne le nombre de cellules vivantes dans la grille
                Argument: une classe Jeu
                Return: un entier
        '''
        
        cpt=0
        
        for i in range(self.__lig):
            for j in range(self.__col):
                if self.__grille[i][j]=='*':
                    cpt+=1
        
        return cpt
    
    
    def est_vide(self):
        ''' Méthode qui indique si la grille ne contient que des cellules mortes
                Argument: une classe Jeu
                Return: True ou False
        '''
        
        return self.nbr_cell_v()==0
    
    
    def num_etape(self):
        ''' Méthode qui retourne le numéro de l'étape en cours
                Argument: une classe Jeu
                Return: un entier
        '''
        
        return self.__etape
    
    
    def get_elt(self,l,c):
        ''' Méthode qui retourne la valeur de l'élément à la position [l][c] dans la grille
                Arguments: une classe Jeu et deux entiers l et c
                Return: une chaîne de caractère
        '''
        
        return self.__grille[l][c]
    
    
    def change_etat(self,l,c):
        ''' Méthode qui change l'état de la case aux coordonnées [i][j]
                Arguments: une classe Jeu et deux entiers l et c
                Return:
        '''
        
        if self.__grille[l][c]=='-':
            self.__grille[l][c]='*'
        else:
            self.__grille[l][c]='-'
    
    
    def reset_grille(self):
        ''' Méthode qui met toutes les cases de la grille en état morte
                Argument: une classe Jeu
                Return:
        '''
        
        for i in range(self.__lig):
            for j in range(self.__col):
                self.__grille[i][j]='-'
    
    
    def est_stable(self):
        ''' Méthode qui indique si la grille est stable
                Argument: une classe Jeu
                Return:
        '''
        
        grille_suiv=[]
        for i in range(self.__lig):
            grille_suiv.append([])
            for j in range(self.__col):
                grille_suiv[i].append(self.__grille[i][j])

        for i in range(self.__lig):
            for j in range(self.__col):
                if self.__grille[i][j]=='-':
                    if self.get_adj(i,j)==3:
                        grille_suiv[i][j]='*'
                
                elif self.__grille[i][j]=='*':
                    if self.get_adj(i,j)<2 or self.get_adj(i,j)>3:
                        grille_suiv[i][j]='-'
        
        return grille_suiv==self.__grille
        


def modele_stable(pos):
    ''' Fonction qui retourne un modèle stable du jeu de la vie
            Argument: un entier pos
            Return: une classe Jeu
    '''
    
    grilles_stables=[]
    
    bloc=[['-','-','-','-'],
          ['-','*','*','-'],
          ['-','*','*','-'],
          ['-','-','-','-']]
    grilles_stables.append(bloc)
    
    tube=[['-','-','-','-','-'],
          ['-','-','*','-','-'],
          ['-','*','-','*','-'],
          ['-','-','*','-','-'],
          ['-','-','-','-','-']]
    grilles_stables.append(tube)
    
    navire=[['-','-','-','-','-'],
            ['-','*','*','-','-'],
            ['-','*','-','*','-'],
            ['-','-','*','*','-'],
            ['-','-','-','-','-']]
    grilles_stables.append(navire)
    
    vaisseau=[['-','-','-','-','-','-'],
              ['-','-','-','*','*','-'],
              ['-','*','-','-','*','-'],
              ['-','*','*','-','-','-'],
              ['-','-','-','-','-','-']]
    grilles_stables.append(vaisseau)
    
    ruche=[['-','-','-','-','-'],
           ['-','-','*','-','-'],
           ['-','*','-','*','-'],
           ['-','*','-','*','-'],
           ['-','-','*','-','-'],
           ['-','-','-','-','-']]
    grilles_stables.append(ruche)
    
    return Jeu(len(grilles_stables[pos-1]),len(grilles_stables[pos-1][0]),grilles_stables[pos-1])



if __name__=='__main__' :
    
    print('_________________________________')
    print('\nBienvenue dans le jeu de la vie !\n')
    
    mode_jeu=input('\nVoulez vous jouer avec une grille aléatoire ou avec une structure stable ? ')
    
    
    if mode_jeu=='a' or mode_jeu=='alea' or mode_jeu=='aleatoire':
        lig=int(input('\nMerci d\'entrer le nombre de ligne pour le jeu : '))
        col=int(input('Merci d\'entrer le nombre de colonne pour le jeu : '))
        vie=Jeu(lig,col)
        
        n=int(input('\nCombien voulez-vous de cellules vivantes dans votre jeu ? '))
        while n>vie.taille():
            n=int(input('Choisissez un plus petit nombre, vous ne pouvez pas dépasser la taille de la grille : '))
        vie.place_cell_v_alea(n)
    
    
    else:
        print('\nChoisissez le modèle que vous voulez voir évoluer :\n')
        print('(1) Le bloc')
        print('(2) Le tube')
        print('(3) Le navire')
        print('(4) Le vaisseau')
        print('(5) La ruche')
        n=int(input('Quel numéro de modèle choisissez vous ? '))
        while n<=0 or n>5:
            n=int(input('Veuillez choisir un numero entre 1 et 5 : '))
        
        vie=modele_stable(n)
        
    
    
    print('\n\nVoici la situation initiale :\n')
    vie.affiche_grille()
    
    choix=input('\n\nVoulez vous voir l\'évolution de ce modèle ? ')
    while (choix=='oui' or choix=='y') and not vie.est_vide():
        print('\n_________________________________')
        print('\nVoici l\'étape '+str(vie.num_etape()+1)+' :\n')
        
        vie.etape_suivante()
        vie.affiche_grille()
        
        print('\nIl y a actuellement '+str(vie.nbr_cell_v())+' cellules vivantes dans cette étape')
        
        if not vie.est_vide():
            choix=input('\n\nVoulez vous voir l\'évolution de ce modèle ? ')
    
    if vie.est_vide():
        print('Votre grille étant vide, il n\'y a plus d\'évolution possible...')


