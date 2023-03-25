from db.run_sql import run_sql
from models.cod_profile import CodProfile
from models.platform import User
from models.weapon import Weapon

def save(weapon):
    sql = "INSERT INTO weapons (name, type, ammo, range) VALUES (%s,%s, %s, %s) RETURNING *"
    values = [weapon.name, weapon.type, weapon.ammo, weapon.range]
    results = run_sql(sql, values)
    id = results[0]['id']
    weapon.id = id
    return weapon

def select_all():
    weapons = []
    sql = "SELECT * FROM weapons"
    results = run_sql(sql)
    for row in results:
        weapon = Weapon(row['name'], row['type'], row['ammo'],row['range'], row['id'] )
        weapons.append(weapon)
    return weapons

def select(id):
    weapon = None
    sql = "SELECT * FROM weapons WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        weapon = Weapon(result['name'], result['type'], result['ammo'],result['range'], result['id'] )
    return weapon 