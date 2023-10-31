from datetime import datetime


def projectValidate():
    # project has id, title, details, target
    while True:
        id = input("Project id:- \n")
        if id.isdigit():
            break
        else:
            print("Invalid Id")
        
    while True:
        title = input("project title:- \n")
        if isinstance(title, str):
            break
        else:
            print("Invalid Title")
        
    while True:
        details = input("Project details:- \n")
        if isinstance(details, str):
            break
        else:
            print("Invalid details")
            
    while True:
        target = input("project targrt:- \n")
        if target.isdigit():
            break
        else:
            print("Invalid Target")
    
    return [id, title, details, target]

def projTiming():
    format = "%d-%m-%Y"
    while True:
        date = input('enter start date \n')
        try:
            datetime.strptime(str(date), format)
        except:
            print("This is invalid date string format. It should be DD-MM-YYYY")
        else:
            start = datetime.strptime(str(date), format)
            now = datetime.today()
            if now < start:
                break
            else:
                print('start date can\'t be before ', now)
    
    while True:
        date = input('enter end date \n')
        try:
            datetime.strptime(str(date), format)
        except:
            print("This is invalid date string format. It should be DD-MM-YYYY")
        else:
            end = datetime.strptime(str(date), format)
            if start < end:
                break
            else:
                print('end date can\'t be before start date ', start)
    startProj = start.strftime(format)
    endProj = end.strftime(format)
    return startProj, endProj

def createProj(email):
    newProj = projectValidate()
    start, end = projTiming()
    newProj.append(email)
    newProj.append(start)
    newProj.append(end)
    
    projects, projDetails  = [], []

    try:
        file = open('projects.txt')
    except:
        print('file isn\'t exist')
    else:
        fileData = file.readlines()
        for d in fileData:
            projects.append(d.strip('\n'))
        
        for project in projects:
            projDetails = project.split(',')
            if projDetails[0] == newProj[0] and projDetails[4] == email:
                print('project already exist')
                file.close()
                createProj(email)
            elif projDetails[0] == newProj[0] and projDetails[4] != email:
                print('can\'t duplicate project id')
                file.close()
                createProj(email)
        else:
            try:
                file = open('projects.txt', 'a')
            except:
                print('can\'t open projects file')
            else:
                newProj = ','.join(newProj) + '\n'
                file.write(newProj)
                file.close()
                print('new project added')
                viewProj(email)

def viewProj(email):
    print(f'your email {email} has projects: ')
    projects, viewList = [], []
    try:
        file = open('projects.txt')
    except:
        print('can\'t open projects file')
    else:
        data = file.readlines()
        for d in data:
            projects.append(d.strip('\n'))
        
        for project in projects:
            project = project.split(',')
            if project[4] == email:
                viewList.append(project)
    
        else:
            if len(viewList) > 0:
                for l in viewList:
                    print(l)
                print('back to menu')
                projectMenu(email)
            else:
                print('this user has no projects to view\nadd new')
                createProj(email)
                
        
    


def projectMenu(email):
    print("Please, Make Your Choice\n1-Create Project\n2-View Project\n3-Back\n4-Exit")
    choice = input('Enter your choice:- ')
    if choice == '1':
        print('create new project')
        createProj(email)
        
    elif choice == '2':
        print('view your projects')
        viewProj(email)
        
    elif choice == '3':
        print('exit... ')
        exit()
        
    else: 
        print('entered invalid choice')
        projectMenu(email)

