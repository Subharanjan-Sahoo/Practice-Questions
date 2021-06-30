'''
Let’s take a password as a combination of alphanumeric characters along with special characters, and check whether the password is valid or not with the help of few conditions.

Conditions for a valid password are:

Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be atlest 8 .


Input :  Geek12#
Output : Password is valid.

Input :  asd123
Output : Invalid Password !!

'''
def passwordValidation(password):
    SpecialSym = ['@','&','#','$']
    flag = True
    while True:
        if (len(password) < 8):
            print("Password should be more then 8 character")
            flag = False
        if not any(char.islower() for char in password):
            print("Password should have at least one lowercase letter")
            flag = False
        if not any(char.isdigit() for char in password):
            print("Password should have at least one number")
            flag = False
        if not any(char.isupper for char in password):
            print("Password should have at least one lowcase letter")
            flag = False       
        if not any(char in SpecialSym for char in password):
            print("Password should have at list one spical character") 
            flag = False
        if flag:
            return flag

def main():
    password = 'Subha@123'
      
    if (passwordValidation(password)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
if __name__ == '__main__':
    main()