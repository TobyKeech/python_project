from flask import Flask, render_template, request, redirect
from repositories import cod_profile_repository
# from repositories import user_repositoriy
# from repositories import weapon_repositoriy
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

