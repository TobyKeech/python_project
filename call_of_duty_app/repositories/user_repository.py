from db.run_sql import run_sql
from models.cod_profile import CodProfile
from models.platform import User

def save(user):
    sql = "INSERT INTO users (first_name, last_name, age) VALUES (%s, %s, %s) RETURNING *"
    values = [ user.first_name, user.last_name, user.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['first_name'], row['last_name'], row['age'],row['id'] )
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = User(result['first_name'], result['last_name'], result['age'],result['id'] )
    return user 