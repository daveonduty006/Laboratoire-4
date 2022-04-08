#
def atm():

    def execution():
        data_list = file_read()
        encrypted_list = encryption(data_list)
        file_write(encrypted_list)
        decrypted_list = decryption(encrypted_list)
        data = dictionary(decrypted_list)
        login_id = user_login(data)
        ACCOUNT_SEL, USER_INPUT = user_menu(data, login_id)
        if USER_INPUT == 1:
            deposit(data, login_id, ACCOUNT_SEL)
        elif USER_INPUT == 2:
            withdrawal(data, login_id, ACCOUNT_SEL)


    def file_read():
        f = open("bd.txt", "r", encoding="utf8")
        raw_list = f.read().splitlines()
        f.close()
        data_list = []
        for ele in raw_list:
            data_list.append(ele.replace("#", "").replace("%", ""))
        return data_list

    def file_write(encrypted_list):
        f = open("bd_encrypt.txt", "w", encoding="utf8")
        write_list = []
        for ele in encrypted_list:
            f.write(f"{ele}\n")
        f.close()

    def dictionary(decrypted_list):
        data = {}
        for entry in range(0, len(decrypted_list), 6):
            data[decrypted_list[entry]] = decrypted_list[entry+1:entry+6]
        return data
    
    def dict_to_list(data):
        keys_list = list(data.keys())
        data_list = []
        for key in keys_list:
            data_list.append(key)
            for ele in range(0,5):
                data_list.append(data[key][ele])
        return data_list

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

    def user_login(data):
        login_id = input("Entrez votre numéro de compte à 4 chiffres: ")
        while login_id not in data.keys():
            print("\nErreur d'identification, veuillez recommencer svp\n")
            login_id = input("Entrez votre numéro de compte à 4 chiffres: ")
        login_ps = input("Entrez le mot de passe de votre compte: ")
        while login_ps not in data[login_id]:
            print("\nMot de passe invalide, veuillez recommencer svp\n")
            login_ps = input("Entrez le mot de passe de votre compte: ")
        return login_id

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
        return ACCOUNT_SEL, USER_INPUT

    def deposit(data, login_id, Acc):
        user_dep = int(input("\nMontant à déposer: "))
        data[login_id][Acc] = str(int(data[login_id][Acc])+user_dep)
        print(f"\nLe solde de votre compte: {data[login_id][Acc]}$")
        data_list = dict_to_list(data)
        encrypted_list = encryption(data_list)
        file_write(encrypted_list)

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











        















    execution()


atm()