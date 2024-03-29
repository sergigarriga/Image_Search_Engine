# -*- coding: utf-8 -*-

#+--------------------------------------------------------------------------+#
#   Importem mòduls                                                          #
#+--------------------------------------------------------------------------+#

import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

#+--------------------------------------------------------------------------+#
#   Definim les classes                                                      #
#+--------------------------------------------------------------------------+#

class Visualitzador(ABC):
    
    def __init__(self, resultat):
        self._database = resultat
        
    @abstractmethod
    def visualitza(self):
        raise NotImplementedError
        
        
class Visualitzador_Recuperacio(Visualitzador):
    
    def __init__(self, resultat):
        super().__init__(resultat)
            
    def visualitza(self):
        print("\n -- Visualitzant resultats --")
        
        index = 0
        opcio_2 = 1
        fig, axs = plt.subplots(1,5)
        pos = 0
        for i in range(index*5, (index*5)+5):
            self._database[1][i].visualitza(axs[pos])
            pos += 1
        plt.show()
        
        while opcio_2 in [1,2]:
            print("𝗘𝘀𝗰𝗼𝗹𝗹𝗶𝘂 𝗾𝘂𝗶𝗻𝗮 𝗼𝗽𝗰𝗶𝗼 𝘃𝗼𝗹𝗲𝘂 𝗿𝗲𝗮𝗹𝗶𝘁𝘇𝗮𝗿:\n\
    1 - Visualitzar els 5 documents següents.\n\
    2 - Visualitzar els 5 documents anteriors.\n\
    Altre núm. - Sortir")
        
            try: 
                opcio_2 = int(input("Opció: "))
            except:
                print("\nERROR: Opció NO vàlida. Tria una opció correcta!")
                opcio_2 = int(input("Opció: "))
            
            if opcio_2 == 2 and index == 0:
                    while opcio_2 == 2: 
                        print("\nERROR: No hi ha documents anteriors. Tria una opció correcta!")
                        opcio_2 = int(input("Opció: "))
            
            if opcio_2 == 1:
                index += 5
            else:
                index -= 5
        
            fig, axs = plt.subplots(1, 5)
            pos = 0
            for i in range(index*5, (index*5)+5): 
                self._database[1][i].visualitza(axs[pos])
                pos += 1 
            plt.show()
    
