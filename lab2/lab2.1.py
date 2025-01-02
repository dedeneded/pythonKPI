# Зчитування та обробка CSV-файлу netflix_list.csv

# 1. Зчитуємо файл та розділяємо рядки
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 2. Розділяємо кожен рядок за комами та формуємо список списків
netflix_data = [line.strip().split(',') for line in lines]

# 3. Визначаємо індекс стовпця 'rating'
header = netflix_data[0]  # Перший рядок містить заголовки
rating_index = header.index('rating')

# 4. Використовуємо list comprehension для відбору шоу/фільмів з рейтингом > 7.5
high_rated_shows = [
    row for row in netflix_data[1:]  # Пропускаємо заголовок
    if len(row) > rating_index and row[rating_index].replace('.', '', 1).isdigit() and float(row[rating_index]) > 7.5
]

# 5. Виведемо тільки перші 5 колонок кожного запису
for show in high_rated_shows:
    print(show[:5])  # Виводимо перші 5 колонок
