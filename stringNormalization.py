# нормализация строк

user_cities = ['Г москва', 'город москва', 'МоСкВа', 'г Москва', 'г.москва', 'Москва']
def city_normalization(city_string, city_name):
    normalized_string = city_string.lower()
    index = normalized_string.find(city_name)
    if index != -1:
        return city_name
    else:
        return None
for elem in user_cities:
    print("До:",elem, "После:", city_normalization(elem,user_cities))
