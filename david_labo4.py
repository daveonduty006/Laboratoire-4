#Étape 3 (création de la base de données):
#Vous devez créer une base de donnée avec les information suivantes:
#Numéro_de_compt	Mot_de_passe	Montant_chèque	Montant_épargne	Montant_placement	taux_intérêt
#1234	            voiture1	    100	            1000	        10 000	            1.8%
#3456	            chat123	        150	            2000	        25 000	            3%
#3333	            1234	        5	            100	            1000	            15%
#0000	            admin	        0	            0	            0	                0%
#L'information dans votre base de donnée doit être encryptée en utilisant votre l'algorithme de 
#l'étape 2. Si vous n'avez pas réussi l'encryptage vous pouvez écrire l'information directement.
#Indice:
#Vous pouvez écrire l'information initiale dans un fichier.txt, le lire, le convertir et remplir un 
#nouveau document ou remplacer le document avec l'information encryptée.







def atm():

    def execution():
        encryption()
        f_decrypted = decryption()
        user_id(f_decrypted)
        user_input = user_menu()

        
    def encryption():
        f = open("bd_original.txt", "r", encoding="utf8")

        l_of_lines = f.readlines()
        for index in range(len(l_of_lines)):
            l_of_lines[index] = l_of_lines[index].split()

        del l_of_lines[0]         
        
        f.close()

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        base10 = "0123456789"
        l_of_lines_e = []
        for sublist in l_of_lines:
            sub_l_e = []
            for str in sublist:
                str_e = ""
                for index in range(len(str)):
                    if str[index] in alphabet:
                        jindex = alphabet.index(str[index])
                        if jindex == 25:
                            str_e = str_e + alphabet[jindex+1]
                        else: 
                            str_e = str_e + alphabet[jindex+1]
                    elif str[index] in base10:
                        kindex = int(str[index])
                        if kindex == 9:
                            str_e = str_e + "0"
                        else: 
                            str_e = str_e + base10[kindex+1]
                    else:
                        str_e = str_e + str[index]
                sub_l_e.append(str_e)
            l_of_lines_e.append(sub_l_e)

        f_e = open("bd.txt", "w", encoding="utf8")

        for sublist in l_of_lines_e:
            for str in sublist:
                f_e.write(str + "\n")
        f_e.close()


    def decryption():
        f_e = open("bd.txt", "r")
        f_e_lines = f_e.readlines()

        for index in range(len(f_e_lines)):
            f_e_lines[index] = f_e_lines[index].split()

        print(f_e_lines)

        f_e.close()

        #l_of_lines_e = []
        #start = 0
        #step = 6
        #for index in range(start,len(f_e_lines),step):
        #    l_of_lines_e.append(f_e_lines[index:step])
        #    start = start + 6
        #    step = step + 6

        

        print(l_of_lines_e)

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        base10 = "0123456789"
        f_decrypted = ""
        for index in range(len(f_e_lines)):
            if f_e_lines[index] in alphabet:
                jindex = alphabet.index(f_e_lines[index])
                if jindex == 0:
                    f_decrypted = f_decrypted + "z"
                else:
                    f_decrypted = f_decrypted + alphabet[jindex-1]
            elif f_e_lines[index] in base10:
                kindex = int(f_e_lines[index])
                if kindex == 0:
                    f_decrypted = f_decrypted + "9"
                else:
                    f_decrypted = f_decrypted + base10[kindex-1]   
            else:
                f_decrypted = f_decrypted + f_e_lines[index] 

        return f_decrypted


    def user_id(decrypted_db):
        login_id = input("Entrez votre numéro de compte à 4 chiffres: ")
        login_ps = input("Entrez le mot de passe de votre compte: ")

        while login_id not in decrypted_db and login_ps not in decrypted_db:
            print("\nErreur d'identification, veuillez recommencer svp\n")
            login_id = input("Entrez votre numéro de compte à 4 chiffres: ")
            login_ps = input("Entrez le mot de passe de votre compte: ")


    def user_menu():
        account_sel = ""
        exit = False
        while not exit:
            ACCOUNT_SEL = 0
            while not 1 <= ACCOUNT_SEL <= 3:
                ACCOUNT_SEL = int(input(f"\n1. Compte chèque\n"
                                        f"2. Compte épargne\n"
                                        f"3. Compte placements\n"
                                        f"Choisissez le compte: "))
            USER_INPUT = 0
            while not 1 <= USER_INPUT <= 5: 
                USER_INPUT = int(input(f"\n1. Faire un dépot\n"
                                       f"2. Faire un retrait\n"
                                       f"3. Voir retour de placement\n"
                                       f"4. Changer de compte\n"
                                       f"5. Terminer\n"
                                       f"Choisissez une option: "))
            if USER_INPUT != 4:
                exit = True

        return USER_INPUT

    execution()


atm()