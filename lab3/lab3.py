class Node:
    """
    Клас вузла AVL-дерева.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    Клас AVL-дерева з методами для вставки, обертання і балансування.
    """
    def get_height(self, node):
        """
        Обчислює висоту вузла.
        """
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """
        Повертає баланс вузла.
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        """
        Праве обертання навколо вузла y.
        """
        x = y.left
        T2 = x.right

        # Виконуємо обертання
        x.right = y
        y.left = T2

        # Оновлюємо висоти
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        """
        Ліве обертання навколо вузла x.
        """
        y = x.right
        T2 = y.left

        # Виконуємо обертання
        y.left = x
        x.right = T2

        # Оновлюємо висоти
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        """
        Вставка ключа в AVL-дерево з балансуванням.
        """
        # Крок 1: Виконуємо звичайну вставку як у BST
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Крок 2: Оновлюємо висоту вузла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Крок 3: Отримуємо баланс вузла
        balance = self.get_balance(root)

        # Ліве перевантаження
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Праве перевантаження
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Ліво-праве перевантаження
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Право-ліве перевантаження
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def pre_order(self, root):
        """
        Обхід у префіксному порядку для виводу дерева.
        """
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def find_node(self, root, key):
        """
        Пошук вузла за ключем.
        """
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.find_node(root.left, key)
        return self.find_node(root.right, key)

    def rotate_left_at_key(self, root, key):
        """
        Обертання вліво навколо заданого вузла.
        """
        node = self.find_node(root, key)
        if node:
            return self.rotate_left(node)
        print("Вузол не знайдено для обертання вліво.")
        return root

    def rotate_right_at_key(self, root, key):
        """
        Обертання вправо навколо заданого вузла.
        """
        node = self.find_node(root, key)
        if node:
            return self.rotate_right(node)
        print("Вузол не знайдено для обертання вправо.")
        return root


# --- Використання AVL-дерева ---
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    while True:
        print("\n1. Додати елемент у дерево")
        print("2. Показати дерево (префіксний обхід)")
        print("3. Вийти")
        print("4. Обчислити висоту піддерева")
        print("5. Обертання вліво навколо вузла")
        print("6. Обертання вправо навколо вузла")
        
        choice = input("Виберіть опцію: ")
        
        if choice == '1':
            try:
                key = int(input("Введіть число для додавання в AVL-дерево: "))
                root = tree.insert(root, key)
                print(f"Елемент {key} додано у дерево.")
            except ValueError:
                print("Будь ласка, введіть коректне число!")
        
        elif choice == '2':
            print("Префіксний обхід дерева:")
            tree.pre_order(root)
            print()
        
        elif choice == '3':
            print("Вихід із програми.")
            break
        
        elif choice == '4':
            try:
                key = int(input("Введіть ключ вузла для обчислення висоти піддерева: "))
                node = tree.find_node(root, key)
                if node:
                    print(f"Висота піддерева з коренем {key}: {tree.get_height(node)}")
                else:
                    print("Вузол із таким ключем не знайдено.")
            except ValueError:
                print("Будь ласка, введіть коректне число!")
        
        elif choice == '5':
            key = int(input("Введіть ключ вузла для обертання вліво: "))
            root = tree.rotate_left_at_key(root, key)
        
        elif choice == '6':
            key = int(input("Введіть ключ вузла для обертання вправо: "))
            root = tree.rotate_right_at_key(root, key)
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")
