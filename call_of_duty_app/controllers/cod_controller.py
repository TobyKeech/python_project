from flask import Flask, render_template, request, redirect
from repositories import cod_profile_repository
# from repositories import user_repositoriy
# from repositories import weapon_repositoriy
from models.cod_profile import CodProfile

from flask import Blueprint

codprofiles_blueprint = Blueprint("codprofiles", __name__)

@codprofiles_blueprint.route("/codprofiles")
def codprofiles():
    codprofiles = cod_profile_repository.select_all() 
    return render_template("codprofiles/index.html", all_codprofiles = codprofiles)

