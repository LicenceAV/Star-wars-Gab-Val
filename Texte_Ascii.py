# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:59:43 2020

@author: owlyn
"""
         
import time
import random
import os
import colorama
from colorama import Fore, Style



# Banque de texte et de dessin pour le jeu
colorama.init()



temps = 10

def clear():                                        #Clear du terminal extérieur
    os.system( 'cls' )
    
character = 'azertyuiopqsdfghjklmwxcvbn'
replay = 'yes'
        
def memorigame(difficulty):                         #Jeu du mémory
    
    
    replay = 'yes'
    ennemi = difficulty
    
    while replay == 'yes' or replay == 'oui' :                         
        
        lst = []                                                
        for i in range(difficulty):                                 #difficulty représente le nombre de lettre à deviner
            i = character[random.choice(range(len(character)))]     #une liste est créée avec des lettres prises au hasard dans 'character'
            lst.append(i)
        
        
        clear()
        print("{: ^100}".format("Le jeu du memory : "))
        time.sleep(5)
        
        for j in range(difficulty):                     #mise en forme du jeu afin que chaque lettre soit affiché décalée de 25 caractères par rapport à la précédente et de 1 ligne par rapport à la précédente.
            x = 25*j
            clear()
            print('\n'*j, ' '*x, lst[j])
            time.sleep(1)
            clear()
            time.sleep(1)
        
        answer = input('Restituer la suite de caractère de en minuscule et tout attaché :')
             
        ennemi = difficulty
        
        if answer == "".join(lst) or answer == "Trivial":       #si la réponse est égale au 'join' de la liste choisie plus haut, alors la fonction return ennemi et donc ici ennemi = 0 car win
            print("you win")
            time.sleep(2)
            print()
            ennemi = 0
        else:                                                   #si la réponse n'est pas entièrement bonne, la réponsé est transformée en liste et le programme compte le nombre de lettres à la bonne position
            print("You loose")
            lst2 = []
            for i in range(difficulty):                         
                lst2.append(answer[i])
                
            for i in range(difficulty):
                    if lst[i] == lst2[i]:
                        ennemi -= 1                          #à chaque bonne lettre, le joueur affronte 1 ennemi de moins (ennemi = difficulty)
            print("Votre infiltratrion n'est pas des plus discrètes et vous affrontez {} ennemis".format(ennemi))
        
        time.sleep(2)
        
        replay = input('Voulez vous rejouer ?')
    return ennemi    
        
class Histoire:                         #la classe Histoire contient toutes les méthodes que l'on appel au fur et à mesure du cycle
                                        #Chaque méthode de cette classe est organisée pour qu'on trouve en premier lieu le texte utilisé par la méthode, puis son activation
    def __init__(self):                 #L'attibut space permettra de séparer les textes entre eux
        self.space = '\n'+100*'='+'\n'
        
        
    def level(self):                    #Début du jeu, Choix de la difficulté
        
        self.settings = """
        
Afin de profiter au mieux du jeu, ouvrez le dans une console externe (Fond noir) en plein écran (4K minimum)""" 
 
        self.level = """
        
