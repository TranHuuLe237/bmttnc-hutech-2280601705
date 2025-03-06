def daonguoclist(lst):
    return lst[:: -1]

input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(','))) 
list_dao_nguoc = daonguoclist(numbers)
print("List sau khi dao nguoc: ", list_dao_nguoc)