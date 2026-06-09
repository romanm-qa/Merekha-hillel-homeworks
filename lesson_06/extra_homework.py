python_students = {"Олексій", "Марія", "Ярослав", "Олена", "Дмитро"}
qa_students = {"Ярослав", "Олена", "Ірина", "Максим", "Дмитро"}

''' Завдання 1.1: "Універсальні бійці"
Знайди студентів, які одночасно навчаються і на курсі Python, і на курсі QA.'''
# Знаходимо студентів, які є в обох курсах
universal_students = python_students & qa_students
print(universal_students)

'''Завдання 1.2: "Списки на розсилку"
Адміністрації академії потрібно зібрати повний список усіх унікальних студентів обох курсів, 
щоб надіслати їм спільне оголошення. Дублікатів імен у списку бути не повинно.'''
# Збираємо всіх унікальних студентів обох курсів без дублікатів
all_unique_students = python_students | qa_students
print(all_unique_students)

'''Завдання 2.1: "Суто програмісти"
Знайди студентів, які вчать Python, але взагалі не цікавляться курсом QA.'''
# Знаходимо студентів, які навчаються тільки на курсі Python
python_only_students = python_students - qa_students
print(python_only_students)

'''Завдання 2.2: "Тільки один курс"
Знайди студентів, які обрали для себе тільки один напрямок (або суто Python, або суто QA), тобто 
виключи тих, хто ходить на обидва курси одночасно.'''
# Знаходимо студентів, які навчаються тільки на курсі QA
qa_only_students = qa_students - python_students
# Збираємо студентів, які обрали лише один курс
students_with_one_course = qa_only_students | python_only_students
print(students_with_one_course)

'''Завдання 3: "Аналітика SaaS-платформи" (Велика задача)
Уяви, що ти працюєш над SaaS-платформою. У тебе є три списки ID користувачів:
active_users — ті, хто заходив на платформу цього місяця.
premium_users — ті, хто купив преміум-підписку.
churned_users — ті, хто написав у саппорт і видалив акаунт.

Тобі потрібно написати код, який відповість на 3 питання бізнесу:
- Які преміум-користувачі були активними цього місяця? (Кому не дарма капає підписка).
- Які преміум-користувачі взагалі не заходили на платформу? (Їм треба надіслати email-нагадування, 
бо вони скоро скасують підписку).
- Чи є серед активних користувачів ті, хто вже офіційно вважається видаленим (churned_users)? 
(Якщо є, то це критичний баг у базі даних!).'''
active_users = [101, 102, 105, 107, 110, 120]
premium_users = [102, 105, 110, 115, 130]
churned_users = [105, 140, 115]

active_users = set(active_users)
premium_users = set(premium_users)
churned_users = set(churned_users)

# Знаходимо преміум-користувачів, які були активними цього місяця
active_premium_users = active_users & premium_users
print(f"Active premium users: {active_premium_users}")

# Знаходимо преміум-користувачів, які не заходили на платформу
inactive_premium_users = premium_users - active_users
print(f"Inactive premium users: {inactive_premium_users}")

# Знаходимо користувачів, які одночасно є активними та видаленими
active_churned_users = active_users & churned_users
print(f"Active churned users: {active_churned_users}")