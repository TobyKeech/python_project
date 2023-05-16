# Python Project

Call of Duty Stats Tracker You’ve been tasked with making an app tracker system for a popular video game Call of Duty. This app displays profiles and statistics over a user. Each user has a profile as well as a weapon. It will be able to calculate KD ratio and win rate.

## MVP
You should be able to create a Cod Profile with a user, gamer tag, kills, deaths, rank, weapon. You will also have a User with a first name, last name and age. Finally you will also create a Weapon which will have a user, name, type, ammo and range.
There should be a page where you can see all Profiles and be able to click through to each profile to see the details where you should be able to edit or delete the profile and populate with new information.

## Extensions: 
Be able to add profiles to the tracker 
Be able to display a KD ratio for a profile 
Be able to set a profile as rank prestige or not

## How to run
- open a terminal session
- Clone the repo
- Requires
    - flask (`pip3 flask` if you have pip3 installed. Which you most likely do.)
    - psychopg2 (`pip3 psychopg2`)
    - postgres
- dbcreate shopping_list
- if you want to set up some test data, `run psql -d shopping_list -f shopping_list.sql`
- navigate to the main directory, and type `flask run`
- in Chrome, use the url localhost:4999 (this is the default - check your terminal session - it will tell you which localhost port it's using)

