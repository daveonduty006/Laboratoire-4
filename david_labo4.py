# Module simulant le principe d'un guichet automatique
def atm():
    # Sous-fonction contrôllant le flux du programme
    def execution():
        data_list = file_read()
        encrypted_list = encryption(data_list)
        file_write(encrypted_list)
        decrypted_list = decryption(encrypted_list)
        data = dictionary(decrypted_list)
        login_id = user_login(data)
        exit = False
        while not exit:
            ACCOUNT_SEL, USER_INPUT = user_menu(data, login_id)
            if USER_INPUT == 1:
                deposit(data, login_id, ACCOUNT_SEL)
            elif USER_INPUT == 2:
                withdrawal(data, login_id, ACCOUNT_SEL)
            elif USER_INPUT == 3: 
                inv_returns(data, login_id, ACCOUNT_SEL)
            elif USER_INPUT == 5:
                exit = True
                print("Bonne journée \U0001F642")
            if USER_INPUT != 5:
                user_sel = input("Désirez-vous faire d'autres opérations? O/N ")
                if user_sel == "N":
                    exit = True
                    print("Bonne journée \U0001F642")
    # Sous-fonction compilant l'information d'une base de données non-encryptée (bd.txt)
    def file_read():
        f = open("bd.txt", "r", encoding="utf8")
        raw_list = f.read().splitlines()
        f.close()
        data_list = []
        for ele in raw_list:
            data_list.append(ele.replace("#", "").replace("%", ""))
        return data_list
    # Sous-fonction sauvegardant des données encryptées dans une base de donnée (bd_encrypt.txt)
    def file_write(encrypted_list):
        f = open("bd_encrypt.txt", "w", encoding="utf8")
        write_list = []
        for ele in encrypted_list:
            f.write(f"{ele}\n")
        f.close()
    # Sous-fonction ajoutant des données encryptées dans la base de données encrypt.txt (ADMIN PRIVILEGE)
    def file_update(encrypted_list):
        f = open("bd_encrypt.txt", "a", encoding="utf8")
        addend_list = []
        for ele in encrypted_list:
            f.write(f"{ele}\n")
        f.close()
    # Sous-fonction réorganisant une liste de données décryptées dans un dictionnaire (data)
    def dictionary(decrypted_list):
        data = {}
        for entry in range(0, len(decrypted_list), 6):
            data[decrypted_list[entry]] = decrypted_list[entry+1:entry+6]
        return data
    # Sous-fonction réorganisant le dictionnaire en une liste prête pour l'encryptage (data_list)
    def dict_to_list(data):
        keys_list = list(data.keys())
        data_list = []
        for key in keys_list:
            data_list.append(key)
            for ele in range(0,5):
                data_list.append(data[key][ele])
        return data_list
    # Sous-fonction offrant une option de log-in pour les utilisateurs et l'administrateur
    def user_login(data):
        login_id = input("Entrez votre numéro de compte à 4 chiffres: ")
        while login_id not in data.keys():
            print("\nErreur d'identification, veuillez recommencer svp\n")
            login_id = input("Entrez votre numéro de compte à 4 chiffres: ")
        login_ps = input("Entrez le mot de passe de votre compte: ")
        while login_ps not in data[login_id]:
            print("\nMot de passe invalide, veuillez recommencer svp\n")
            login_ps = input("Entrez le mot de passe de votre compte: ")
        if login_id == "0000" and login_ps == "admin":
            admin_menu(data)
        return login_id
    # Sous-fonction offrant un menu d'opérations à l'administrateur 
    def admin_menu(data):
        ADMIN_SEL = 0
        while not 1 <= ADMIN_SEL <= 3:
            ADMIN_SEL = int(input(f"\n1. Ajouter un compte\n"
                                  f"2. Enlever un compte\n"
                                  f"3. Changer taux intêret pour compte\n"
                                  f"Choisissez une option: "))
        if ADMIN_SEL == 1:
            new_acc_num = input("\nEntrez le nouveau numéro de compte (max 4ch): ")
            new_acc_ps = input("\nEntrez le mot de passe (lettres min. ou ch): ")
            new_acc_chq_bal = "0"
            new_acc_sav_bal = "0"
            new_acc_inv_bal = "0"
            new_acc = [new_acc_num, new_acc_ps, new_acc_chq_bal, new_acc_sav_bal,\
                       new_acc_inv_bal]
            encrypted_list = encryption(new_acc)
            file_update(encrypted_list)
        if ADMIN_SEL == 2:
            targeted_acc = input("\nEntrez le numéro de compte visé: ")
            data.pop(targeted_acc)
            data_list = dict_to_list(data)
            encrypted_list = encryption(data_list)
            file_write(encrypted_list)
        if ADMIN_SEL == 3:
            targeted_acc = input(f"\nEntrez le numéro de compte visé: ")
            new_interest_rate = input(f"\nEntrez le nouveau taux (sans le symbole%): ")
            data[targeted_acc][4] = new_interest_rate
            data_list = dict_to_list(data)
            encrypted_list = encryption(data_list)
            file_write(encrypted_list)   
    # Sous-fonction offrant un menu d'opérations aux utilisateurs      
    def user_menu(data, login_id):
        exit = False
        while not exit:
            ACCOUNT_SEL = 0
            while not 1 <= ACCOUNT_SEL <= 3:
                ACCOUNT_SEL = int(input(f"\n1. Compte chèque\n"
                                        f"2. Compte épargne\n"
                                        f"3. Compte placements\n"
                                        f"Choisissez le compte: "))
            USER_INPUT = 0
            if ACCOUNT_SEL == 3:
                while not 1 <= USER_INPUT <= 5:
                    print(f"\nLe solde de votre compte: {data[login_id][ACCOUNT_SEL]}$")
                    USER_INPUT = int(input(f"1. Faire un dépot\n"
                                           f"2. Faire un retrait\n"
                                           f"3. Voir retour de placement\n"
                                           f"4. Changer de compte\n"
                                           f"5. Terminer\n"
                                           f"Choisissez une option: "))
                if USER_INPUT != 4:
                    exit = True
            else: 
                while not 1 <= USER_INPUT <= 4:
                    print(f"\nLe solde de votre compte: {data[login_id][ACCOUNT_SEL]}$")
                    USER_INPUT = int(input(f"1. Faire un dépot\n"
                                           f"2. Faire un retrait\n"
                                           f"3. Changer de compte\n"
                                           f"4. Terminer\n"
                                           f"Choisissez une option: "))
                if USER_INPUT != 3:
                    exit = True  
        if ACCOUNT_SEL != 3:
            if USER_INPUT == 4:
                USER_INPUT = 5              
        return ACCOUNT_SEL, USER_INPUT
    # Sous-fonction opérant le dépôt d'argent dans les comptes bancaires des utilisateurs
    def deposit(data, login_id, Acc):
        user_dep = int(input("\nMontant à déposer: "))
        data[login_id][Acc] = str(int(data[login_id][Acc])+user_dep)
        print(f"\nLe solde de votre compte: {data[login_id][Acc]}$")
        data_list = dict_to_list(data)
        encrypted_list = encryption(data_list)
        file_write(encrypted_list)
    # Sous-fonction opérant le retrait d'argent dans les comptes bancaires des utilisateurs
    def withdrawal(data, login_id, Acc):
        user_dep = int(input("\nMontant à retirer: "))
        exit = False
        while not exit:
            if int(data[login_id][Acc])-user_dep < 0:
                print("\nFonds disponibles insuffisants")
                user_dep = int(input("\nMontant à retirer: "))
            else:
                data[login_id][Acc] = str(int(data[login_id][Acc])-user_dep)
                print(f"\nLe solde de votre compte: {data[login_id][Acc]}$")
                exit = True 
        data_list = dict_to_list(data)
        encrypted_list = encryption(data_list)
        file_write(encrypted_list)
    # Sous-fonction affichant les projections sur 5 ans des retours d'investissement aux utilisateurs
    def inv_returns(data, login_id, Acc):
        interest = float(data[login_id][4])
        init_place = int(data[login_id][Acc])
        year_1 = float(init_place+(interest/100*init_place))
        year_2 = float(year_1+(interest/100*year_1))
        year_3 = float(year_2+(interest/100*year_2))
        year_4 = float(year_3+(interest/100*year_3))
        year_5 = float(year_4+(interest/100*year_4))
        print(f"\nSolde actuel = {init_place}$\n"
              f"Taux intêrets = {interest}%\n"
              f"1 an(s) = {year_1:.2f}$\n"
              f"2 an(s) = {year_2:.2f}$\n"
              f"3 an(s) = {year_3:.2f}$\n"
              f"4 an(s) = {year_4:.2f}$\n"
              f"5 an(s) = {year_5:.2f}$\n")
    # Sous-fonction encryptant des données contenues dans une liste (A=B_Z=A, 1=2_9=0)
    def encryption(data_list):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        base10 = "0123456789"
        encrypted_list = []
        for ele in data_list:
            e_ele = ""
            for index in range(len(ele)):
                if ele[index] in alphabet:
                    jindex = alphabet.index(ele[index])
                    if jindex == 25:
                        jindex = 0
                        e_ele += alphabet[jindex]
                    else: 
                        e_ele += alphabet[jindex+1]
                elif ele[index] in base10:
                    kindex = base10.index(ele[index])
                    if kindex == 9:
                        kindex = 0
                        e_ele += base10[kindex]
                    else: 
                        e_ele += base10[kindex+1]
                else:
                    e_ele += ele[index]
            encrypted_list.append(e_ele)
        return encrypted_list
    # Sous-fonction décryptant des données encryptées dans une liste (decrypted_list)
    def decryption(encrypted_list):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        base10 = "0123456789"
        decrypted_list = []
        for ele in encrypted_list:
            d_ele = ""
            for index in range(len(ele)):
                if ele[index] in alphabet:
                    jindex = alphabet.index(ele[index])
                    if jindex == 0:
                        jindex = 25
                        d_ele += alphabet[jindex]
                    else: 
                        d_ele += alphabet[jindex-1]
                elif ele[index] in base10:
                    kindex = base10.index(ele[index])
                    if kindex == 0:
                        kindex = 9
                        d_ele += base10[kindex]
                    else: 
                        d_ele += base10[kindex-1]
                else: 
                    d_ele += ele[index]
            decrypted_list.append(d_ele)
        return decrypted_list 

    execution()


atm()