def hook_fish():
    print("I got a fish")

def wait():
    print('waiting')

while True:
    response=input("Is bobber underwater? answer yes or no: ")
    if response=='yes':
        is_moving=True
        print('I Got a bite')
        hook_fish()
    else:
        wait()