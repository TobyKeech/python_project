from flask import Flask, render_template, request, redirect
from repositories import cod_profile_repository
from repositories import platform_repository
from repositories import weapon_repository
from models.cod_profile import CodProfile

from flask import Blueprint

codprofiles_blueprint = Blueprint("", __name__)

@codprofiles_blueprint.route("/codprofiles")
def codprofiles():
    codprofiles = cod_profile_repository.select_all() 
    return render_template("codprofiles/index.html", all_codprofiles = codprofiles)

@codprofiles_blueprint.route("/codprofiles/<id>")
def show_profile(id):
    codprofile = cod_profile_repository.select(id)
    return render_template("codprofiles/show.html", solo_profile= codprofile)

@codprofiles_blueprint.route("/codprofiles/<id>/delete", methods=['POST'])
def delete_profile(id):
    cod_profile_repository.delete(id)
    return(redirect("/codprofiles"))

@codprofiles_blueprint.route("/codprofiles/new")
def new_profile():
    platforms = platform_repository.select_all()
    weapons = weapon_repository.select_all()
    return render_template("codprofiles/new.html", all_weapons = weapons, all_platforms = platforms)

@codprofiles_blueprint.route("/codprofiles", methods=['POST'])
def create_codprofile():
    gamer_tag = request.form['gamer_tag']
    kills = request.form['kills']
    deaths = request.form['deaths']
    rank = request.form['rank']

    platform_id = request.form['platform']
    platform = platform_repository.select(platform_id)

    weapon_id = request.form['weapon_id']
    weapon = weapon_repository.select(weapon_id)
    
    
    new_codprofile = CodProfile(gamer_tag, kills, deaths, rank, platform, weapon)
    cod_profile_repository.save(new_codprofile)
    return redirect("/codprofiles")

@codprofiles_blueprint.route("/codprofiles/<id>/edit")
def edit_profile(id):
    codprofile = cod_profile_repository.select(id)
    platforms = platform_repository.select_all()
    weapons = weapon_repository.select_all()
    return render_template("codprofiles/edit.html", codprofile= codprofile, all_weapons = weapons, all_platforms = platforms)



# @codprofiles_blueprint.route("/codprofiles/<id>", methods=["POST"])
# def update_codprofile(id):
#     gamer_tag = request.form["gamer_tag"]
#     kills = request.form['kills']
#     deaths = request.form['deaths']
#     rank = request.form['rank']
#     user = request.form['user']
#     weapon_id = request.form['weapon_id']

#     weapon = weapon_repository.select(weapon_id)
#     codprofile = CodProfile(gamer_tag, kills, deaths, rank, user, weapon,id)

#     cod_profile_repository.update(codprofile)
#     return redirect("/codprofiles")
