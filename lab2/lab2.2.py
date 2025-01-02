# Генераторна функція для фільтрації шоу або фільмів
def filter_english_shows_after_2015(data):
    """
    Генерує рядки, що відповідають умовам:
    a) Мова шоу або фільму — англійська.
    b) Тип — серіал або фільм.
    c) Закінчилися після 2015 року.
    """
    # Знаходимо індекси необхідних колонок
    header = data[0]
    language_idx = header.index('language')
    type_idx = header.index('type')
    end_year_idx = header.index('endYear')
    
    # Проходимо по кожному рядку після заголовків
    for row in data[1:]:
        try:
            language = row[language_idx].strip()
            show_type = row[type_idx].strip()
            end_year = row[end_year_idx].strip()
            
            # Перевіряємо умови
            if (
                language == 'English' and
                show_type in ['tvSeries', 'movie'] and
                end_year.isdigit() and int(end_year) > 2015
            ):
                yield row
        except IndexError:
            # Пропускаємо неповні або некоректні рядки
            continue


# 1. Зчитування та обробка CSV-файлу
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 2. Розділяємо кожен рядок за комами та формуємо список списків
netflix_data = [line.strip().split(',') for line in lines]

# 3. Використовуємо генератор для фільтрації
filtered_shows = filter_english_shows_after_2015(netflix_data)

# 4. Виведемо перші 5 результатів
for i, show in enumerate(filtered_shows):
    print(show)
    if i >= 4:  # Зупиняємо після перших 5 результатів
        break
