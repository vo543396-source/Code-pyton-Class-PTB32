product = ["apple", "samsung", "lenovo"]
shopping_list = []

def product_list(product):
    for index in range(len(product)):
        print(f"{index}: {product[index]}")



def shopping(shopping_list):
    if not shopping_list:
       print("chua co san pham trong gio hang !!")
    else:
       print("mat hang hang cua ban bao gom la: ")
       for index in range(len(shopping_list)):
          print(f"{index + 1}: { shopping_list[index]}")


def add_shopping_list(product, shopping_list):
    print("dang sach san pham la: ")
    product_list(product)       

    item_index = int(input("nhap san pham ban muon them vao: ")) + 1
    if item_index >= 0 and item_index < len(product):
        selected_item = product[item_index]
        shopping_list.appnd(selected_item)
        print(f"{selected_item} da dc them vao gio hang cua ban")
    else:
        print("san pham khong hop le ")


def remove_item(shopping_list):
    if not shopping_list:
        print("gio hang cua ban dang trong ")
    else:
        print("cac san pham co trong gio hang la: ")
        shopping(shopping_list)
        item_index = int(input("nhap vi tri san pham ban muon xoa: ")) - 1
        if item_index >= 0 and item_index < len(shopping_list):
            delete_item = shopping_list.pop(item_index)
            print(f"{delete_item} da duoc xoa ra khoi cua hang")
        else:
            print("khong hop le !")

# goi ham remove_item(shopping_list)


#ham quan ly chuong trinh
def main():
    product = ["apple", "samsung", "lenovo"]
    shopping_list = []
    while True:
        print("1.xem dang sach san pham")
        print("2:xem gio hang")
        print("3.them san pham vao gio hang")
        print("4.xoa san pham ra khoi gio hang") 
        print("5.thoat") 
        Choice = int(input("nhap tinh nang ban muon chon:"))

        if Choice == 1:
            product_list(product)
        elif Choice == 2:
            shopping(shopping_list)
        elif Choice == 3:
            add_shopping_list(product, shopping_list)
        elif Choice == 4:
            remove_item(shopping_list)
        elif Choice == 5:
            break
main()