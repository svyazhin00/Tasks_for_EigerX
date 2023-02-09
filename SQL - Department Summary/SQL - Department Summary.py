import mysql.connector
from mysql.connector import Error
from config import db_config

def create_db_mysql(db_host, user_name, user_password, db_name = None):
    connections_db = None
    try:
        connections_db = mysql.connector.connect(
            host=db_host,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print('Подлючение - успешно...')
    except Error as connection_error:
        print(f'Подключение не прошло {connection_error}')
    return connections_db

#DataBase creation
conn = create_db_mysql(db_config['mysql']['host'],
                       db_config['mysql']['user'],
                       db_config['mysql']['password']
                       )

cursor = conn.cursor()
create_db_sql_query = 'CREATE DATABASE IF NOT EXISTS {}'.format('Task_2')
cursor.execute(create_db_sql_query)
cursor.close()
conn.close()


conn = create_db_mysql(db_config['mysql']['host'],
                       db_config['mysql']['user'],
                       db_config['mysql']['password'],
                       'Task_2'
                       )

try:
    # Department table creation
    cursor = conn.cursor()
    create_db_sql_query_department = '''
    CREATE TABLE IF NOT EXISTS Department (
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL, 
    PRIMARY KEY (id)
    ) ENGINE = InnoDB'''
    cursor.execute(create_db_sql_query_department)
    conn.commit()

    # Employee table creation
    create_db_sql_query_employee = '''
    CREATE TABLE IF NOT EXISTS Employee (
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL, 
    salary TEXT NOT NULL,
    dept_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (dept_id) REFERENCES Department (id)
    ) ENGINE = InnoDB'''
    cursor.execute(create_db_sql_query_employee)
    conn.commit()

    # Insert into the table Department
    insert_department_table = '''
    INSERT INTO
    `Department` (`name`, `location`)
    VALUES
    ('Executive', 'Sydney'),
    ('Production', 'Sydney'),
    ('Resources', 'Cape Town'),
    ('Technical', 'Texas'),
    ('Management', 'Paris');'''
    cursor.execute(insert_department_table)
    conn.commit()


    # Insert into the table Department
    insert_employee_table = '''
    INSERT INTO
    `Employee` (`name`, `salary`, `dept_id`)
    VALUES
    ('Candice', 4685, 1),
    ('Julia', 2559, 2),
    ('Bob', 4405, 4),
    ('Scarlet', 2350, 1),
    ('Ileana', 1151, 4);'''
    cursor.execute(insert_employee_table)
    conn.commit()

    #Output selection
    select_person_table = '''
    SELECT Department.name, COUNT(Employee.dept_id)
    FROM Department LEFT JOIN Employee
    ON Department.id = Employee.dept_id
    GROUP BY Department.name
    ORDER BY Department.name;
    '''
    cursor.execute(select_person_table)
    query_res = cursor.fetchall()
    print(query_res)

except Error as error:
    print(error)

finally:
    cursor.close()
    conn.close()
