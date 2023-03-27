from flask import Flask, render_template, redirect, request
from repositories import cod_profile_repository
from repositories import platform_repository
from repositories import weapon_repository
from models.weapon import Weapon

from flask import Blueprint

weapons_blueprint = Blueprint("weapons", __name__)

@weapons_blueprint.route("/weapons")
def weapons():
    weapons = weapon_repository.select_all() 
    return render_template("weapons/index.html", all_weapons = weapons)

@weapons_blueprint.route("/weapons/<id>")
def show_weapon(id):
    weapon = weapon_repository.select(id)
    return render_template("weapons/show.html", solo_weapon= weapon)