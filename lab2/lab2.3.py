# Ітератор для фільтрації акторського складу
class CastIterator:
    def __init__(self, data):
        self.data = data[1:]  # Пропускаємо заголовки
        self.cast_index = data[0].index('cast')  # Індекс колонки cast
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current < len(self.data):
            row = self.data[self.current]
            self.current += 1
            try:
                cast = row[self.cast_index].strip()
                if len(cast) > 50:  # Перевірка довжини
                    return cast
            except IndexError:
                continue  # Пропускаємо некоректні рядки
        raise StopIteration


# Функція для підрахунку шоу/фільмів для дорослих і середнього рейтингу
def analyze_adult_and_rating(data):
    """
    a) Підраховує кількість шоу/фільмів для дорослих.
    b) Розраховує середній рейтинг для шоу та фільмів з більше ніж 1000 голосів.
    """
    # Індекси необхідних колонок
    header = data[0]
    is_adult_idx = header.index('isAdult')
    rating_idx = header.index('rating')
    num_votes_idx = header.index('numVotes')
    
    adult_count = 0
    total_rating = 0
    rating_count = 0
    
    for row in data[1:]:
        try:
            # Підрахунок для дорослих
            if row[is_adult_idx].isdigit() and int(row[is_adult_idx]) == 1:
                adult_count += 1
            
            # Підрахунок середнього рейтингу
            if (row[num_votes_idx].replace('.', '', 1).isdigit() and 
                float(row[num_votes_idx]) > 1000 and 
                row[rating_idx].replace('.', '', 1).isdigit()):
                total_rating += float(row[rating_idx])
                rating_count += 1
        except IndexError:
            continue  # Пропускаємо некоректні рядки
    
    average_rating = total_rating / rating_count if rating_count > 0 else 0
    return adult_count, average_rating


# --- Використання ітератора та функції ---

# 1. Зчитування файлу
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 2. Розділяємо дані
netflix_data = [line.strip().split(',') for line in lines]

# 3. Використання ітератора для виводу 10 акторських складів
print("Перші 10 акторських складів з довжиною > 50 символів:")
cast_iterator = CastIterator(netflix_data)
for i, cast in enumerate(cast_iterator):
    print(f"{i+1}. {cast}")
    if i >= 9:  # Показати тільки 10 записів
        break

# 4. Використання функції для аналізу
adult_count, average_rating = analyze_adult_and_rating(netflix_data)
print("\nАналіз датасету:")
print(f"Кількість шоу/фільмів для дорослих: {adult_count}")
print(f"Середній рейтинг шоу/фільмів з більше ніж 1000 голосів: {average_rating:.2f}")
