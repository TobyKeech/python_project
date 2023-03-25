from models.cod_profile import CodProfile
from models.platform import Platform
from models.weapon import Weapon

import repositories.platform_repository as platform_repository
import repositories.weapon_repository as weapon_repository
import repositories.cod_profile_repository as codprofile_repository

platform1 = Platform("PS5")
platform_repository.save(platform1)

platform2 = Platform("Xbox")
platform_repository.save(platform2)

platform3 = Platform("PC")
platform_repository.save(platform3)

weapon1 = Weapon("ISO Hemlock", "Assualt Rifle", "mid caliber", "medium")
weapon_repository.save(weapon1)

weapon2 = Weapon("Signal 50", "Sniper", "high caliber", "long")
weapon_repository.save(weapon2)

weapon3 = Weapon("Sakin", "Assualt Rifle", "mid caliber", "medium")
weapon_repository.save(weapon3)

codprofile1 = CodProfile("BlackRaven", "2434", "1487", "345", platform1, weapon1)
codprofile_repository.save(codprofile1)

codprofile2 = CodProfile("MikeyFrbz", "1600", "1400", "450", platform3, weapon2)
codprofile_repository.save(codprofile2)

codprofile3 = CodProfile("Mister Lucky Lee", "1500", "1200", "450", platform2, weapon3)
codprofile_repository.save(codprofile3)