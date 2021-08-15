import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

alltask = ['0. Easy1', '1. Easy2', '2. Easy3.1', '3. Easy3.2', '4. Easy3.3', \
            '5. Easy3.4', '6. Easy3.5', '7. Easy3.6', '8. Easy4', '9. Medium1']
print('All Tasks')
for t in alltask:
    print(t, end='   ')
print('')

# select tasks
def selection():
    ans = True
    while ans == True:
        try:
            ct = int(input('Please choose one task number 0-9: '))
            if ct >= 0 and ct <= 9:
                r.sadd('tasks', ct)
            else:
                print('The number out of range 0-9.')
        except:
            print('Finished Selection.\nInput is not an integer.')
            ans = False
        r.smembers('tasks')
    return taskShow()

# delete tasks
def deletion():
    try:
        print('You want to delete some tasks?')
        b = int(input("No = 0\tYes = 1 : "))
        if b in [0, 1]:
            ans = bool(b)
        else:
            ans = ynError()
    except:
        ans = ynError()

    while ans == True:
        try:
            ct = int(input('Please choose one task number: '))
            if str(ct) in r.smembers('tasks'):
                r.srem('tasks', ct)
            else:
                print('This number has not been selected.')
            # print(f'{alltask[ct]} is deleted')
        except:
            print('Finished Deletion\nInput is not an integer.')
            ans = False
        
    return taskShow()

# show choose tasks
def taskShow():
    tasks = [int(t) for t in r.smembers('tasks')]
    tasks.sort()
    print('All tasks you select: ', end=' ')
    for t in tasks: 
        print(alltask[t], end='   ')
    print('')
    return tasks

def ynError():
    try:
        b = int(input("Please input '0' or '1' : "))
        if b in [0, 1]:
            ans = bool(b)
        else:
            ans = ynError()
    except:
        ans = ynError()
    return ans

if __name__ == '__main__':

    if len(r.smembers('tasks')) == 0:
        ans = True
    else:
        tasks = taskShow()
        print('Do you want to change the tasks?')
        try:
            b = int(input("No = 0\tYes = 1 : "))
            if b in [0, 1]:
                ans = bool(b)
            else:
                ans = ynError()
        except:
            ans = ynError()

    if ans == True:
        r.delete('tasks')
        tasks = selection()
        tasks = deletion()
    
    import func

    for t in tasks: 
        print('\n',alltask[t],': ', end='')
        if t == 0:
            func.showNum()
        elif t == 1:
            func.leapyear()
        elif t == 2:
            func.star1()
        elif t == 3:
            func.star2()
        elif t == 4:
            func.star3()
        elif t == 5:
            func.star4()
        elif t == 6:
            func.star5()
        elif t == 7:
            func.alpha()
        elif t == 8:
            func.specific()
        elif t == 9:
            func.primeNum()
print('\n---------------------')
print('See you next time!')

