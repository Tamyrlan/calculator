
def create_complex():
    while True:
        real_num=(input("Enter real unit of complex number:")) ## adding real unit of a complex number
        if not(real_num.isdigit()):
            print('Error,it is not a number, please try again :(')
            continue
        real_num = int(real_num)
        break
    while True:
        img_num = input('Enter imaginary unit of complex number:') ## adding imaginary unit of complex number
        if not(img_num.isdigit()):
            print('Error,it is no a number,please try again :(')
            continue
        img_num=int(img_num)
        break
    return complex(real_num,img_num)