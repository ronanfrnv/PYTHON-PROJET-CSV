# -*- coding: utf-8 -*-
"""
@author: rfourneur
"""

from turtle import fillcolor
import folium

#-------------------------------------------------------------------------------------------------------------------------------
# Fonction qui extrait l'ensemble des informations du fichier villes_france.csv 
# Cette fonction ajoute l'ensemble des informations dans un tableau avec les guillemets en moins "" et sans les \n 
#-------------------------------------------------------------------------------------------------------------------------------
def extraction_villes_csv(fichier): 
    f = open (fichier, "r")
    lignes = f.readlines()
    f.close()
    valeur = [] 
    for i in range (len(lignes)):
        temp = lignes[i].replace('""',"") 
        valeur.append(temp.replace('\n',""))
    return valeur
#-------------------------------------------------------------------------------------------------------------------------------
# Cette fonction sépare l'ensemble des villes dans des tableaux différents afin de faciliter sa lecture par la suite
#-------------------------------------------------------------------------------------------------------------------------------
def extract_infos_villes(liste):
    table1 = []
    for i in range (len(liste)):
        temp = liste[i]
        temp = temp.replace('"',"")
        temp2 = temp.split(',')
        tab = []
        for a in range (len(temp2)):
            if a==1 or a==14 or a==15 or a==16 or a==17 or a==25 or a==26:
                if temp2[a] == '2A' or temp2[a] == '2B' or temp2[a] == 'NULL':
                    tab.append(str(temp2[a]))
                else:
                    tab.append(int(temp2[a]))
            if a ==3 or a==8:
                tab.append(str(temp2[a]))
            if a ==18 or a==19 or a==20:
                tab.append(float(temp2[a]))
        table1.append(tab)    
    return table1

#-------------------------------------------------------------------------------------------------------------------------------
# Cette fonction créer 5 fichiers en fonction des préfixe téléphonique  | Cette fonction ne retourne aucun résultat
#-------------------------------------------------------------------------------------------------------------------------------
def extract_villes_depart_indicatif(liste):
    Liste01 = ['75', '77', '78', '91', '92', '93', '94', '95'] # Liste pour les numéros en 01
    Liste02 = ['14','18','22','27','28','29','35','36','37','41','44','45','49','50','53','56','61','72','76','85','974','976']
    Liste03 = ['2','8','10','21','25','39','51','52','54','55','57','58','59','60','62','67','68','70','71','80','88','89','90']
    Liste04 = ['1','3','4','5','6','7','11','13','15','2A','2B','26','30','34','38','42','43','48','63','66','69','73','74','83','84']
    Liste05 =['9','12','16','17','19','23','24','31','32','33','40','46','47','64','65','79','81','82','86','87','971','972','973','975','977','978']
    
    # Par exemple si dessous la fonction lis chaque numéro des départements en 01 et les compares avec l'ensemble des villes
    # Si celle si correspond elle l'ajoute dans le fichier texte
    file01 = open("IF01.txt", "w") 
    for i in range(len(Liste01)):
        for b in range(len(liste)):
            if str(liste[b][0]) == Liste01[i]:
                file01.write(f"{liste[b][0]} {liste[b][1]}\n")
    file01.close()

    file02 = open("NO02.txt", "w") 
    for i in range(len(Liste02)):
        for b in range(len(liste)):
            if str(liste[b][0]) == Liste02[i]:
                file02.write(f"{liste[b][0]} {liste[b][1]}\n")
    file02.close()

    file03 = open("NE03.txt", "w") 
    for i in range(len(Liste03)):
        for b in range(len(liste)):
            if str(liste[b][0]) == Liste03[i]:
                file03.write(f"{liste[b][0]} {liste[b][1]}\n")
    file03.close()

    file04 = open("SE04.txt", "w") 
    for i in range(len(Liste04)):
        for b in range(len(liste)):
            if str(liste[b][0]) == Liste04[i]:
                file04.write(f"{liste[b][0]} {liste[b][1]}\n")
    file04.close()

    file05 = open("SO04.txt", "w") 
    for i in range(len(Liste05)):
        for b in range(len(liste)):
            if str(liste[b][0]) == Liste05[i]:
                file05.write(f"{liste[b][0]} {liste[b][1]}\n")
    file05.close()
    return

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cette fonction compte et extrait l'ensemble des villes pour le département 12. Cette fonction retourne un tableau comportent l'ensemble des villes département
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def extract_ville_NumDepart(numéro, liste):
    compteur = 0 # Initialisation du compteur
    result = []
    ville_12 = open("ville_12.txt", "w") # On créer un fichier afin d'inserer l'ensemble des villes du département de Aveyron (12)
    for i in range(len(liste)): # Pour chaque tableau
        if str(liste[i][0]) == numéro: # On le compare aux numéro du département 
            compteur +=1  # Si celui la est juste au augmente le compteur de 1
            ville_12.write(f"{liste[i]}\n") #Puis on ajoute l'ensemble de ses informations dedans
            result.append(liste[i]) #On l'ajoute aussi dans un tableau
    ville_12.close()
    """print(f"Il y a {compteur} de villes dans le département numéro {numéro}")""" #Si nous souhaitons afficher la valeur du nombre ville il faut décommenter cette ligne
    return result
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cette fonction donne l'ensemble des 5 petites villes et des 5 plus grosse villes
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