Choisir le niveau de difficulté : 
    
    
3) Droïde (facile, l'ennemi a 33% de chance de prendre la bonne décision)
    
2) Poe Dameron (moyen, 66% d'être intelligent, et leurs stats sont supérieures de 10%)
    
1) Dark Maul [la bonne moitiée] (difficile, l'ennemi ne vous fera pas de cadeaux et il est 20% plus puissant) 
    
Attention, nous n'avons pas eu le temps d'équilibrer toutes les classes
De ce fait, le jeu est largement faisable en difficulté facile.
Nous vous conseillons de prendre un Mandalorien Jedi avec une tunique et d'utiliser impérativement les pouvoirs de la force.


"""
     
        print(self.space, self.settings)  #activation du texte
        time.sleep(temps)                   #On utilise le module time afin d'avoir assez de temps pour lire, le temps peut être modifié L21
        print(self.space, self.level)
        
    def Synopsis(self):
        
        self.preSynopsis = Fore.CYAN + Style.BRIGHT + """ 
Il y a bien longtemps, dans une galaxie fort lointaine... """

        self.Synopsis = Fore.YELLOW + """
     
                  .              .       .                    .      .
.        .               .       .     .            .
   .           .        .                     .        .            .
             .               .    .          .              .   .         .
               _________________      ____         __________
 .       .    /                 |    /    \    .  |          \    .      .
     .       /    ______   _____| . /      \      |    ___    |     .     .
             \    \    |   |       /   /\   \     |   |___>   | 
           .  \    \   |   |      /   /__\   \  . |         _/               .
 .     ________>    |  |   | .   /            \   |   |\    \_______    .
      |            /   |   |    /    ______    \  |   | \           |
      |___________/    |___|   /____/      \____\ |___|  \__________|    .
  .     ____    __  . _____   ____      .  __________   .  _________
       \    \  /  \  /    /  /    \       |          \    /         |      .
        \    \/    \/    /  /      \      |    ___    |  /    ______|  .
         \              /  /   /\   \ .   |   |___>   |  \    \     .      .
   .      \            /  /   /__\   \    |         _/.   \    \  .     .
           \    /\    /  /            \   |   |\    \______>    |   .
            \  /  \  /  /    ______    \  |   | \              /         ;.
 .       .   \/    \/  /____/      \____\ |___|  \____________/  LS
                               .                                        .
     .                           .         .               .                 .
                .                                   .            .

                  Cela fait bien longtemps que l'univers a   .        .     .
                 oublié la paix, l'Empire détient le pouvoir    .  .
     .       .  et ne cesse de coloniser tour à tour chacunes         .
.        .     des planètes sur lequel il pose ses griffes.    .            .
   .           A sa tête, le maléfique Dark LAUM, retranché sur   .      .
             le vaisseau Elysia, commande chaque attaque afin de
         .  réduire au mieux l'existence des rebelles.               .   .
   .       Cela fait bien longtemps que cette guerre dure, et Elysia       .  .
.      .  est une menace considérable face aux rebelles. Les Jedi ont    .
         disparu depuis bien longtemps et seul quelques escadrons de          .
    .   chasseurs rebelles s'opposent encore à l'empire.               .    .
.         Cependant, l'espoir n'est pas vain, le pouvoir mystique de la     .
    . force n'a jamais disparu, et le destin tragique de l'univers serait
     en passe de changer.                                                   .
       Cette galaxie est composée d'inombrables aliens,  monstres bizarres,     .
 . étranges droïdes, puissantes armes, grands héros, et terrifiants oppresseurs     . 
 C'est une galaxie aux mondes fantastiques, aux appareils magiques, aux conflits   .
terribles mais dont l'espoir est immortel.     
 
 

        """ + Fore.RESET 
        print(self.preSynopsis)             #Activation du texte.
        time.sleep(temps/2)
        print(self.Synopsis)
        
    def Introduction(self):
        
        self.introduction = """
        
          .                      ,/~'| ---_____
     __                          ;_'/   ___              --~~LL~~--
   :/=|=L==--{-                                             /~~\-
   /=\|_                   ----------   __________          \__/-
__;-----)                             _=~~~_||_~~~~=_    --__YY__--
~~|~~~~~~|------_______                   /\__/\_
__|______|------~~~~~~~       ------     ( (__) )
~~;-----)                                 \/__\/~
   \=/|~                  -------    ~=____ || ____=~        _~~=_
   :\=|==--{-                            ~~~~~~~~~~         / /=  ~~= --
     ~~                                                     | , ;` '|--
  .                  .             -)------+====+       .
                           -)----====    ,'   ,'   .                 .
              .                  `.  `.,;___,'                .
                                   `, |____l_\    .                 .
         .           _,.....------c==]""______ |,,,,,,.....____ _    .
    .      .       "-:______________  |____l_|]'''''''''''       .     .
                                  ,'"",'.   `.
         .                 -)-----====   `.   `.              LS
                     .            -)-------+====+       .            . """ + """       
    
        
*Bruits de chocs métalliques

*Explosions sur votre droite et votre gauche

*Les alarmes et les flashs lumineux signalant les derniers instants de vôtre vaisseau retentissent

*Vous rentrez dans l'attraction gravitationnelle de la planète Dagobah et vous n'êtes plus qu'à quelques kilomètres du sol et des marécages putréfiés de cet astre.

*Bien que vous puissiez vous réjouir, vous êtes néanmoins toujours poursuivi par l'Empire et votre vaisseau est en piteux état...

Souhaitez vous :
    
a) Vous poser
b) Voler vers une zone plus sécurisé ?
"""

        time.sleep(temps*2)
        print(self.introduction)



    def IntroductionPt2(self, answer):
     
        self.Crash = """ 
        
*Votre vaisseau est dans ses derniers instants de vie

*Son nez pointe de plus en plus vers le sol et vous vous écrasez parmis les marécages et les arbres pestiférés de Dagobah.

*....

*Par miracle, vous n'êtes pas mort, seulement blessé (-30 pts de vie), il semblerait même que l'on vous ait sauvé.

*Vous êtes étalé par terre, dans une hutte.
"""
        self.Atterissage = """
        
*Votre vaisseau n'est bientot plus qu'un vulgaire tas de féraille, il était urgent de se poser.

*De la fumée noire vous rend visible cependant, elle ne provient pas de votre vaisseau mais de huttes installées dans les marécages

*Vous avez désespéremment besoin d'aide et de sécurité, vous décidez donc de vous y poser. (+ 5% de Chance)"""

        self.Yoda = """ 
         
*Cela va bientôt faire 1 mois que vous vous cachez

*Une forme apparait dans les feuillages """ + Fore.GREEN +"""

Forme Sombre : "Vous cacher inutile il est, ni d'avoir peur, aventurier. Sans entrainement pas longtemps vous ne tiendrez." """ + Fore.RESET + """

*Sortant de la pénombre, vous remarquez le maitre des maitres : Yoda. """ 

        self.ApparitionYoda = Fore.GREEN + """

                   ..   :.         ..                      
                  .-:    :-=-..       ..                    
                .=:         :..                             
*#=            -*=---==:--       :..:+-.:.                  
@@@*:         +@@@@#=+**+=+=:--: .:::.::-. :                
%%%@@%#-.   :%@%@@%%%@@@#... .      .=.     -.              
=@+@@@@@@#-:=*+=-:.:-=###=   -=*=+*=:.#*..:*....            
 #@+@@@@@@@@%#+-      .  :.-#%@@%#%@@+*@@@@@++#+            
 .@#*@@@@@@@@@@@#-   .: .-##@#+:---=%@@@#*@@@@@@+           
  :%@*##%@@@@@@@@@*-. -=--**=--==*#*#@@#:.%@+-=%#     -*+:  
   .#@@*-+@@@@@@@@@#: .==++*#%@* -@%**#=::%%++==:  .=%@@%@%-
     -%@@+=#@@@@@@*+-.  :::::::-*+++:  .  =@++@@=#%@@*+=-:-:
       -%@@+-+##++#@@#**--++:.   .:: --:=:.**=#*-+@%-::     
         -#@#+++*%@@@@@@*%@#*+-.    =*%@@@@-*@@%: - ..      
          :@@@@@@@@@@@@@@@@@@@@@%+=#= .+@%-.-+%*   :-       
          :@@@@@@@@@@@@*=+++++*####:    .   -*--- .-        
           *@@@@@@@@@@@%##*===+.  .+=..      ##@% .         
           -@@@@@@@@@@@@@@@@@#=  .-=====+==-.+@#:           
           =@@@@*+@@@@@%=...:-         .::::.@@:            
          :%@@@@+.+@@@@#:-=#*.              *@:             
          +*=@@@:  *@@@@@@@=      .=-     .+*.              
           :-+@@+   :++++-.       #@@%###*=:                
            ..-@@+.            .--%@@@@@*.                  
               :%@=.    :  ..  ..+++++=:                    
                .+:  ..  :: .-:--                           
                   :-..:: ::--=*@%#+-                       
                   .+%%@#=..::-#@@##*                       
                     :#@@@#. =%@@@%#:                       
                       -*@@@@@@@@@+                         
                         .-==#+-:.

Yoda : " Attendre il ne sert à rien, vous trouvera l'Empire tôt out tard... Entrainer il vous faut si vous échapper vous voulez..." """
    
        self.Me = """
Yoda : - " Mais avant dites moi, qui être vous ? " """ + Fore.RESET + """

* Selectionnez la race, la classe, ainsi que l'équipement que vous voulez arborer pendant tout le jeu
"""
        
        if answer == 'a' :      #si le joueur fait le choix 'a', alors le texte de l'attérissage est déclenché

            print(self.space, self.Atterissage)
            
        else :                  #Sinon, le texte du crash est déclenché
            print(self.space, self.Crash)
            
        time.sleep(temps)
        print(self.space, self.Yoda)
        time.sleep(temps)
        print(self.ApparitionYoda)
        time.sleep(temps)
        print(self.Me)
        time.sleep(temps/2)    
    
    
    def introductionJoueur(self, name):
        
        self.personnage = '{} : - " Je suis {} ! " \n'
        
        self.finMe = Fore.GREEN + """
 Yoda : - "Vrai il est, votre arrivée j'attendais... Maintenant, vous entrainer il faut. Mes conseils, écouter vous allez ." """ + Fore.RESET +"""

* Yoda vous tend le livre ancestral du combat ancestral du Jedi Ancestral.

* A ce même moment, des chasseurs de prime à la solde de l'Empire vous ont retrouvé.
""" + Fore.GREEN + """
Yoda : - "Sur ces bandits, mesurer vos compétences, vous devez !" """ + Fore.RESET

        self.Didacticiel = """ 
 
- Les combats se presentent sous un système de tour par tour. Vous avez une action à chaque tour.

- Un combat se termine lorsqu'un des joueurs n'a plus de vie, le combat boucle au début de la vague si vous perdez.

- En fonction de la race et de la classe choisie, votre personnage sera plus ou moins orienté vers le coté clair ou obscur.

- Il est possible de récupérer l'équipement d'un ennemi une fois ce dernier à terrea. 1/2 chance de dropper l'armure ou l'arme.

- La force se régénère à hauteur de 5 points chaque tour.

- Vous pouvez à tout moment voir pendant le combat vos stats en appelant 'stats'.

- Vous pouvez à tout moment voir pendant le combat voir la liste des attaques possibles en appelant 'help'.

- Nous vous conseillons très fortement d'appeler 'help' dès votre premier combat.

- TOUS les combats ainsi que les énigmes peuvent êtres passées avec 'Trivial' AVEC UNE MAJUSCULE AU 'T'
    
"""
        

        print(self.personnage.format(name, name), self.finMe)       #Utilisation du nom du joueur rentré plus tôt dans la variable.
        time.sleep(temps)
        print("{:-^100}".format("Didacticiel :"))   #mis en page du didacticiel
        print(self.Didacticiel)
        
    def FinYoda(self):
        
        self.FinYoda = Fore.RESET + Style.BRIGHT +  """
        
"""+ Fore.GREEN + """Yoda : "Vous battre vous savez, cependant, l'esprit aussi, pour survivre, maitriser, il faut savoir  .
Ces trois énigmes vous répondrez et le chemin vous trouverez..." """+ Fore.RESET +""" """

        Q1 = """ 
Celle d'une cellule,
N’est pas celle blindée
C’est une opération,
Qui aide à mieux régner
Qui est-elle ?    """
      
        Q2 = """
Sous les pieds, ou dans la main,
Elle est double pour l'académicien.
En abondance dans les prés,
De loin, vous l'entendez.
Qui est-elle ? """

        Q3 = """
Parfois loin de la réalité,
Une image elle peut accompagner.
La réponse ici trouvée,
Vous permettra peut-être d’y entrer.
Qui est-elle ? """

        self.YodaFin = """ 
    
"""+ Fore.GREEN + """Yoda : "Non déterminée la fin de l'Empire est, et dans l'unité il sombrera, la fin de l'empire seul vous ne provoquerez pas... 

Trouver les plans d'Elysia il faut, reformer la Rébellion et détruire Elysia. Jarjar vous orienter il saura , le trouvez vous devez."

"""+ Fore.RESET +""" """
        self.FindJarjar = """ 

* Jarjar se trouve sur Naboo

* Vous remontez donc dans votre vaisseau en direction de la planète de feu Amidala

...

* Vous arrivez bientot dans le champs gravitationnel de la planète

* Vous appercevez que la lueur au loin n'est pas un astre mais bien un vaisseau qui fonce sur vous """

        self.NabooStarfighter = Fore.LIGHTYELLOW_EX + """
        
        
                                                                                .    
                                                                             .::     
                                                                           .::       
                                                                         .::         
                                                                      .::.           
                                                                   ...:.             
                                                                .::.:.               
                                                            ..:==:::.                
                                  ..                    =#***=--=-:-:                  
                             ...                       :=***=-=--:.                   
                         .::--.                     .-+===-:---.                     
                     ..:-=+=:                     .=*#%=:----:                       
                  .::---===.                .. .:=#%##+-:::-.                        
                ..-++==--:                ....=+#%%#+:--::-.                         
           ...:-+****+=:               ...:::==*%%*-..:::-.                          
         .::-+*##*+-..:::..         ....-=--+=+*+=::---::-                           
      .:-=+*##*++-.    ....:.    ....:-=-. =*++=---=-::.:-:                          
      :+**#*=-.  .....   .::::::::::-::..:===-:::---:..:-=:                          
    .=**#*:.      ::..... ..--:::-+-..:-=+==-::--==:.:--=:                           
   :+=:...         :::...   ..:--..-=++++=----====-:--==:                            
                   .-::..  .:==:  .-==**+======--::---=.                  :.         
                    ::::..:--.  .:--+***+++++=--:::-=-                  .:.          
                     ------.  ..:-+##*****+===--:---.                  -:            
                     :---.   .:-+#%##**+===---::--:                  :-              
                     .:    .:-+###**+=---:----::::               ..:-:               
                      .  .:-+###*++=---::::.::::::::.         :::-=-:                
                       .:=+##%#*++==---:::::...:::---:.    .:::-==-:                 
                          .:-=====+===-::::......:::----:.:---===--:                 
                                   .::-----::::::::::----::-=++==-:                  
                                         ..::------=----::-=**+=-.                   
                                               ..:-=--:::=***++:                     
                                                   :-::=+***+=.                      
                                                  --:-+****+:                        
                                                .::-=*****-                          
                                              .==:-****#+.                           
                                              :=+*#*#%*:                             
                                              :-=*%%#=                               
                                             -+***+=                                 
                                            -#*=:                                    
                                             .     """ + Fore.RESET + """   
                                                
                                   
Souhaitez vous : 
    
a) Ne rien faire
    
b) L'abattre
                                             
                                             """






        print(self.space, self.FinYoda)         #Jeu d'énigme, tant que le joueur n'a pas trouvé la réponse, l'énigme est posée.
        answer1 = input(Q1)

        while answer1 != 'La division' and answer1 != 'la division' and answer1 != 'Division' and answer1 != 'division' and answer1 != 'Trivial':
            print("FAUX")
            answer1 = input(Q1)
        
        answer2 = input(Q2)
        
        while answer2 != 'la corne' and answer2 != 'La corne' and answer2 != 'corne' and answer2 != 'Corne'and answer2 != 'Trivial':
            print("FAUX")
            answer2 = input(Q2)
            
        answer3 = input(Q3)
        
        while answer3 not in ('La légende', 'la légende', 'légende', 'Légende', "la legende", "Legende", "legende", "Trivial") :
            print("FAUX")
            answer3 = input(Q3)

        print(self.space, self.YodaFin)
        time.sleep(temps)
        print(self.space, self.FindJarjar)
        time.sleep(temps)
        print(self.space, self.NabooStarfighter)
        
    def Naboo(self, choice, name):
        
        self.NabooChoiceA = """

* Le vaisseau vous frôle de peu, c'était juste un Starfighter de la garde impériale de Naboo en patrouille

* Vous appervecez un port de libre

* Vous attérissez dans la ville, proche du palais Royale """      

        self.NabooChoiceB = """ 

* Vous tirez un coup de canon plasma


...
* piou
...

* La vaisseau inconnu est touché à l'aile et commence à s'écraser vers Naboo

* Vous appercevez un port et décidez de vous y poser

* Des gardes entourent votre vaisseau, vous n'auriez pas dû abattre l'un des leurs
"""

        
        self.Jarjar = """
        
* Vous vous empressez d'aller trouver Jarjar

* Vous le trouvez dans une ruelle, entouré de 2 super-droïdes de combat et un droïdeka

* ils semblent questionner Jarjar

* ils vous repèrent et décident de vous attaquer.
"""

        self.Jarjar2 = Fore.YELLOW + Style.BRIGHT + """
        
                      +*--=.      .==-*+                     
                   :*+:::-*.    .*-::-**:     Jarjar = - " Ay-yee-yee! Wha! You saved my again !            
                   =#.=::--*    *-::-=.#=                 Les druides voulaient mes ren-saignements.
                   *:=---:-#    #-:---=-*                  Mais Mesa sait que c'est {} qui doit l'avoir.
                  .#+. ** =%+==+%= ** .+#.                  Les plans de Elysia sont sur HOT mais attention
                   +---:-**#.  .##*--=--+                   Mesa sait que planète pas chaude !"
                   *=:.:-::*   .*::-:::+*                   
                 =+=--..:--     .=-:: -==*-                 
              .++-    :::.        .:-:.  .=+=.              
            :*+:     .:              :.     -++:            
          :*+.     -=::=:          :=::=-     :+*.          
         =*:      +=.***=.         =**+.=+      -*-         
        =*        .==*::-:        :-:-*-=:        #=        
        #   +*+:    .                 ..    .+++  .#        
       -%   . .+:                          .+:..   %:       
      =+*+      *:                        .*.     =**-      
     *+  #+      +=.                     -*.     =#  ++     
   .#:  -:++      :%*=-:...        ..:-+#-      +*--  -*.   
  :*. :-:  +#.     -*.=:-*+=*++#++*=:+.*-     .#+  --: :*.  
 :#-+-.   ::.#-     +=      :  -  .   -*     :*:-:   .-=-#. 
:%##:    :-  -@= :-  *+::-----:-::--:+#  :: +#   -:    -%#%.
+=*.   .:-  .-++: -=  =+:.        .:+=  =-.*-.=.  -:.   :*=+
 =+  .--.  .-  #.  =+  .:==-:::::-=-.  ==.%:   =.  .--   += 
 #. --    --   -#   +=      .   .     =+ %=     -:   .=- .# 
-+:#:   .--     #-   =+.             ++ :#       --    -#:*-
##@-  :-:       :#    :++---:..::--+*-  *=        .:-.  =%##
+.#. -:          ++     ..:=+*+===-.    #.           :- .#:+
  #.-.            #-                    #.            :-.#  
  **+             .%.                   #:             ++*  
  *@+              -%.                  ++             +@*  
  ==*               -#:                  #.            +++  
    #.               :#-                 .*.          .# .  
    -*                 ++                 :#:         *=    
     +=                 -*:                .#.       =*     
      ++.                .*=                ++      +*      
       :*=.                *-               #-    -*-       
         :++=:             .#              *=  :=+=         
           .-=====--.       *            :+=:=++-           
                :--=====.  =+           :#+=+-.             
                      .=+-:*           :@*=.                
                        :%=            **                   
                        :.             -                    
                                                               
* Vous vous rendez sur HOTH""" + Fore.RESET

        self.HOTH = Fore.BLUE + Style.BRIGHT +  """
 :.   .                     .        .             .        ; .         .      
  :.    _____  .  _____. ____________  _____________  _____:    _____       .  
   ::. /    /\   /    /\f            ||             t/\    \   /\    \ .        
  . :::.   / /. /    / j    _____    ||____     _____l \    \ .\ \    \  .     
    `:%n  /_/__/    / /f   f\____|   ||____|   |_____/\ \    \__\_\    \ .     
 .  / ##           / /j   j'j  . |   |     |   |      .\ \              \    . 
   /    _____     / / f   f f.   |   |   . |   t .   .' \ \     _____    \ .   
  /    /\__ /    / / j   j_j_____|   |     |    l   .;   \ \    \___/\    \   .
 /    / /  /    / /  f               | .   |    |  ::     \ \    \  \ \    \  .
