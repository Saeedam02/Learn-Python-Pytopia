#from termcolor import colored 

Name_list=list()

Options={
    1: 'Quit',
    2: 'Check if I know You',
    3: 'Introduce Yourself to me',
    4: 'Make me forgot you',
    5: 'Print the list of people Iknow',
    }

Options_str='\n'.join([f'{key}- {value}' for key,value in Options.items()])

while True:
    Option = int(input(
        f'Enter your option from the list :\n{Options_str}\n'
    ))
    print()
    if Option == 0:
        print('>>>Bye!')
        break
    elif Option == 1:
        username = input('Please enter your name:')
        if username in Name_list:
            # WE already know the user
            print('>>>I know you!\n')
        else:
            # We don't know you
            print(">>>I don't know you!!\n")
    elif Option == 2:
        username = input('Please enter your name:')
        if username in Name_list:
            # WE already know the user
            print('>>>I know you already!\n')
        else:
            # We don't know you
            Name_list.append(username)
            print(">>>I know you now!\n")
    elif Option == 3:
        username = input('Please enter your name:')
        if username not in Name_list:
            # WE already didn't know the user
            print(">>>I didn't know you!\n")
        else:
            # We know you already
            Name_list.remove(username)
            print(">>>now I don't know you!\n")
