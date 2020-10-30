#!/usr/bin/env python
from past.builtins import raw_input

db = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    db[name] = pwd


def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        print('welcome back', name)
    else:
        print('login incorrect')

def showmenu():
    prompt = " (N)ew User Login\n(E)xisting User Login\n(Q)uit\nEnter choice:"
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                print("Error")
            else:
                if choice == 'q':
                    print('\nYou picked: [%s]' % choice)
                if choice not in 'neq':
                    print('invalid option, try again')
                else:
                    chosen = True
                    done = True
                    newuser()
                    olduser()

if __name__ == '__main__':
    showmenu()