/____/ /. /____/ / .j________________|     |____| :*:  .   \ \____\  \ \____\ .
\____\/   \____\/   \________________|     |____f  "        \/____/   \/____/ .
 .         .   .         .              .        .          .     .   .     . """ + Fore.RESET + """
           ___      |\________/)
+         [_,_])    \ /       \|
    +    /|=T=|]     /   __  __\   +
         |\ " //     |_  9   p ]\     +
 +       ||'-'/--.  / /\ =|  \|\ \  
        /|| <\/> |\ | '._, @ @)<_)          +
   +   | |\   |  |   \.__/(_;_)    +
       |  .   H  |   |  :  '='|        +
     + |  |  _H__/  _| :      |
        \  '.__  \ /  ;      ';    +
       __'-._(_}==.'  :       ;  +       
      (___|    /-' |   :.     :
     [.-'  \   |   \   \ ;   :       +
    .-'     |  |    |  |   ":     +
   /        |==|     \  \  /  \_        +
  /         [  |      '._\_ -._ \ +
 /           \__)   __.- \ \   )\\  +
/       |        /.'      >>)    
|        \       |\     |     +
|     .'  '-.    | \    /             +
|    /     /     / /   /     +
           |    /                  +
        
* Vous vous rendez sur HOTH, malheuresement la planète est controllée par l'Empire...

* Vous allez devoir vous infiltrer afin de trouver les plans de Elysia. 


* Si vous réussissez ce test en entier, aucun ennemi n'est à combattre

* Sinon, un nombre d'ennemis proportionnel à vôtre taux d'échec vous attaquera
"""

            
        time.sleep(temps/3)   
        
        if choice  == 'a':          #la méthode est organisée de telle manière à ce qu'on rentre en argumant d'entrée, un attribut est print.
            print(self.space, self.NabooChoiceA)
            time.sleep(temps/2)
            
        elif choice == 'b':
            
            print(self.space, self.NabooChoiceB)
            time.sleep(temps/2)   
        
        elif choice == 'c':
            
            print(self.space, self.Jarjar)
            time.sleep(temps/2)

        elif choice == 'd':
            print(self.space, self.Jarjar2.format(name))
            time.sleep(temps*1.5)
            print(self.space, self.HOTH)
            time.sleep(temps*1.5)
         
            
        
    def Felucia(self):  
        
        self.Felucia = """
    
* Vous récupérez ceci : """ + Style.DIM + Fore.GREEN + """
    
    _______ _ _ _ __ __ __  _ ___ _   __  ___  __ __  __  _  ___ _ _  __ _______
%=x%=x% | |V| |_)|_ |_) | |_| |   |_) |_| (_  |_  |_) |  |_| |\| (_  %=x%=x%
~~~~~~~ | | | |  |_ | \ | | | |_  |_) | | __) |_  |   |_ | | | | __) ~~~~~~~
 LS
                 .-. .-.
               .=========.         E x t e r i o r ,   A e r i a l   V i e w
               ||.-.7.-.||         -----------------------------------------
               ||`-' `-'||
               `========='
                `-'| |`-'8               1 .............. Sensor Suite Tower
          ______   |9|   ______          2 ... Heavy Twin Turbolaser Turrets
         /     /\__| |__/\     \         3 ............. Heavy Laser Turrets
        /  \_ / /  |_|  \ \ _/  \        4 ....... TIE Fighter Launch Chutes
       /___(\\\/         \///)___\       5 ............... Heavy Blast Doors
       \____\\`==========='//____/       6 .................... Guard towers
       /     '/ .-------. \\     \       7 ........ Shuttle Landing Platform
    __/     //. \`+---+'/ .\\     \__    8 ........... AT-AT Docking Station
   /\ \    ///x`.\|___|/.'x\\\    / /\   9 ................. Connecting Ramp
  /  \ \  //`-._//|   |\\_.2'\\  / /  \  .
 /  _.-==='_____//.-=-.\\_____`===-._  \ .
 \   `-===.\-.  \ `-=1' /  .-/.===-' 3 / The pre-fabricated,  multi-function
  \  / /  \\\ \  \.===./  /4///  \ \  /  Imperial garrison base is the back-
   \/_/    \\\ | /.---.\ | ///    \_\/   bone of the  Empire's  occupational
      \     \\\|/ |_m_| \|///     /      forces. These heavily-armoured for-
       \_____\=============/_____/       tresses have  walls up to 10 meters
       /____///    ___    \\\____\       thick  to  guard   against   ground
       \   (_//\__|||||__/\\_)   /       assaults,  and  powerful  deflector
        \  /  \|,,|||||,,|/  \  /        shields  protect  them  for  air or
         \_____|  | 5 | 6|_____/         space attacks.
               `--'   `--'
               
 """ + Style.RESET_ALL + Style.BRIGHT + """              
    
* Vous avez remporté le combat, cependant bien que les plans soient à vôtre disposition, vous n'êtes rien tout seul face à l'Empire.

* Vous savez que la rebellion se cache sur Felucia, car après tout, vous en faites partie.

* Arrivé sur Felucia, l'Empire est déjà présent car il vous a retrouvé... L'Empire attaque la planète.

* Défendez la :
    """
        print(self.space, self.Felucia)
        time.sleep(temps)
    def FeluciaSpeech(self):
        
        self.fincombat = """
        
* Vous les avez vaincu, une grande partie de Felucia est libérée, tous les rebelles sont autour de vous, certains sont assis de fatigue, d'autres morts.

* Il reconnaissent votre bravoure et l'audace dont vous avez fait preuve durant cette bataille

* Convainquez les de rejoindre votre cause 

(Afin de prouver votre charisme aux soldats, répondez à ces 5 questions triviales de culture générale)"""
        
        Q1 = """
    
Donnez la bonne orthographe du mot dont la définition est : symbiotes présents chez toutes les espèces organiques de la galaxie qui maintiennent leur lien avec la Force.
Réponse a, b, c ou d.

a) Midi-chlorien 
b) Medi-chlorien
c) Medi-Khlorien
d) Méjeconpranrien
    
