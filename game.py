# Functions: ini_pencils,

num_pencils = 0
first_g = " "
second_g = " "
end_game = False


def ini_pencils():
    validation = False
    print("How many pencils would you like to use: ")
    while not validation:
        str_pencils = input()
        if str_pencils.isdigit() and str_pencils != "0":
            validation = True
            int_pencils = int(str_pencils)
            break
        elif str_pencils.isdigit() and str_pencils == "0":
            print("The number of pencils should be positive")
        else:
            print("The number of pencils should be numeric")
            validation = False
    return int_pencils


def first_player():
    valid_players = ['John', 'Jack']
    validation = False
    print("Who will be the first (John, Jack): ")
    while not validation:
        first = input()
        if first not in valid_players:
            print("Choose between 'John' and 'Jack'")
        else:
            validation = True
            break
    return first


def valid_take(num_p):
    possible_values = ["1", "2", "3"]
    str_take = " "
    end_game = False
    while not end_game:
        str_take = input()
        if str_take not in possible_values or str_take == "0":
            print("Possible values: '1', '2' or '3'")
        elif str_take in possible_values:
            if num_p == 0:
                end_game = True
                break
            elif int(str_take) > num_p:
                print('Too many pencils were taken')
            elif int(str_take) <= num_p:
                return int(str_take)
        else:
            break


def game(num_p):
    end = False
    current = first_g
    while not end:
        if num_p == 0:
            print(f"{current} won!")
            break
        print("|" * num_p)
        print(f"{current}'s turn")
        if current == "John":
            current = "Jack"
        else:
            current = "John"
        num_p -= valid_take(num_p)



num_pencils = ini_pencils()
first_g = first_player()
game(num_pencils)




