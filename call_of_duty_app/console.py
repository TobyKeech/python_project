from models.cod_profile import CodProfile
from models.user import User
from models.weapon import Weapon

import repositories.user_repository as user_repository
import repositories.weapon_repository as weapon_repository
import repositories.cod_profile_repository as codprofile_repository

user1 = User("Toby", "Keech", 26)
user_repository.save(user1)

user2 = User("Mikey", "Forbes", 40)
user_repository.save(user2)

user3 = User("Lee", "Robertson", 38)
user_repository.save(user3)

weapon1 = Weapon("ISO Hemlock", "Assualt Rifle", "mid caliber", "medium")
weapon_repository.save(weapon1)

weapon2 = Weapon("Signal 50", "Sniper", "high caliber", "long")
weapon_repository.save(weapon2)

weapon3 = Weapon("Sakin", "Assualt Rifle", "mid caliber", "medium")
weapon_repository.save(weapon3)

codprofile1 = CodProfile("BlackRaven", "2434", "1487", "345", user1, weapon1)
codprofile_repository.save(codprofile1)

codprofile2 = CodProfile("MikeyFrbz", "1600", "1400", "450", user2, weapon2)
codprofile_repository.save(codprofile2)

codprofile3 = CodProfile("Mister Lucky Lee", "1500", "1200", "450", user3, weapon3)
codprofile_repository.save(codprofile3)