Votre réponse : """
            
        Q2 =   """
Pourquoi l'Empereur ne prend t'il pas l'hélicoptère ? 
Réponse a, b, c ou d.

a) Parce qu'il a peur du vide
b) Parce qu'il n'y en a pas dans Star-wars
c) Parce qu'il peut faire une surcharge IEM 
d) Parce que les pales patinent

Votre réponse : """
        
        Q3 =  """
        
Quelle est la meilleure façon de réussir son code ?
Réponse a, b, c ou d :
    
a) StackOverflow
b) C.Desjouy
c) Les tutos indiens sur youtube 
d) La force 
    
Votre réponse : """
            
        Q4 =  """
        
Comment appelle-t-on un wookie qui parle ?
Réponse a, b, c, ou d :
    
a) Un Ewook
b) Gungi
c) Tarfful
d) Un talkie-Wookie
    
    
Votre réponse : """

        Q4 = """ 
L'an dernier, mon père avait le double de mon âge. Cette année, nos deux âges s'expriment par les deux mêmes chiffres, mais écrits dans un ordre différent.

Quel est l'âge de mon père ? 
Réponse a, b, c ou d :

a) 73
b) 71
c) 75
d) 61
    
    
Votre réponse : """
    
        Q5 = """ Que doit-on mettre après cette suite de lettre ?
J - F - M - A - M - J - J - ?

Votre réponse : """

        FinFelucia = """ 
        
* Maintenant vous êtes paré pour attaquer Elysia, les rebelles sont à vos cotés et vous apportent de l'expérience.

