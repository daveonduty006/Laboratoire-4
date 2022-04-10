# Module simulant le principe d'un guichet automatique
def atm():
    # Sous-fonction contrôllant le flux du programme
    def execution():
        decrypted_list = file_read()
        data = dictionary(decrypted_list)
        login_id, ADMIN_ACCESS = user_login(data)
        if not ADMIN_ACCESS:
            acc_menu(data, login_id)
        decrypted_list = dict_to_list(data)
        encrypted_list = encryption(decrypted_list)
        file_write(encrypted_list)        
        print("Bonne journée \U0001F642")
    # Sous-fonction compilant l'information d'une base de données (bd_unencrypted.txt on initial boot, encrypted bd.txt thereafter)
    def file_read():
        try:
            with open("bd_unencrypted.txt", "r") as f:
                raw_list = f.read().splitlines()
                f.close()
                decrypted_list = []
                for ele in raw_list:
                    decrypted_list.append(ele.replace("#", "").replace("%", ""))
                return decrypted_list
        except FileNotFoundError:
            f = open("bd.txt", "r")
            encrypted_list = f.read().splitlines()
            f.close()
            decrypted_list = decryption(encrypted_list)
            return decrypted_list
    # Sous-fonction sauvegardant des données encryptées dans une base de donnée (bd.txt)
    def file_write(encrypted_list):
        f = open("bd.txt", "w")
        for ele in encrypted_list:
            f.write(f"{ele}\n")
        f.close()
    # Sous-fonction ajoutant des données non-encryptées dans la base de données !!!ADMIN PRIVILEGE!!!
    def file_update(encrypted_list):
        f = open("bd.txt", "a")
        for ele in encrypted_list:
            f.write(f"{ele}\n")
        f.close()
    # Sous-fonction réorganisant une liste de données dans un dictionnaire (data)
    def dictionary(decrypted_list):
        data = {}
        for key in range(0, len(decrypted_list), 6):
            data[decrypted_list[key]] = decrypted_list[key+1:key+6]
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
        ADMIN_ACCESS = None
        login_id = input("\nEntrez votre numéro de compte à 4 chiffres: ")
        while login_id not in data.keys():
            print("Numéro de compte invalide, veuillez recommencer svp")
            login_id = input("Entrez votre numéro de compte à 4 chiffres: ")
        login_ps = input("Entrez le mot de passe de votre compte: ")
        while login_ps not in data[login_id]:
            print("Mot de passe invalide, veuillez recommencer svp")
            login_ps = input("Entrez le mot de passe de votre compte: ")
        if login_id == "0000" and login_ps == "admin":
            ADMIN_SEL = admin_menu(data)
            ADMIN_ACCESS = ADMIN_SEL
        return login_id, ADMIN_ACCESS
    # Sous-fonction offrant un menu d'opérations à l'administrateur 
    def admin_menu(data):
        exit = False
        while not exit:
            ADMIN_SEL = int(input(f"\n1. Ajouter un compte\n"
                                  f"2. Enlever un compte\n"
                                  f"3. Changer taux intêret pour compte\n"
                                  f"4. Terminer\n"
                                  f"Choisissez une option: "))
            if ADMIN_SEL == 1: 
                add_acc(data)
            elif ADMIN_SEL == 2:
                rem_acc(data)
            elif ADMIN_SEL == 3:
                mod_int(data)
            elif ADMIN_SEL == 4:
                exit = True
        return ADMIN_SEL
    # Sous-fonction permettant de créer un nouveau compte et de l'ajouter, encryptée, à la base de données !!!ADMIN PRIVILEGE!!!
    def add_acc(data):
        new_acc_num = input("\nEntrez le nouveau numéro de compte (max 4ch): ")
        new_acc_ps = input("Entrez le mot de passe (lettres min. ou ch): ")
        new_acc_chq_bal = "0"
        new_acc_sav_bal = "0"
        new_acc_inv_bal = "0"
        new_acc_int_rate = "0"
        new_acc = [new_acc_num, new_acc_ps, new_acc_chq_bal, new_acc_sav_bal,\
                   new_acc_inv_bal, new_acc_int_rate]              
        encrypted_list = encryption(new_acc)
        file_update(encrypted_list) 
        data[new_acc_num] = [new_acc_ps, new_acc_chq_bal, new_acc_sav_bal,\
                           new_acc_inv_bal, new_acc_int_rate]    
    # Sous-fonction permettant d'effacer le compte d'un utilisateur après un log-off de l'administrateur !!!ADMIN PRIVILEGE!!!
    def rem_acc(data):
        targeted_acc = input("\nEntrez le numéro du compte visé: ")
        while targeted_acc not in data.keys():
            print("Numéro de compte invalide")
            targeted_acc = input("Entrez le numéro du compte visé: ")
        data.pop(targeted_acc)
    # Sous-fonction permettant de modifier le taux d'intêret d'un utilisateur après un log-off de l'administrateur !!!ADMIN PRIVILEGE!!!
    def mod_int(data):
        targeted_acc = input("\nEntrez le numéro du compte visé: ")
        while targeted_acc not in data.keys():
            print("Numéro de compte invalide")
            targeted_acc = input("Entrez le numéro du compte visé: ")
        new_int = input("Entrez le nouveau taux (sans le symbole %): ")
        while "%" in new_int: 
            new_int = input("Entrez le nouveau taux (sans le symbole %): ")
        data[targeted_acc][4] = new_int
    # Sous-fonction offrant un menu de sélection de compte à l'utilisateur 
    def acc_menu(data, login_id):
        acc_sel = 0
        while not 1 <= acc_sel <= 3:
            print("1. Compte Chèque")
            print("2. Compte Épargne")
            print("3. Compte Placements")
            acc_sel = int(input("Choisissez un compte: "))
        op_menu(data, login_id, acc_sel)
    # Sous-fonction offrant un menu de navigation dans le compte choisi par l'utilisateur 
    def op_menu(data, login_id, acc_sel):
        if acc_sel == 3:
            print(f"Solde disponible: {data[login_id][3]}$")            
            user_sel = 0
            while not 1 <= user_sel <= 5:
                print("1. Faire un dépôt")
                print("2. Faire un retrait")
                print("3. Voir mon retour de placement")
                print("4. Changer de compte")
                print("5. Terminer")
                user_sel = int(input("Choisissez une option: "))
            if user_sel == 1:
                deposit(data, login_id, acc_sel)
                op_menu(data, login_id, acc_sel)
            elif user_sel == 2:
                withdrawal(data, login_id, acc_sel)
                op_menu(data, login_id, acc_sel)
            elif user_sel == 3:
                inv_returns(data, login_id, acc_sel)
                op_menu(data, login_id, acc_sel)
            elif user_sel == 4:
                acc_menu(data, login_id)
            else:
                return        
        elif acc_sel != 3:
            print(f"Solde disponible: {data[login_id][acc_sel]}$")   
            user_sel = 0
            while not 1 <= user_sel <= 4:
                print("1. Faire un dépôt")
                print("2. Faire un retrait")
                print("3. Changer de compte")
                print("4. Terminer")
                user_sel = int(input("Choisissez une option: "))
            if user_sel == 1:
                deposit(data, login_id, acc_sel)
                op_menu(data, login_id, acc_sel)
            elif user_sel == 2:
                withdrawal(data, login_id, acc_sel)
                op_menu(data, login_id, acc_sel)
            elif user_sel == 3:
                acc_menu(data, login_id)
            else:
                return       
    # Sous-fonction permettant le dépôt d'argent dans les comptes bancaires des utilisateurs
    def deposit(data, login_id, Acc):
        user_dep = int(input("\nMontant à déposer: "))
        data[login_id][Acc] = str(int(data[login_id][Acc])+user_dep)
        print(f"\nLe solde de votre compte: {data[login_id][Acc]}$")
    # Sous-fonction permettant le retrait d'argent dans les comptes bancaires des utilisateurs
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
    # Sous-fonction encryptant des données contenues dans une liste (encrypted_list) *(A=B_Z=A, 1=2_9=0)*
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