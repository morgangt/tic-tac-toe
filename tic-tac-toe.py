pol = {
    "a": [None, None, None], 
    "b": [None, None, None], 
    "c": [None, None, None]
}


def print_pol(map_item):
    print("  1|2|3")
    
    for key, line in map_item.items():
        complit_line = ""
        for index, l in enumerate(line):
            complit_line += l if l else "_"
            if index < 2:
                complit_line += "|"
        print(f"{key} {complit_line}")


def check_win(map_item, symbol):
    is_win_left_diaganl = 0
    is_win_rigth_diaganl = 0
    is_win_vertical = [None, None, None]
    index_left = 0
    index_rigth = 2
    
    for item in map_item.values():
        if item == [symbol, symbol, symbol]:
            return True
            
        if item[index_left] == symbol:
            is_win_left_diaganl += 1

        if item[index_rigth] == symbol:
           is_win_rigth_diaganl += 1
        
        index_left += 1
        index_rigth -= 1

    for i in range(3):
        if map_item["a"][i] == symbol and map_item["b"][i] == symbol and map_item["c"][i] == symbol:
            return True
            
    if is_win_left_diaganl == 3 or is_win_rigth_diaganl == 3:
        return True
        
    return False


print_pol(pol)
user_symbol = "X"


while True:
    user_step = input(f"Ваш ход - {user_symbol}: ")
    error_message = "Неверный ход, попрубуй ещё"
    
    try:
        if not pol[user_step[0]][int(user_step[1])-1]:
            pol[user_step[0]][int(user_step[1])-1] = user_symbol
        else:
            print(error_message)
            continue
    except (KeyError, IndexError):
        print(error_message)
        continue

    
    is_win = check_win(pol, user_symbol)
    if is_win:
        print_pol(pol)
        print(f"Выйграли {user_symbol}!")
        break
    
    user_symbol = "X" if user_symbol == "O" else "O"
    print_pol(pol)
