# Генератор для фільтрації шоу за кількістю епізодів і рейтингом
def filter_shows_by_episodes_and_rating(data, average_rating):
    """
    Генерує заголовки шоу, що відповідають умовам:
    a) Мають більше 10 епізодів.
    b) Рейтинг вище середнього.
    """
    # Індекси необхідних колонок
    header = data[0]
    title_idx = header.index('title')
    episodes_idx = header.index('episodes')
    rating_idx = header.index('rating')
    
    for row in data[1:]:
        try:
            episodes = row[episodes_idx].strip()
            rating = row[rating_idx].strip()
            
            # Перевірка умов
            if (episodes.isdigit() and int(episodes) > 10 and 
                rating.replace('.', '', 1).isdigit() and float(rating) > average_rating):
                yield row[title_idx]
        except IndexError:
            continue  # Пропускаємо некоректні рядки


# 1. Зчитування файлу
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 2. Розділяємо дані
netflix_data = [line.strip().split(',') for line in lines]

# 3. Обчислюємо середній рейтинг
header = netflix_data[0]
rating_index = header.index('rating')

# Середній рейтинг за допомогою comprehension
average_rating = sum(
    float(row[rating_index]) for row in netflix_data[1:] 
    if len(row) > rating_index and row[rating_index].replace('.', '', 1).isdigit()
) / sum(
    1 for row in netflix_data[1:] 
    if len(row) > rating_index and row[rating_index].replace('.', '', 1).isdigit()
)

# 4. Використовуємо генератор для фільтрації
filtered_titles = list(filter_shows_by_episodes_and_rating(netflix_data, average_rating))

# 5. Виведемо список заголовків
print("Заголовки шоу, які мають більше 10 епізодів і рейтинг вище середнього:")
for title in filtered_titles:
    print(title)
