## L2: Unittest Features

### Что это за тема
Как объединять тесты в классы и наборы (Test Case / Test Suite), 
как выполнять подготовку/уборку до и после тестов (fixtures), 
какие есть встроенные проверки (asserts) в unittest, 
и как пропускать тесты или помечать их как "ожидаемо падающие".

---

### Установка
`unittest` — встроенный модуль Python с версии 2.1, устанавливать не нужно.

Важно: unittest автоматически находит тесты только в файлах, 
имя которых начинается с `test_` (например, `test_login.py`).

---

### Test Case (тест-кейс)

Все проверки в unittest объединяются в **тест-кейсы**.
Тест-кейс — это класс, унаследованный от `unittest.TestCase`.
Каждый метод класса, начинающийся с `test_`, будет распознан как отдельный тест.

```python
import unittest

class TestCaseClass(unittest.TestCase):

    def test_1(self):
        pass

    def test_2(self):
        pass
```

Наследование от `unittest.TestCase` даёт доступ ко всем методам проверки (asserts).

---

### Asserts (проверки)

Вместо обычного `assert` в unittest используются свои методы проверки. 
Все они доступны через `self`, так как наследуются от `unittest.TestCase`.

| Assert | Аналог | Появился в Python |
|---|---|---|
| `assertEqual(a, b)` | `a == b` | — |
| `assertNotEqual(a, b)` | `a != b` | — |
| `assertTrue(x)` | `bool(x) is True` | — |
| `assertFalse(x)` | `bool(x) is False` | — |
| `assertIs(a, b)` | `a is b` | 3.1 |
| `assertIsNot(a, b)` | `a is not b` | 3.1 |
| `assertIsNone(x)` | `x is None` | 3.1 |
| `assertIsNotNone(x)` | `x is not None` | 3.1 |
| `assertIn(a, b)` | `a in b` | 3.1 |
| `assertNotIn(a, b)` | `a not in b` | 3.1 |
| `assertIsInstance(a, b)` | `isinstance(a, b)` | 3.2 |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` | 3.2 |

Пример использования:

```python
import unittest

class TestCaseClass(unittest.TestCase):

    def test_1(self):
        # проверяем, что 1 есть в списке
        self.assertIn(1, [2, 1, 4])

    def test_2(self):
        # проверяем, что a и b — один и тот же объект
        a = b = 1
        self.assertIs(a, b)

    def test_3(self):
        # проверяем равенство значений
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertEqual(a, b)
```

---

### Test Fixture (подготовка и уборка)

Fixture — это подготовка окружения перед тестами и уборка после них.
Для этого в `unittest.TestCase` есть 4 метода:

- `setUpClass()` — выполняется **один раз** перед всеми тестами класса
- `tearDownClass()` — выполняется **один раз** после всех тестов класса
- `setUp()` — выполняется **перед каждым** тестом
- `tearDown()` — выполняется **после каждого** теста

`setUpClass` и `tearDownClass` — методы класса, поэтому помечаются декоратором `@classmethod`.

```python
import unittest

class TestCaseClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Test Case "TestCaseClass" has started.')

    @classmethod
    def tearDownClass(cls):
        print('Test Case "TestCaseClass" has finished.')

    def setUp(self):
        print('Check {} has started.'.format(self._testMethodName))

    def tearDown(self):
        print('Check {} has finished.'.format(self._testMethodName))

    def test_1(self):
        self.assertIn(1, [2, 1, 4])

    def test_2(self):
        a = b = 1
        self.assertIs(a, b)

    def test_3(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertEqual(a, b)
```

Вывод при запуске покажет порядок выполнения:
Test Case "TestCaseClass" has started.
Check test_1 has started.
Check test_1 has finished.
Check test_2 has started.
Check test_2 has finished.
Check test_3 has started.
Check test_3 has finished.
Test Case "TestCaseClass" has finished.

Ran 3 tests in 0.001s
OK


**Важный нюанс про `tearDown()`:**
- Выполняется даже если тест упал с ошибкой.
- Если `tearDown()` сам выбросит исключение (кроме `AssertionError` или `SkipTest`) — это засчитается как отдельная ошибка, а не как провал теста.
- `tearDown()` вызовется только если `setUp()` прошёл успешно.
- То же самое правило действует для пары `setUpClass()` / `tearDownClass()`.

*Простыми словами:* если "подготовка" не удалась — "уборка" не запустится, потому что убирать, по сути, нечего.

---

### Test Suite (набор тестов)

Test Suite — способ объединить несколько тест-кейсов вместе.
Создаётся как объект `unittest.TestSuite()`, а тест-кейсы добавляются через `addTest()`.

Два способа добавить TestCase в TestSuite:

**1. Через `unittest.makeSuite()`:**
```python
suite_1 = unittest.TestSuite()
suite_1.addTest(unittest.makeSuite(TestCaseClass))
```

**2. Через создание экземпляра класса:**
```python
suite_1 = unittest.TestSuite()
suite_1.addTest(TestCaseClass())
```

Можно объединять несколько Suite в один через `addTests()` (обрати внимание — с буквой **s** в конце, метод для нескольких suite сразу):

```python
class AnotherTestCase(unittest.TestCase):
    def test_me(self):
        self.assertEqual(1, 2)

suite_2 = unittest.TestSuite()
suite_2.addTest(unittest.makeSuite(AnotherTestCase))

suite_3 = unittest.TestSuite()
suite_3.addTests([suite_1, suite_2])
```

*Простыми словами:* TestSuite — как папка, в которую можно сложить и отдельные тест-кейсы, и другие папки (suite) с тестами.

---

### ⚠️ Актуализация: `unittest.makeSuite()` устарел

*Этого не было в самом уроке, но важно знать для собеседований.*

`unittest.makeSuite()` — **deprecated** начиная с Python 3.9, 
а в Python 3.13 он полностью удалён из модуля.

Современный способ собрать TestSuite — через `unittest.TestLoader`:

```python
loader = unittest.TestLoader()
suite = loader.loadTestsFromTestCase(TestCaseClass)
```

Если на собеседовании спросят "как собрать TestSuite" — 
лучше сразу отвечать через `TestLoader`, а `makeSuite` упомянуть 
как старый способ, который встречается в легаси-коде.

---

### Дополнительные возможности

**Пропуск тестов (Skip)**

Можно пропустить один тест или весь класс тестов.

- `@unittest.skip(reason)` — пропустить тест безусловно
- `@unittest.skipUnless(condition, reason)` — пропустить, если условие `False`
- `@unittest.skipIf(condition, reason)` — пропустить, если условие `True`

```python
import unittest
import sys

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        pass
```

Пропустить весь класс тестов:

```python
import unittest

@unittest.skip("Whole TestCase class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```

**Ожидаемое падение теста (Expected Failure)**

Иногда тест ДОЛЖЕН падать, чтобы подтвердить корректную работу приложения 
(например: проверка, что нельзя залогиниться с неверным паролем).

Такой тест помечают декоратором `@unittest.expectedFailure`.

```python
import unittest

class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```

Логика такая:
- Тест помечен `@unittest.expectedFailure` → unittest ждёт, что он упадёт.
- Если тест действительно падает → статус **Passed**.
- Если тест неожиданно проходит → статус **Failed**.

---

### Итог темы
Unittest даёт инструменты, чтобы:
- объединять тесты в тест-кейсы и наборы (suite),
- готовить данные перед тестами и убирать за собой после (fixtures),
- проверять результат через встроенные asserts,
- гибко управлять запуском: пропускать тесты или ожидать их падение.