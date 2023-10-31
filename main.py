import re
from projects import projectMenu


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pass_reg = re.compile("^[A-Za-z\d@$!#%?&]{6,20}$")
phone_regex = re.compile(r"^0?[10,11,12]\d{9}")

# validation 
def nameValidate(type):
    while True:
        name = input(f'your {type} name \n')
        if name.isalpha() and len(name) >= 3:
            break
        else:
            print('enter valid name with more than 3 char')
    return name

            
def emailValidate():
    while True:
        email = input('your email \n')
        if re.fullmatch(email_regex, email):
            break
        else:
            print('enter valid email')
    return email

def passwordValidate():
    while True:
        password = input('your password \n')
        if re.search(pass_reg, password):
            break
        else:
            print('invalid password\nyour password should be between 6 to 20 characters long.')
    return password

def phoneValidate():
    while True:
        phone = input('your phone number \n')
        if re.search(phone_regex, phone):
            break
        else:
            print('invalid phone number\nyour phone should be 10 numbers.')
    return phone


def userExisting(newUser):
    email = newUser[2]
    try:
        file = open('users.txt')
    except:
        print('can\'t open users file')
    else:
        lines = file.readlines()
        users, userDetails = [], []
        
        for l in lines:
            users.append(l.strip('\n'))
        
        # email existance check
        for user in users:
            userDetails = user.split(',')
            if userDetails[2] == email:
                file.close()
                print('this user is already exist\n2-Login ')
                login()
                break
            
        # in case the user is new
        else: 
            try:
                file = open('users.txt','a')
            except:
                print('can\'t open users file')
            else:
                newUser = ','.join(newUser) + '\n'
                file.write(newUser)
                file.close()
                print('user added')
                projectMenu(email)
                
                
                
# registrayion function
def registration():
    fname = nameValidate('first')
    lname = nameValidate('last')
    email = emailValidate()
    password = passwordValidate()
    phone = phoneValidate()
    
    newUser = [fname, lname, email, password, phone]
    userExisting(newUser)
    
    
    
def login():
    email = emailValidate()
    password = passwordValidate()
    
    try:
        file = open('users.txt')
    except:
        print('can\'t open users file')
    else:
        lines = file.readlines()
        users = []
        userDetails = []

        for l in lines:
            users.append(l.strip('\n'))

        for user in users:
            userDetails = user.split(',')
            if userDetails[2] == email and userDetails[3] == password:
                print('loged in successfully')
                file.close()
                projectMenu(email)
                break
        else:
            print('you have to register first\n 1-Registration')
            registration()
            
            

# main menu to chooice
def main():
    print('Choose:- \n1-Registration \n2-Login \n3-Exit')
    choice = input('Enter your choice:- ')
    if choice == '1':
        registration()
        
    elif choice == '2':
        login()
    
    elif choice == '3':
        print('exit... ')
        exit()
        
    else: 
        print('entered invalid choice')
        main()

# start project
print('Crowd fund project\n') 
main()
