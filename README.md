# Module19.6Karaseva
Домашнее задание по теме "Настраиваем СУБД postgre в django" (Карасева А.Д.)

1. Официальный пакет pgsql и PGadmin установлены, выполнено подключение к локальному серверу, создана база данных.
Скриншот прилагается.

![image](https://github.com/user-attachments/assets/61530274-165c-4d40-a716-b45179cca0b0)

2. В Django проекте "For_example" установлен драйвер psycopg2 для работы с базой PGSQL с помощью pip install psycopg2. 
В файле setting.py проекта выполнено подключение к базе данных:

![image](https://github.com/user-attachments/assets/42879341-3f57-4659-87f1-54eabdfc7524)

Созданы и выполнены миграции используя makemigrations и migrate. В базе данных создались технические таблицы Django проекта "For_example":

![image](https://github.com/user-attachments/assets/a7fe5a68-860e-4c55-a0c7-cadaeb504d20)

3. Перенесена модель User в PGSQL.
   
![image](https://github.com/user-attachments/assets/f5a8be50-5a20-438e-a884-23b55f75e1b0)

Таблицы Buyer и Games (на примере предыдущего задания) созданы через конструктор PGadmin и связаны с Джанго проектом (файл models.py).

![image](https://github.com/user-attachments/assets/03c29465-ea3d-4f13-9dc4-440d92a087f7)

![image](https://github.com/user-attachments/assets/b51d60ff-966b-4852-ab30-cb7c290b7e98)

![image](https://github.com/user-attachments/assets/d5e31f7d-db98-4dfc-97ca-eabb2056b722)

4. Django ORM для тестирования запросов: QuerySet запросы сохранены в отдельном файле "QuerySet запросы" в проекте.

   


