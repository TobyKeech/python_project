from db.run_sql import run_sql
from models.cod_profile import CodProfile
from models.platform import Platform

def save(platform):
    sql = "INSERT INTO platforms (type) VALUES (%s) RETURNING *"
    values = [platform.type]
    results = run_sql(sql, values)
    id = results[0]['id']
    platform.id = id
    return platform

def select_all():
    platforms = []
    sql = "SELECT * FROM platforms"
    results = run_sql(sql)
    for row in results:
        platform = Platform(row['type'], row['id'] )
        platforms.append(platform)
    return platforms

def select(id):
    platform = None
    sql = "SELECT * FROM platfroms WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        platform = Platform(result['type'], result['id'] )
    return platform 