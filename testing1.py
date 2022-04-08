data = {"allo" : ["1", "2", "3"], "bonjour" : ["4", "5", "7"]}

keys_list = list(data.keys())
values_list = list(data.values())
data_list = []
for key in keys_list:
    data_list.append(key)
    for ele in range(0,2):
        data_list.append(data[key][ele])

print(data_list)