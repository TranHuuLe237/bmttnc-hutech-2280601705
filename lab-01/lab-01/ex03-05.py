def demsolanxuathien(lst):
    count_dict ={}
    for item in lst:
        if item in count_dict:
            count_dict[item] +=1
        else:
            count_dict[item]=1
            return count_dict
        
        input_string = input("Nhap danh sach, cach nhau boi dau cach: ")
        word_list= input_string.split()
        
        solanxuathien=demsolanxuathien(word_list)
        print("so lan xuat hien la: ",solanxuathien)