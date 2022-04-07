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

        # code source: https://pynative.com/python-count-number-of-lines-in-file/
        # user: Vishal
        with open('bd_original.txt', 'r', encoding="utf8") as fp:
            for count, line in enumerate(fp):
                pass
        line_count = count + 1

        l_of_keys = []
        for line in range(line_count):
            key = f.readline(5)
            l_of_keys.append(key)


        for ele in range(len(f_lines)):
            l_of_removes = ["\t", "\n", " ", "[", "]", ",", "'", "#", "%"]
            for remove in l_of_removes:
                f_lines[ele] = f_lines[ele].replace(remove, "")            
        
        f.close()

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        base10 = "0123456789"
        f_encrypted = []
        for ele in f_lines:
            ele_e = ""
            for index in range(len(ele)):
                if ele[index] in alphabet:
                    jindex = alphabet.index(ele[index])
                    if jindex == 25:
                        ele_e = ele_e + alphabet[jindex+1]
                    else: 
                        ele_e = ele_e + alphabet[jindex+1]
                elif ele[index] in base10:
                    kindex = int(ele[index])
                    if kindex == 9:
                        ele_e = ele_e + "0"
                    else: 
                        ele_e = ele_e + base10[kindex+1]
                else:
                    ele_e = ele_e + ele[index]
            f_encrypted.append(ele_e)

        print(f_encrypted)

        f_e = open("bd.txt", "w")
        f_e.write(f_encrypted)
        f_e.close()


    def decryption():
        f_e = open("bd.txt", "r")
        f_e_lines = f_e.read()
        f_e.close()

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