* Vous devez maintenant attaquer Elysia, le repère de Dark LAUM """


        Elysia = """ 
        
                  _        .                          .            (           
  .          .                  .          .              .
        +.           _____  .        .        + .                    .
    .        .   ,-~"     "~-.                                +
               ,^ ___         ^. +                  .    .       .
              / .^   ^.         \         .      _ .
             Y  l  o  !          Y  .         __CL\H--.
     .       l_ `.___.'        _,[           L__/_\H' \\--_-          +
             |^~"-----------""~ ^|       +    __L_(=): ]-_ _-- -
   +       . !                   !     .     T__\ /H. //---- -       .
          .   \                 /               ~^-H--'
               ^.             .^            .      "       +.
                 "-.._____.,-" .                    .
          +           .                .   +                       .
   +          .             +                                  .
          .             .      .                                                        
                 (_)        .       .                                     .                o
  .        ____.--^.                                                                      /\           .
   .      /:  /    |                               +           .         .               |  `.
         /:  `--=--'   .                                                .                |  `.
        /: __[\==`-.___          *           . ELYSIA                              .      |    `.
       /__|\ _~~~~~~   ~~--..__            .             .                                `.     |          .
       \   \|::::|-----.....___|~--.                                 .                     |     |_.--.
        \ _\_~~~~~-----:|:::______//---...___                                           .  `.   /<= .-'              .
    .   [\  \  __  --     \       ~  \_      ~~~===------==-...____                .        |_./|_.'/))    .
        [============================================================-                      /()_.-'/ /`-.
        /         __/__   --  /__    --       /____....----''''~~~~      .                 / / _.-'\/_   `-.__
  *    /  /   ==           ____....=---='''~~~~ .                                         (./())      ~~--..__~`-o
      /____....--=-''':~~~~                      .                .                  .     | /   .            `-'
      .       ~--~         .        .                       .                              //       .   .             
                     .                                   .           .                    //
                          .                      .             +                 .       //               
        .     +              .                                       <=>                //       .           . 
                                               .                .      .               //
   .                 *                 .                *                ` -          o/
   
        
* Votre esquadron s'approche en direction d'Elysia cependant, vous appercevez déjà ses canons s'orienter dans votre direction

* Les premiers tirs commencent à retentir, vous garder tant bien que mal le controle de votre vaisseaux et réussissez à vous poser avec votre esquadron dans le spatio-port de Elysia.

*Cependant des ennemis arrivent"""

        total = 0
        
        print(self.space, self.fincombat)
        time.sleep(temps)
        answer1 = input(Q1)             #QCM de culture général, Une chance par réponse
        
        if answer1 == 'a':
            total = total + 1
            print('Bonne réponse')
        else:
            print('Faux')
        
        answer2 = input(Q2)
        
        if answer2 == 'd':
            total = total + 1
            print("Bonne réponse")
        else:
            print('Faux')
            
        answer3 = input(Q3)
        
        if answer3 == 'a' or answer3 =='b' or answer3 == 'c' or answer3 =='d':
            total = total+1
            print("Bonne réponse")
        else:
            print('Faux')
            
        answer4 = input(Q4)
        
        if answer4 == 'a':
            total = total+1
            print("Bonne réponse")
        else:
            print('Faux')
            
        answer5 = input(Q5)
        
        if answer5 == 'A - S - O - N - D' or answer5 == 'ASOND' or answer5 == 'A S O N D' or answer5 == 'asond' or answer5 == 'a s o n d' or answer5 == 'a - s - o - n - d':
            total = total+1
            print("Bonne réponse !")
            
            
        else:
            print('Faux')
            
            
        print(total)
        time.sleep(temps/2.5)
        print(self.space, "{} soldats vous ont rejoint".format(1000*total), FinFelucia)
        time.sleep(temps)
        print(self.space, Elysia)
        time.sleep(temps)
        
        return(total)                   #La fonciton return le nombre total de bonnes réponses ce qui permet de l'utilisé dans la boucle du jeu
    def DarkLaum(self) :
        
        self.EntranceDarkLAUM = """ 
        
                               ._                                 
                              ,-'_ `-.         """ + Style.RESET_ALL + Fore.RED + """DarkLAUM : - "... Je suis ton... pire ennemi...           """ + Style.RESET_ALL + """        
                              ::". -. `.        
                              ||     .  \                   
                              |:     | \ \     """ + Fore.RED + """  Ne crois pas que c'est en ralliant quelques """ + Style.RESET_ALL + """         
                              : .    |  ;\`.                        
                              _\ .   '  | \ \                       
                            .' `\ *-'   ;  . \  """ + Fore.RED + """âmes perdues à ta cause que tu vas provoquer la fin de l'Empire " """ + Style.RESET_ALL + """           
                           '\ `. `.    /\   . \                     
                         _/  `. \  \  :  `.  `.;                    
                       _/ \  \ `-._  /|  `  ._/                     
                      / `. `. `.   /  :    ) \                      
                      `;._.  \  _.'/   \ .' .';                     
                      /     .'`._.* /    .-' (                      
                    .'`._  /    ; .' .-'     ;                      
                    ; `._.:     |(    ._   _.'|                     
                    `._   ;     ; `.-'        |                     
                     |   / .-'./ .'  \ .     /:                     
                     |  +.'  \ `-.   .\ *--*' ;\                    
                     ;.' `. \ `.    /` `.    /  .                   
                    /.L-'\_: L__..-*     \   ".  \                  
                   :/ / .' `' ;   `-.     `.   \  .                 
                   / /_/     /              \   ;  \                
              |  _/ /       /          \     `./    .               
            `   .  ;       /    .'      `-.   ;      \              
           --  /  /  --   ,    /           `"' \      .             
          .   .  '       /   .'                 `.     \            
             /  /    `  /   /                  |  `-.   .           
        --  .  '   \   /                         `.  `-._\          
       .   /  /       : `*.                    :   `.    `-.        
          .  '    `   |    \                    \    `-._   `-._    
     --  /  /   \     :     ;                    \              |   
   .    .  '           ;                          `.  \      :  ;   
       /  /   `       : \    \                      `. `._  /  /    
  --  .  '  \         |  `.   `.                      `-. `'  /\    
     /  .             ;         `-.              \       `-..'  ;   
 `  .  '   `          |__                     |   `.         `-._.  
_  :  /  \             ;`-.                  :     `-.           ;  .
    `"  `               |   `.                 \       `*-.__.-*"' \ .
' /  . \                ;_.  :`-._              `._                / .
                       /   `  . ; `"*-._                       _.-` .
                     .'"'    _;  `-.__                     _.-`     
                     `-.__.-"         `""---...___...--**"' |       
                                                  `.____..--'
        


"""
 
        self.suiteDarkLAUM = """ 
     
* Vous êtes paralysé par la peur, vous ne répondez rien, Dark LAUM a l'avantage """ + Fore.RED + """

Dark LAUM : - "Viens de te battre." """ + Fore.RESET
        
        print(self.space, self.EntranceDarkLAUM)
        time.sleep(temps)
        none = input("Que voulez vous répondre à Dark LAUM ? \n ") #l'input ne sert à rien, c'est juste du troll
        time.sleep(temps/3)
        print('\n ...')
        time.sleep(temps/3)
        print(self.suiteDarkLAUM)
        time.sleep(temps/2)
        
    def DarkDeath(self):
        
        
        self.death = """
        
* Votre dernier coup affaiblit très fortement le seigneur

* Vous voyez qu'il ne s'en tirera pas """

        self.deathSuite =  Fore.RED +"""
        
Dark LAUM = - "Je peux être vaincu, mais cela n'empêchera l'Empire de subsister... Votre 'Résistance' ne vaut rien face au pouvoir et à la puissance de l'Empire..."

...""" + Fore.RESET + """

* Vous ne pouvez plus accorder plus de temps à cette discussion

* Vos alliés ont posé la bombe et Elysia vit ses derniers instants

* Vous partez

""" + Fore.RED + """ 
Dark LAUM = - "Longue vie à l'Empereur Palpotel" """  + Fore.RESET + """

* Elysia explose """
    
        print(self.space, self.death)
        time.sleep(temps)
        print(self.space, self.deathSuite)

    def Credits(self):
            
            
        self.crédit = """
        
Réalisé par : """ + Fore.MAGENTA + Style.BRIGHT + """
    
                                                  .                  ......      .......               .......     ......               .....         
    :*.    .=+         -#.                   .=.  :.               :*=:::::==. ==-----:=+: *=     .*.:*+:::::-=.:*+:::::==..*.     :*.:*=---=+:.      
    .=%:   #*:  .:::-: +@:  :-:::.. -=-=--:: =@*: =- .====---:.    -@+:::::*%.:@=      -@# @*     :@:-@#:::::-%:-@%:::::+%::@.     =@.-@:   .-=#.     
      *=..:%:   .+==%% =@: -%%+==@+ #@*-.:-%.-@=. %* -@@*:.::#+    -@#******= :@-      :@* %+     :@::@%+****+= -@%+*****+ :@.     =@.:@.     -@:     
       #*:@*   =*::.#@ =@: =@%-.::: *#    :@.-@:  %+ :@#     %*    -@=.....+@.:@=      :@* %+     :@::@*.....:%::@*.....=@::@.     =@.:@.     -@:     
       .+*:.   #@.  %@ =@- -@%.  *= %#    -@.-@=  %* -@#     %*    -@=     +@::@=    . -@# @* . . :@:-@*     :@-:@*     =@-:@:     =@.-@:   :%+:      
        :=      -===+* :*.  .-===:. ==    .*  :+- +- .+=     =-    :*=======:  :======-=-. .:====-=- :*-     .+..*=     :*: .-=====-. .+=-===+.       
                                                                                                                                                      
 """ + Fore.RESET + """                                                                                                                                                     
                                                             .                                                                                        
                                                            :@.                                                                                       
                                                     .....  :@-                                                                                       
                                                    -%+++%# :@=                                                                                       
                                                    *%...-+ -@                                                                                        
                                                    =#-::-: .#-                                                                                       
                                                     +#**#.  .+.                                                                                      
                                                      ....    .       """ + Fore.GREEN    +"""                                                                             
                                                                                                                                                      
     .#@%%%@=           .%+            .%-          +#       #+        .%+    -@     -%%%%%%@#  *@%%%%%%@*.%=  **      *#                             
    =%.     -+          .@*                         *%       #%:      .*@*  .-=*=:   =@. .   +@:    %#    :@+  *@@+    #%                             
    =@.           -***  .@%+*+*-  :++*- +:   :*+*+. *%       #%**.   =##@*  -@* @*   =%.     =@:    #*    :@+  #%=%=   #%                             
    =%. :#**#+    :+-#*:.@%===+#* =@*+-.@=  =%+==*# +%       %+:@=  .@# @* -#=. :%=  =@******#-     #*    :@+  #* -##. #%                             
    =@.  --:#%  .--=-*@+ @*    #@ -@:  .@=  @@---=# +%       %* =+--+:.:@* *@=:-:@@  =@------*#.    ##    :@+  ##  :#=.*%                             
    :*::::: =#  -#-:.+%= @#::::** -@:  .%=  +#::::  +#       #+   *=   .@+ **####*+: =%      =@:    **    .@+  **    ++*#                             
      :----..:    .--::. ::--:-.  .-    :.    ----. .:       :.         :..:       - .:      .:     :.     -.  ..     :::   
    
    

"""
        self.crédit2 = """
        
Avec l'aide de : """

        self.crédit3 = """
        
...........:-:..........................................:-:........................................::...............     ..::..       ...:::..........
............::..........................................:::........................................::.........::....     ...:...::.  . ..:::..........
.........:...::.......................................::.:::.....................................::..::........::..:.    .......::.....::.............
......::::::...::::...........::::::...............::::::::..:::..............................:::::::..:::.........::.  ...........::--::.::....:::...
..::::....::::....:::::........:..:...........::::::...::::....:::::::.................::::::::...:::....:::::.....::.  .:....::::::::....::...:::....
::........::.........:::::::::::::......:::::-::.......:::...........::::::::::.:::::::::::.......::...........::::::...::::::::::...:....::...:::....
..........::..:...........:.::::::::::::::............::::....................::.:::..............::......................:...............:::..:::....
..........:::.:.......................................:::::......................................:::::................... .:............:::::..::::...
.........::::::.......................................:::::......................................::.::........... .   .... ...............:::...:::...
.........:::...........................................::::.............................::::::::::::::::::::::::::.....:::.....::.:.:-:::::::::::::::-
..::..::::::::::::::::::::-:-----------------=--------====--==-====---==-===============::=========================================================+==
========================================================================================::============================================================
+==++=============================================================++++==================-:========================================+===================
+++++++++++++++++++++==+++++++++=====++++++++++++++++++++++++++++++++++=+===+===========--============================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=++++++++==++++++++++++++++++++==++===++=+=+++==++==+++======+========+++++++++++++++++=+
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*++++=++++++++++++++++++++++++++++++++++++++++++++++++++++=+++====+++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*%@@@@@@%#++++++++++++++++++++++++++++++++++++++++*++++++++++++++++++++++++++++++*+**
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*#%@@@@@@@@@#+=++++++++++++++*+**++*++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*####%@@@@@@@@@%++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*#####%@@@@@@@@@@@#++*++++++++**+++++++***++++++***++***++++++++++++++++++++++++****+++***
+++++++++++++++++++++++++++++++++++****++**++*++++++*++++++*#####*###%%@@@@%%%%*+++++++**+++++++++++***+++++++++***********+***++*++*++++++*+**++++***
++++++++++++++++++++++++++++*++++++++++++++++*+++++++++*+++*##****##%%%######%%*+*++++***+++**********+++++++++**++*****+++++++**+++++++*+*+**+++++*++
+++++++++++++++++++++++++++*++++++++++++++++++++++++++++++*#####%@@@@@@@@@@%####++********++*++*++++++++++++++*+++++++++++++++++++++++++++++++++++++++
=++++++++++++++=++++++++++=++++++++++++++++++++++++++===+===--=====+++**###%%%%%++++++++++++++++++++++*++++++**++++++++++++++++++++++*++++*+++++++++**
==+++==+++==+===++==+++=++====++++==++==++++=+++++++++++==:..:::::.:::.::::::-=+*++++++++++++++++===++++++++=+++++++++++++++++++++++++++++*+++++++++++
=+++++++==+=====+++++++++++++++====================+++++=-..:::::::::::::::::.  -====+=+++++++++++++++++======+++++++=+++=+++++++++++++==+++++++++++++
+++=++++====================================+===========+-..:......:::......... .-===+===+++====+++++======++============--==============+=+==+====+++
=================----=---==---=+=======+==================: ...    .:.    ......:---============+=======================---===========--=====-=======-
-====---=======================+=====--=-----========++===-.........:..   ...::::----==========--=-==-======--=-=========--------==-------=-----==----
======-====--======+====-==-----==-:::-:...::-=-----:-----::::....:::::.....:::..:---=-=======-----====++++=-=+=++++++++++++=++++++++*++++*++*********
=-----:--::--==--=======--====================++==+==+++=+=:::::::::::.:::::::::::----=****##*#######################*****#####*****#####*******#*****
*****************##################**##################***#=:::::::.....:::::::..::-=+##***************#####************#*****************++********++
*************+*********************************************#=:::::.......:::::-==++*******************************************************************
***********************************************************##-::::::...:::::::*###************************************#******************########*####
##########************************+**********###***#####****=:::::::..::::::::-===+*#####**************************************#**********************
************************************************###+++++:... .:::::::.:::::::.  .. :==++*#######*****************************##*######################
************************####*###***#############*+-          .:::........::::.  ........:-==+++**####**#********++***********+++++++++++++++=++=======
********######################################*-:             :::... ....:::..    ..............:-----:------:::-:::::::::::::::......................
++*+*********++++++++++++=============--------.               .:::::::::::...     ...........    ...................:::.:.::::.::.::::::::::::::::::::
.::::::::::.:::..::..........:.................                ....::::::....       .......    ....................::::::.::...................:......
...::..:............::::::::::::::::::::...:...                 ............   ..       .    .........................................................
...::..:...........:::..........:.::..........                     ........                 ..........................................................
...::........................................                                               ..........................................................
............................................                                                  ...................  ...... .............     .         
...........................................                                                     .....:. ................:::.::::::::::::-------=======
                          .  ..............                                                     ..... -*+****+**********###*##**######################
:::::------------=====+++++++*********=. .                                                       . .:-=*#*********************************************
######################################= .                                                         -*@@@#*########**###################################
#####*###############################*+**=..                                                    .+#%@@@%#++*+++++++=+==============-------------------
#########*********************+**++++*#%#----:.                                               .:=**#%%@@%=.::.....:..........:.................::.....
=--------:----:-::::::::::::::::::..=##%=:---:::.                                            .:-+**##%%%%%=.::.......::::::::::::::::::::.::::::::::::
........................:..::..:::.-####-:-::::::                                            ::-=+*##%%%%%#-.:........::::.:::::::::::::...::::::..:::
:::::..:::::::..:::...:::..:::..:.:*#*#*:::::::::                                           .:::-+**##%%%%%*:.:........::::::::...:::::......:....:...
............:.....:..:..........:.-**##*::::::::.                                           ..:::-=+*#%%%%#%=..........::::::::...:::.................
...............................:..+**###=:::::::.                                          ....::::+#%%%%%%%#:..........:::::::.::::..................
..................................+**###%+::::::                                           ......-+#%%%%%%%%#+........................................
.................................:+++**####=:::.                                           ... .=##%%%%%%%%%##: ......................................
.................................:+++******#+:.:.                                          .:--+###%%%########+....................................   
.................................-===+++++**#*=:...                                      :=+++**#%%%###*+++++++:                  ..  ................
                                .:--------=+*##*=:..                                   .----=*##%%##**+===--::-+==++++++++++++++++++++++++++**********
-----===========================+=::---------=*#%#*=:                                 .:..-*##%%##**+=-----:-+####################*#############**#***
##################################+-:----------=+*%%%*=.                              .:=*%%###**+=---------*#****************************************
**********************************#*-------------=+*#%@%*-.                         .-+#%%##**+=----------=*******************************************
***********************************#*---------------=+*%@%#+:                     :=*#%###**+=----------:=#****##******##**###****#**#****************
**************************#********##-.:---------------+*#%@%*=.               .-=+*%%###*+=----------:: :=+==============+=============----------::-:
***************+*+++++=++++++++++++++:  .::-------------=+*%%@@%+:      .::--=*##+-=+*#+=---------::..................................................
--:-:--:::::::::::..::..:...::..........   ..::------------=*#%%%%*=-+*##%%%%%%###+:.:=-------:....   ................................................
...................:....................       ...::----------+####*+#***#**++++*##+:.::-::..      .  ............................::..................
..................::.....................            ..::-------=-=++=::-=====++=--=-                  ...........................::..................
.........................................                 ...--::===-===-:-====----:.                   ..............................................
.........................................                    .-::-::==-:----=----:.                    ...............................................
.........................................                     :--:::::.-==-::::.                       ...............................................
.........................................                      :::-:::::::::::.                        ...............................................
.........................................                        .:::---:::::::.                       ...............................................
.........................................                          ....:-::::::.                      ................................................
..........................................                             .--::::::.                                                                     
....   ..                                                              .--::::::.                     ....::::::::::::::----::---==================+++
        ..................:::::::::::-----:                            .-:::::::                     :*********************#****################***#**
++=+++++++*****+*****************#*******#*:                           .::-:.:-:                    .+********************++**+***********************
********************************************:                           .-: .::.                    -*****************************########*######*####
***********************************#**###**#*:                          .:  ::.                    .+#**#*############################################
***********************###############**###*#*:                             ..                   . -#*************##***********##****####******###****
**************************************######*#+                                                   :***************************************************
************************************#**+==----:.                                                 .+********************************++++***************
*******************************###*++-..........                                                 -************************************++**************
********#*********#************+=-:..............                                                -+++++++=+=+++++=========-==========----======-------
+++++++++++++==++++++=========:..................                                                .::........::::::....:::.:....:::....................
:::::::::.::::..............:.....................               .                  . ..        .............................:.::::.::........::....:.
..................          .  .                                 :-                                      .............................................
*********************************************+*****+++++++++++**+##*++++++++++++++++**********+*******************************************************        

CYRIL DESJOUY """

        self.crédit4 = """
        
        
::-=+=**+*====*#***+=+====+*++=-=-:-=++--*%%%%%%*-::---::::---===---=*++++++*****+*+*##*+==++==+++**+==++==+++**=--===++==*#+=-::-----=========+==---=
::-++==***+===+*#**+++====+**+=-=-::-==-=*%%%%%%*=-::---::---===----++++++++*****+***#*+===++==++*#*=-=++===++*+=---------==+--:::::-----==----==-:::-
.:-=+=-+#*=--=++##*+++=====+**=-==:::::-+%%%%%%%*=--:::-:::--==----=+++*+++++****+***#*++=+++==+**#*=-=*+====+*+=-----=---=++=--::-------===--===--::-
::-=+-:-**=---+=*##=-+=-=-==++=-====++**#%%%%%%%*-----------===----=++++=+++*****+***#*+++++====+**=:-=+=-===+*+---=--:::--=+-:::::::::-====-----::::-
::-=+=--+*+===+==##=-=---:=++*=-=+++++*##%%%%%%%*======-----==----=+++++++++****+****#*+=-=+==--+**-::=+=:-+++****###=..:---+-..:....:-+*+--=**+-:::--
=--=+==-=**===+==*#+=+===-=+=++==+=+++*##%%%%%%%*=========-===----=+*+++++++****++***#**+-=++===+##+--++++++++*####%%*-:-=--=-.....:=++***++###=-:.:--
---=++===*#*==+=-=**==++++**++*+++++++*##%%%%%%%*+++**++===++==--=++++=+++==*********#*++==+++++*#*+===+++=+++*+++#%@#=--=--=-.. ..:-----====----:.::-
:::==---=***+++=-=*#+++++****+***++=++*##%%%%%%%*++++====-=+++=--=++++++++==+******+***+++=++****#*---++=--+++*=-=+*#*=--===++---==-:----=++==++-:----
:-======+**#*++==*###***+==*%**#*++=++*##%%%%%%%*=+*+-:--=++++==-=---------=+++***+++*++*+++**##*+-::-+***++++*+==+***+=-=****+**++=-=+****+++*+++++**
===+++*++*+##**+*#######***#%****+=+++*##%%%%%%%*=*##**++++++=--::::::::::--==+*+++++*+*****++***=-::-+#%%*+++**+*###*+--+#%#**+=---::-=-===++***+**##
%+-=**+=+*+*######**#%###%@%##*+++++++*##%%%%%%%+=+*##*++++++-:::::::::::::---===++++=+*+*%*=--=++=---+**++++**+*####***=*%@@%%#+=-=-:-==--==-=++=-=+=
%#++*#*++***####%%########%%%##*++++++*##%%%%%%%+==+++=====-::::::------::----=-========:-+=-.:=*=--:-====+++*+=+###****+*%%%%%*+-:::::-:::::::--:::-=
%%@%#%%#*#%%%%#%%%#**#%%%%%%##%%*+=+++*##%%%%%%#*++====---:::::::::::::::::::---======-::--:::-+*==+*=+*##*++**=--===++=--+***+:::..::..::::.::.....:-
***##%%#*#%###%%%%#*=+#*+*###%%@#+=++***#%######*+=---::.::::..:::::-::::....:--===-:-:.:=:.-*#####%%*+#%#+++***++++====--+++*+****+==--+*++*+++++++==
#*++**+++*###*#%%%%%%%%%#**#%#%#*+++++**######*=----::::::::........::...... .::::::.....:..:=###%%%%*+#%#*++**********+==***#*#***+**+=+*************
#+==+***#******##*++++*%%###%%%%#+=++++*****+---:::::::::......:::::..  ................::::::-+####*++*=-=++*******#***==**######***#*+=*#*********++
**++*#%%##%%####%####*##%%%##%%%#+=++++++=+=---::::..::::::::::::.....   ..................::::-=+=+==++::=++*##********++****#######***++*#*********+
%%%%##%%#%%%@%%########%%%@@@%%%#++++++=====::.......:.:::::::.::::...    ..................:::::::-+++**++++**+++******##***########*##*+**####*##***
%@@%#%@@%%@@@@@@%########%%%%%%%#++++++===--:.::................::::..     .... .  .........::::...:=++#%*+++##*++*#**####**#*##*###*****++***********
%%%##%%%%%%%%####**######%%#####*+=++====-:::....          ....:::..         ...  ..:..  ....:.:...:--+**++*+###***#%%@%%#********#*******++**********
+++=*%%%@@%%%#*****##%%%%%%#####*+===----:::...            ...::::.       ... ........   .......:..::-=**++*+********#%%#*+******#%###*****+****#*****
--::==-=+*****##***%%%%%%%%%%%%#*+==--==-:...               .....         ........       .......:...::-=*++++*#####=--=+#*++******#********+****##****
#*-:=-::-+**+*######%%%%%%%%@@%#*===---::...                               .......  .       .:::.. ...:-=-==+#*=----=++***+=+*****+++***********###***
#*=-+=----=+##%%%%%%%%%%@@@%%%##*===--:....                                 ...........      .........::----+*=:--=--=++**+++*************#*****###***
%%*+++++++++*###%%@%%%%%%%%###*+++=--:...                                   ...:. ... ..       ..::..::.:---+*++*++================++*+++*##*######*++
@@%#####%####%%%%%@@%#%%%%%####=---::...                                    ...:.....           ......:::--=+*++================++++*###*########*****
@@@%%%##%##%%%%%%######*##%%###=:......                        ...........    .........   .      .......::.:=**++=+====++++++==*#%##########*****##***
@@@@%%#################**#####+:.:.....                   .....::::::::....     ..........     . ..... .::..-***++++++++*****++*#%%#****###****++*****
%%%%%%%%%@@%%%%%%%%#**#####%#*=:.:.....               ....::::::----:::::...    ..........  ..    ..   ..:---+**++====+++++++*++++++++==+========+##**
##%%%%%%@@@@@@%%@@@#+*%%%%%%#*-........             .....::::--------::::..      .....   .  .         ..:::--+***+==---==+++****+=====------===++*****
####%%%%%%%%%%%%%%@%##%@%#%%#+:. ..   .            ..::::::::-------:::::..        .                 ...:.:::-=+*###****+++++*****++=++***************
####%%%%%%%%##*########%#*##*=:                   ..:::::::---------:::::..        .       ..          ..:::::-====+*#%%%#**+++********####%%####%%##%
+**#%%@@%%%%#***###%%%%%###+-:..                 ...::::::----------:::::..                             .::::-=+++=====+**###########%%%%%#*********++
--+%@@@%%@@%%%#*#%%@@@@@@%*+:.                   ..::::::-----------:::::..                         ... .:..:=**#########***###%%%%%@@@@@@%%%%%%###***
=++**#########**%%%%%%%%%%#+:                   ...:::::-------------::::...                         .......-====+*#%%%####**###%%%%%%@@@@@@@@@@%%%%@@
#%%%%%%%####*++*#########***:                   ..:::::-----------------:::..        ..                   ..:::-+**######*++**++************##%%@%%%#+
%%%%%###****#%%%%%%%%%%%%%%#=.                 ...::::-------------------:::..      ....                 ..::.:=++*###*****####*###****++***++#%##+=:.
++==++++**#%@@@@@@%%%%####**++-.               .::::----------------------:::..                          .:::.:---+*#*==*#%%#*++++++++*****###*=-:...:
==+++***###%%@%%%%%%#######**#*-              .::::::---------------::::::....                           ..:..:=--*##*+*%%%#=:::.......::.:-+=::::-==+
*******#####*#########%%%%###%%*:.            .....   ...:::::::--:::...      .                        ........:-++####%%%%#+==+=++===----::::-=+####*
****##*##*++++++====-===+++++*#*-.            .    ........:::::-::::........:::....                ........:::-=--==+*********#%%%#*+----::=+*####*##
#**####*=---------===+++==+***#*-.:           ..::...    ....:-----::... ...     ..::---::..    ... .  ..   ...:..:-::::::::::-====-----=***##%%%%#**#
#######+=======-=+++++++++++++**++=:         .::.   ..     ..:--==--::..........:...:=++=--:.    ......       .::--==----::::::-::::-+*#%%@%@@%%%%%%%@
######+=========++++====+++=+++*#+=-:.       .::............::-==+=--::........::::-==+++=--:        .       ..:-=*##*+=-:::::--==+***#%%%%%%%*+++*#%%
#####*=========***+=--=+**+***++=-:::.       .::::::......:::-==+**+=--:::::::::-==+****++++-.             .. ..:*%#*===::-=+**#%%%%%#%%%%%%%##***##%#
#*##*++++++++++**+===+++++*****+-::::..      .---:::::::::::--==+*+++==----:----=+*******+++=:             .....-*#*===+=++*###%%%%%###########%%%%%##
+++++++********+++*++**++*****++-::::.       .--------:::::---=+++**+===-===-===+**####******=::::. .... ....:-=++++++++++++++**#****+*****####*######
***+**********+=+**=++***+***++====-:..      .--------:--::---=++***+==--=++===++**#*###*****+===::. .::..-:.-+*********+++***++*****##########**####%
************++++**++********#+----++-::....  .---------::::---=+*##**+*+:::--===++++***********+=----:--.--:-+**********++++***+**##%%##############%%
*+++++++***+==+*+++***###%%@%+:::-++=--:.::..:------:::..:--:--=+**##**+:...::--==+++**********+===+++=-:-:=****************++=+#%%%%#***######%####%%
*+++++++*+=--==++**###%%%#%%#-:.:=+==+++-=+=::---:::::...::::::-=+=--==--::...::--=+++*********=++++**-::-=+*********#****+==-=#@@@%%#***##*+##%######
*++++++**+=--=+++*%%#####*##+:.::=+==+##*+*+-:-::::::...:...::::::::-===---::..::-===+********+--====:..:::-+**********+=-:..:=*%@@%%%%%###*+*#%%%%%%%
********++===++++*%%####****+-:::=+=-=**#*+-:--:::::.....::::::::::-==+++=--::..:-===+********=....::... ..:=****++****=.    -+*%%%%%######**#%%%%%%%%
=++++=+*++=-====+++**#%###**+=-::==-:-*#**+=---:::::...:::::::::::----=====--::::==+==+*******=  .::...     :=*********+-. :-==++++++======-=====+++++
====--====-----==++***####*=::..:-=-:-*#**++-::-::::...:....::::::::::::-:::.:::-+++==+*******- ..:....     .-+*********+---:::-===-=======--=========
-------:.:-----==+****###**=-. ..---:=**##*+=::-:::-::..    :---=-=++++=+-:...::=+++==*******+: ........     .:=++++++++++=. .:-=+=========--===++++++
........ .:::--===++++++====-:...::::--+*#**+-:::::-:::......::--:-++--=+===-::-++++==*******+.........       .:-----------:...-=++++++====-==++++++++
          .::::--==+=----:::-:.  ...:-=====--:::::::::::::::::::::::-==+***+=--=+++==+++*+***= ..   ......     ..........:::...:-==========--====+++++
          .:---==++=----------:..::..-=====-:::::::::::::::::::::::--==++++====++++==+++++***-  ....::::::..             .--::...:--------::----======
        .....::::::..:::::::::.  .. .:----:::....:::::::::::::::::::--==+===++++++++++++++*#*:...::--==-::::.  .         .==-:..   ...................
      .:--......::::::::::::...  .. .:::-:::......:::::::::::::::::::--===-=+***+++++++++****:.----=+===-----..          :--==:..:::::::::..::::::::::
:::::::-=-:..::::--------::::..  ....:-----:::.....::::::::::::::::---=====++***+++++++******=--:-====+=---==-:.         ::.:-:::------::::::---------
==========---------=======--::.  ....:--==-----:::::---::::--:::--===+==+++++**++++=++****##*=-:::*#*+=========-::----::::--:-------------:::---------
+======+++==------====+++===-:....:..:--==----------==:::::::::----=====+++++++++===++*****#*:.:..-###+==+==================-=------------::----------
+++++++++++=======+++++++++=-:...::::--=============-. .::::::::::::::----=======+++++****##*+-...:+*%%*+++++++++++++++++++++++=++++=======-==========
++++++++++++++++++++++**++++-::.:::----=========+==-.  .:::::::::::::::::-----=+++++++****####+:..:=*#%%*++++++++++++++++++++++++++++++++++==++=++++++
++++++++++++++++++++++**++++==--------============-:   .:::::::::.......::::-=++***+++****######-..-*##%%%*+++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++*+*+++======----======++===-:.   .::::::::::......::--==+*****+*****######+. -*##%%%@%++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++=====-=======+=====--.    .-:::::::::::::::---===++++++++***#######+-.:+#%%%%%%%%##**+++++***++++++*******+++++++++++++++
++++++++++++++++++++++++++++++==========+=======-:     :::::::::::::::::---==+++===++****#######+-. -#%%%%%%%@@%%%%%%#*++++**+**********++++++++***+++
+++++++++++++++++++++++++++++++++==-============-.     .:::::::::::::::::--==+++====++***######*+-. :*%%@%%%%@%%%%%%%%%##**+++*****************+******
+++++++++++++++++++++++++++++++=----===========--:     .::::::::::::::::::-==+++====++****#####+=:. :*%%%%%%%%@%%%%%##%%%%%%#**+**********************
++++++++++++++++++++++++*++++==---===========----:     .:::::::::::::::::::-=+++=====++*****##*=-:  -#%%%%%%%%@%%%%%###%%%%@%%#****+*+**+*******++++++
+++++++++++++++++++*+++++====--------=======-----:      ..:::::::::::::::::-=======+++++*****+=-:. .+#%%%%%%%%%%%%%%###%%%%%%%@%%##*********+*++++++++
++++++++++++++++++**+++=====-----===---=====-----:        .::::::::::::::::--=====+++++++***+=--.  :*%%%%%%%%%%%%%%%###%%%##%%%%%@@%%#****************
++++++++++*******+++=========---====-========---=:        ...::::::::::::::-----==++++++++*+=--.  .=#%%%%%%%%%%%%#**##%%%%###%%%%%%%%%%#********++**++
+++++++++*****+++++===========-===============--=:          ...:::::::::::-------=+++++++++=-:.   :*%%%%%%%%%%%%%%%###%%%%##*#%%%%%%%%%%%%#*++++++**+*
++++++****+++++==============-===================.        ......:::::::::::::::--==++==++==-:. . .=#%%%%%%%%%###%%%%#%%%%%%#*##%%%%%%%%%%%%%%#*+++**++
++++++++++++=+++=====================-===========.        .......::::..::::::::--========-:..    -*#%%%%%%%%%######%%%%%%%%#**##%%%%%%%%%%%%%%%%**++*+
++++++++++++==================-==================.        .....:::::::.....::::-========-:...   .=##%%%%%%%%####*#**#%%%%%%#**##%%%%%%%%%%%%%%%@%%#**+
++++++++======================-================++.           ...:::::::::.:::::-======-::.      :*#%%%%%%##%######*+*#%%%%#######%%%%%%%%%%%%%%%%%%%%#
++++++=+=======================================*+.              ..::::::::::::::-----:::..      -*%%%%%%%######*##**#%%%##########%%%%%%%%%%%%%%%%%%%%
+++++==========================================++.                    ......::::........       .+#%%%%%%%%##########%%%############%%%%%%%%%%%%%%%%%%%
++++============================================*:                        ....... .....        -*#%%%%%%%%%#**#####%%%%############%%%%##%#%%%%%%%%%%%
+++=============================================*+                       ............    ..   .+#%%%%%%%%%##*#####%%%#############%%%%###%#%%%%%%##%%%
+===============================================+*:                      ...........    ..   .=*#%%%%%%%%%########%%%####**#######%##########%%%%##%%%
+===============================================+#=                     ...........    .    .:+##%%%%%%%%########%%%%####*#####%##%######%###%%%##%%%%
+================================================+*:                       .......        . .=###%%%%%%%########%%%%###*#######%##%######%##%###*#%%%%
+================================================+#=                       .....            :+###%%%%%%%########%%%%##***#####%%###############*##%%%%
==================================================**:                ..........          . .=*###%%%%%%%%######%%%%###***###%%%%##############*##%%%%%
"""

        print(self.crédit)
        time.sleep(temps)
        print(self.crédit2)
        time.sleep(temps)
        print(self.crédit3)
        time.sleep(temps)
        print(self.crédit4)
        time.sleep(temps)
