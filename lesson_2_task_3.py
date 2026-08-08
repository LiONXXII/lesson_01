def square(side):
    area = side * side              # сначала посчитали площадь (area)

    if not isinstance(side, int):   # если сторона (side) НЕ целое число
        area = int(area) + 1        # отбрасываем дробную часть и добавляем 1
    return area                     # возвращаем результат


print(square(5))                    # вернет 25
print(square(5.3))                  # вернет 29
print(square(0.5))                  # вернет 1
