def roll_call_dwarves(list):
    count = 1
    for dwarf in list:
        print(f"{count}. {dwarf}")
        count += 1

def summon_captain_planet(list):
    new_list = [(n.capitalize() + '!') for n in list]
    return new_list

def long_planeteer_calls(list):
    new_list = [n for n in list if len(n) > 4]
    response = len(new_list) > 0
    return response

def find_the_cheese(list):
    Cheeses = ["cheddar", "gouda", "camembert"]
    for n in list:
        if n in Cheeses:
            return n

    return None
