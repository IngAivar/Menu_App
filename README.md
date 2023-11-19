# Menu App

## Древовидное меню в Django

ТЗ 
```
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас недостаточно знаний.
Задание выложить на гитхаб.
```

### Стек
![python version](https://img.shields.io/badge/Python-3.10-yellow)
![django version](https://img.shields.io/badge/Django-4.17-blue)


### Запуск проекта в dev-режиме
Инструкция ориентирована на операционную систему windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/artyom-vah/tree_menu.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 

```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. Создайте суперюзера, зайдите в админку
```
python manage.py createsuperuser
```

6. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

7. Перейдите в админку и добавьте несколько пунктов и подпунктов ваших менюшек

8. При переходе по адресу http://127.0.0.1:8000/main_menu/
будет выведено:
```
main_menu
    Опция_1
        подопция_1.1
        подопция_1.2
    Опция_2
        подопция_2.1
    Опция_3
        подопция_3.1
        подопция_3.2
        подопция_3.3
            подопция_3.3(1)
```

Пример готового проекта:

***Админка:***
<img src="https://github.com/IngAivar/Menu_App/blob/dev_2/imgs/admin_1.png" alt="Описание картинки" width="900"/>
<img src="https://github.com/IngAivar/Menu_App/blob/dev_2/imgs/admin_2.png" alt="Описание картинки" width="900"/>
<img src="https://github.com/IngAivar/Menu_App/blob/dev_2/imgs/admin_3.png" alt="Описание картинки" width="900"/>

***Вывод в браузер:***
<img src="https://github.com/IngAivar/Menu_App/blob/dev_2/imgs/brows.png" alt="Описание картинки" width="400"/>

