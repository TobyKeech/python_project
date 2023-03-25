from db.run_sql import run_sql
from models.cod_profile import CodProfile

import repositories.platform_repository as platform_repository
import repositories.weapon_repository as weapon_repository

def save(codprofile):
    sql = "INSERT INTO codprofiles (gamer_tag, kills, deaths, rank, platform_id, weapon_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [ codprofile.gamer_tag, codprofile.kills, codprofile.deaths, codprofile.rank, codprofile.platform.id, codprofile.weapon.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    codprofile.id = id
    return codprofile

def select_all():
    codprofiles = []
    sql = "SELECT * FROM codprofiles"
    results = run_sql(sql)
    for row in results:
        platform = platform_repository.select(row['platform_id'])
        weapon = weapon_repository.select(row['platform_id'])
        codprofile = CodProfile (row['gamer_tag'], row['kills'],row['deaths'], row['rank'], platform, weapon, row['id'])
        codprofiles.append(codprofile)
    return codprofiles

def select(id):
    codprofile = None
    sql = "SELECT * FROM codprofiles WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        selected_codprofile = results[0]
        user = platform_repository.select(selected_codprofile['user_id'])
        weapon = weapon_repository.select(selected_codprofile['weapon_id'])
        codprofile = CodProfile (selected_codprofile['gamer_tag'], selected_codprofile['kills'],
                                 selected_codprofile['deaths'], selected_codprofile['rank'],
                                    user, weapon, selected_codprofile['id'])
    return codprofile

def delete(id):
    sql = "DELETE  FROM codprofiles WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(codprofile):
    sql = "UPDATE codprofiles SET (gamer_tag, kills, deaths, rank, user_id, weapon_id) VALUES (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [codprofile.gamer_tag, codprofile.kills, codprofile.deaths, codprofile.rank,codprofile.user_id, codprofile.weapon_id]
    run_sql(sql, values)