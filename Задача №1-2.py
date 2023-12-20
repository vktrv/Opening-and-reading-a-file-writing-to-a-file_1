from pprint import pprint
def dict_collector(file_path):
    with open(file_path, 'r',encoding ='utf 8' ) as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = file_work.readline().strip().split(' | ')
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline()

    return(menu)

def get_shop_list_by_dishes(dishes, persons=int):
    menu = dict_collector('recipes.txt')
    print('Меню ресторана:')
    pprint(menu)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'quantity': int(item['quantity'])*persons, 'measure': item['measure']})])

                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) + int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    shopping_list.update(items_list)

        print(f"Чтобы приготовить блюдо на {persons} персон нужно купить:")
        pprint(shopping_list)
    except KeyError:
        print("Нет таких блюд")

dict_collector('recipes.txt')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)