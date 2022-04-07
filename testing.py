f = open("bd_original.txt", "r", encoding="utf8")

l_of_lines = f.readlines()
# return a list of lines 

for index in range(len(l_of_lines)):
    l_of_lines[index] = l_of_lines[index].split()
# return a list of lists, the sublists are created when \n is spotted
l_of_ls_lines = l_of_lines 
del l_of_ls_lines[0]         
        
f.close()

alphabet = "abcdefghijklmnopqrstuvwxyz"
base10 = "0123456789"
l_of_ls_e = []
for sublist in l_of_ls_lines:
    l_e = []
    for ele in sublist:
        ele_e = ""
        for index in range(len(ele)):
            if ele[index] in alphabet:
                jindex = alphabet.index(ele[index])
                if jindex == 25:
                    jindex = 0
                    ele_e = ele_e + alphabet[jindex]
                else: 
                    ele_e = ele_e + alphabet[jindex+1]
            elif ele[index] in base10:
                kindex = base10.index(ele[index])
                if kindex == 9:
                    kindex = 0
                    ele_e = ele_e + base10[kindex]
                else: 
                    ele_e = ele_e + base10[kindex+1]
            else:
                ele_e = ele_e + ele[index]
        l_e.append(ele_e)
    l_of_ls_e.append(l_e)
# list of lists is now encrypted

f_e = open("bd.txt", "w", encoding="utf8")

for sublist in l_of_ls_e:
    sublist[-1] = sublist[-1] + "\n"
    f_e.writelines(sublist)

f_e.close()