def Min5Villes_Habitants(numéro,liste):
    table =[]
    result =[]
    tab = extract_ville_NumDepart(numéro,liste) #On récupere l'ensemble des villes de nos département
    table = tri(tab) # On importe la fonction de tri
    
    fichier_2 = open("Min5Villes_ n°12.txt", "w") # On insere les 5 plus petites villes du département numéro 12  dans un fichier et dans un tableau
    for j in range (5):
        fichier_2.write(f"{table[j]}\n")
        result.append(table[j])
    fichier_2.close

def Max5Villes_Habitants(numéro,liste):
    table =[]
    result =[]
    tab = extract_ville_NumDepart(numéro,liste) #On récupere l'ensemble des villes de nos département
    table = tri(tab) # On importe la fonction de tri
    
    fichier_1 = open("Max5Villes_ n°12.txt", "w")  # On insere les 5 plus grosses villes du département numéro 12 dans un fichier et dans un tableau
    for j in range (5):
        fichier_1.write(f"{table[len(table)-(1+j)]}\n")
        result.append(table[len(table)-(1+j)])
    fichier_1.close()
    return result  # On retourne un tableau

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cette fonction tri l'ensemble du nombres d'habitant en 2010 et retourne le tableau
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def tri(tab): 
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(tab[j][3]) > int(tab[j+1][3]) : # le [3] signifie que nous voulons trier par rapport à la fonction
                tab[j], tab[j+1] = tab[j+1], tab[j]  # Elle bouge les valeurs en fonction
    return tab 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cette fonction créer un fichier html avec une carte sur la région et sur définit les 5 plus grosses villes et 5 plus petites villes de la région et ajoute un cercle
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def mapMax5Villes(tab):
    tab_color= ["#FFE901","#FFAA0C","#FF923E","#FF7901","#FF0010"]
    m = folium.Map(location=[44.34116285530782, 2.7151862201520194],zoom_start=9)
    for i in range(5):
        folium.CircleMarker([float(tab[i][9]), float(tab[i][8])],color=tab_color[i],radius=i+3, popup=tab[i][1]).add_to(m)
        m.add_child(folium.ClickForMarker(popup="Waypoint"))
    m.save('Max_5_villes.html')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cette fonction créer un fichier html avec une carte sur la région et sur définit les 5 plus petites villes de la région et ajoute un cercle
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def mapMin5Villes(tab):
    tab_color= ["#FFE901","#FFAA0C","#FF923E","#FF7901","#FF0010"]
    m = folium.Map(location=[44.34116285530782, 2.7151862201520194],zoom_start=9)
    for i in range(5):
        folium.CircleMarker([float(tab[i][9]), float(tab[i][8])],color=tab_color[i],radius=i+3, popup=tab[i][1]).add_to(m)
        m.add_child(folium.ClickForMarker(popup="Waypoint"))
    m.save('Min_5_villes.html')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cette fonction affiche les 10 villes ayant pris le plus d'habitant entre 1999 et 2010 et retourne un tableau et puis l'inscrit dans un fichier texte
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def TopAcc10Villes(numéro,liste):
    file = open("TopAcc10Villes_ n°12.txt", "w") 
    tab = extract_ville_NumDepart(numéro,liste)
    result_calcul = []
    for i in range ((len(tab))):
        result_calcul.append(tab[i][5] - tab[i][4]) #Il calcul pour chaque ville la différence entre 2010 et 1999
    result = tri_2 (result_calcul)
    temp = []
    resultat = []
    for j in range (10):
        temp.append(result[i-(0+j)])

    for a in range (len(temp)):
        for b in range (len(tab)):
            if temp[a] == (tab[b][5] - tab[b][4]):
                file.write(f"{tab[b][1], tab[b][5] - tab[b][4]}\n")
                resultat.append(tab[b][1])
    file.close()
    return resultat

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cette fonction affiche les 10 villes ayant pris le perdu le plus d'habitant entre 1999 et 2010 et retourne un tableau et puis l'inscrit dans un fichier texte
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def TopBaisse10Villes(numéro,liste):
    file = open("TopBaisse10Villes_ n°12.txt", "w") 
    tab = extract_ville_NumDepart(numéro,liste)
    result_calcul = []
    for i in range ((len(tab))):
        result_calcul.append(tab[i][5] - tab[i][4]) #Il calcul pour chaque ville la différence entre 2010 et 1999
    result = tri_2 (result_calcul)
    temp = []
    resultat = []
    for j in range (10):
        temp.append(result[j])

    for a in range (len(temp)):
        for b in range (len(tab)):
            if temp[a] == (tab[b][5] - tab[b][4]):
                file.write(f"{tab[b][1], tab[b][5] - tab[b][4]}\n")
                resultat.append(tab[b][1])
    file.close()
    return resultat