class Visualitzador_Agrupacio(Visualitzador):
    
    def __init__(self, resultat):
        super().__init__(resultat)
    
    def visualitza_basic(self):
        try: 
            for i in range(len(self._database[1])):
                fig, axs = plt.subplots()
                self._database[1][i][0].visualitza(axs)
                plt.show()
        except:
            print("\nERROR: Model erroni!")
            
    def visualitza_dinamic(self):
        try: 
            opcio = -1
            print("\nTrieu un grup ' 1 -",len(self._database[1]),"': (", len(self._database[1])+1," - Sortir )")
            while opcio < 1 or opcio > len(self._database[1])+1:
                opcio = int(input("Opció: "))
                if opcio < 1 or opcio > len(self._database[1])+1:
                    print("\nERROR: Opció NO vàlida. Tria una opció correcta!") 
                elif opcio != len(self._database[1])+1 and len(self._database[1][opcio-1][1]) == 0: 
                    print("\nNo hi ha documents en aquest grup!")
                    opcio = -1
                
            if opcio > 0 and opcio < len(self._database[1])+1:         
                print("\n -- Visualitzant Grup", opcio, "--")
                #print(self._database[1][opcio][0].file_name)
                index = 0
                opcio_2 = 1
                opcio -= 1
                avancar = True
                if len(self._database[1][opcio][1]) >= 5:
                    fig, axs = plt.subplots(1, 5)
                    pos = 0
                    for i in range(index*5, (index*5)+5):
                        self._database[1][opcio][1][i].visualitza(axs[pos])
                        pos += 1
                    plt.show()
                else:
                    avancar = False
                    fig, axs = plt.subplots(1, len(self._database[1][opcio][1]))
                    pos = 0
                    for i in range(len(self._database[1][opcio][1])):
                        self._database[1][opcio][1][i].visualitza(axs[pos])
                        pos += 1
                    plt.show()
                
                while opcio_2 in [1,2]:
                    print("𝗘𝘀𝗰𝗼𝗹𝗹𝗶𝘂 𝗾𝘂𝗶𝗻𝗮 𝗼𝗽𝗰𝗶𝗼 𝘃𝗼𝗹𝗲𝘂 𝗿𝗲𝗮𝗹𝗶𝘁𝘇𝗮𝗿:\n\
            1 - Visualitzar els 5 documents següents.\n\
            2 - Visualitzar els 5 documents anteriors.\n\
            Altre núm. - Sortir")
                
                    try: 
                        opcio_2 = int(input("Opció: "))
                    except:
                        print("\nERROR: Opció NO vàlida. Tria una opció correcta!")
                        opcio_2 = int(input("Opció: "))
                
                    if opcio_2 == 2 and index == 0:
                            while opcio_2 == 2: 
                                print("\nERROR: No hi ha documents anteriors. Tria una opció correcta!")
                                opcio_2 = int(input("Opció: "))
                                
                    if opcio_2 == 1 and avancar == False:
                        while opcio_2 == 1: 
                            print("\nERROR: No hi ha documents posteriors. Tria una opció correcta!")
                            opcio_2 = int(input("Opció: "))            
    
                    if opcio_2 == 1:
                        
                        index += 5
                        if index+5 > len(self._database[1][opcio][1]):
                            avancar = False  
                            fig, axs = plt.subplots(1, len(self._database[1][opcio][1])-index)
                            pos = 0
                            for i in range(index, len(self._database[1][opcio][1])-index):
                                self._database[1][opcio][1][i].visualitza(axs[pos])
                                pos += 1
                            plt.show()
                        else:
                            fig, axs = plt.subplots(1, 5)
                            pos = 0
                            for i in range(index*5, (index*5)+5):
                                self._database[1][opcio][1][i].visualitza(axs[pos])
                                pos += 1
                            plt.show()
                            
                    elif opcio_2 == 2:
                        index -= 5
                        avancar = True
                        fig, axs = plt.subplots(1, 5)
                        pos = 0
                        for i in range(index*5, (index*5)+5):
                            self._database[1][opcio][1][i].visualitza(axs[pos])
                            pos += 1
                        plt.show()
        except:
            print("\nERROR: Model erroni!")
            
    def escull_opcio(self):
        print("\n| 𝙱𝚎𝚗𝚟𝚒𝚗𝚐𝚞𝚝𝚜 𝚊𝚕 𝚅𝚒𝚜𝚞𝚊𝚕𝚒𝚝𝚣𝚊𝚍𝚘𝚛! (𝚟𝚎𝚛𝚜𝚒𝚘 𝟸.𝟸.𝟹) |\n")
        print("𝗘𝘀𝗰𝗼𝗹𝗹𝗶𝘂 𝗾𝘂𝗶𝗻𝗮 𝗼𝗽𝗰𝗶𝗼 𝘃𝗼𝗹𝗲𝘂 𝗿𝗲𝗮𝗹𝗶𝘁𝘇𝗮𝗿:\n\
    1 - Visualitza el document més pròxim al representant de cada grup.\n\
    2 - Navegar pels els documents d'un grup.\n\
    Altre núm. - Sortir")
        try:
            opcio = int(input("Opció: "))
        except:
            print("\nERROR: Opció NO vàlida. Tria una opció correcta!")
            opcio = int(input("Opció: "))
        return opcio
    
    def visualitza(self):
        opcio = 1
        while opcio in [1,2]:
            opcio = self.escull_opcio()
            if opcio == 1:
                self.visualitza_basic()
            elif opcio == 2:
                self.visualitza_dinamic()