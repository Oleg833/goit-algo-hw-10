# goit-algo-hw-10

## Висновки:
### Завдання 1

- Status: 1, Optimal
- Lemonade units: 30.0
- Fruit juice units: 20.0
- Total Products: 50.0 units

1. **Змінні рішення:** Модель використовує дві змінні рішення: `x1` (кількість одиниць "Лимонаду") та `x2` (кількість одиниць "Фруктового соку").

2. **Функція максимізації:** Метою є максимізація загальної кількості вироблених продуктів, що визначається як `x1 + x2`.

3. **Обмеження ресурсів:** Враховуються обмеження на використання ресурсів, таких як вода, цукор, лимонний сік та фруктове пюре.

4. **Обмеження виробництва:** Враховані обмеження на виробництво кожного виду напою.

Цей код може бути корисним як основа для вирішення подібних задач у виробництві та логістиці, де важливо оптимізувати виробництво з обмеженими ресурсами.

### Завдання 2

- Апроксимоване значення інтеграла: 40.67695
- Інтеграл за 'spi.quad':  40.66667

1. **Апроксимоване значення інтеграла:**
   За допомогою методу Монте-Карло, ми отримали апроксимоване значення інтеграла, яке може слугувати приблизною величиною області під кривою функції в заданих межах. Це значення може змінюватися при різних запусках програми або при зміні кількості випадкових вибірок.

2. **Графік функції та апроксимована площа:**
   Графік дозволяє візуально оцінити форму функції \(f(x) = x^2 + 3x + 10\) та виділити область під кривою, яку ми намагаємося апроксимувати. Межі інтегрування (\(a\) і \(b\)) позначені червоною і синьою пунктирними лініями відповідно.

3. **Точність апроксимації:**
   Точність результату методу Монте-Карло залежить від кількості випадкових вибірок. Збільшення кількості вибірок може підвищити точність, але при цьому збільшується обчислювальний витрати.

В цілому, метод Монте-Карло є потужним інструментом для апроксимації інтегралів, особливо у випадках, коли інші методи можуть бути складні у застосуванні.