def tri_2(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(tab[j]) > int(tab[j+1]) :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab
def menu ():
    print("\n================ MENU ==================")
    print("taper 1: Extraire les Villes du fichier")
    print("taper 2: Extraire des statistiques Villes d’un département")
    menu = int(input("Choissez les options :"))
    if (menu == 1):
        liste = extraction_villes_csv("villes_france.csv")
        info = extract_infos_villes(liste)
    elif (menu == 2):
        liste = extraction_villes_csv("villes_france.csv")
        info = extract_infos_villes(liste)
        print("\n================ Choisir un département ==================")
        numéro = input()
        print("\n================ SOUS MENU : STATISTIQUES ==================")
        print("taper 1: Lister les 5 Villes ayant le moins d'habitants")
        print("taper 2: Lister les 5 Villes ayant le plus d'habitants")
        print("taper 3: Affiche une carte des 5 plus grosses villes")
        print("taper 4: Affiche une carte des 5 plus petite villes")
        print("taper 5: Affiche un fichier texte sur les 10 villes ayant une baisse de population importante")
        print("taper 6: Affiche un fichier texte sur les 10 villes ayant une plus grosse hausse de population importante")
        sousmenu = int(input("Choissez les options"))
        if (sousmenu == 1):
            result = Min5Villes_Habitants(numéro,info)
            print("Vous trouverez les résultats dans le fichier texte Min5Villes_ n°12.txt")
        elif (sousmenu == 2):
            result = Max5Villes_Habitants(numéro,info)
            print("Vous trouverez les résultats dans le fichier texte Max5Villes_ n°12.txt")
        elif (sousmenu == 3):
            result = Max5Villes_Habitants(numéro,info)
            mapMax5Villes(result)
            print("Vous trouverez une carte en fichier html pour les 5 grosses villes")
        elif (sousmenu == 4):
            result = Min5Villes_Habitants(numéro,info)
            mapMin5Villes(result)
            print("Vous trouverez une carte en fichier html pour les 5 petites villes")
        elif (sousmenu == 5):
            TopBaisse10Villes(numéro,info)
            print("Vous trouverez les résultats dans le fichier texte TopBaisse10Villes_ n°12.txt")
        elif (sousmenu == 6):
            TopAcc10Villes(numéro,info)
            print("Vous trouverez les résultats dans le fichier texte TopAcc10Villes_ n°12.txt")

menu()