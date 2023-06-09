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
- if you want to set up some test data, `run psql -d call_of_duty -f stats_tracker.sql`
- navigate to the main directory, and type `flask run`
- in Chrome, use the url localhost:4999 (this is the default - check your terminal session - it will tell you which localhost port it's using)

## Example: 
Static images of the application when running:
<img width="1440" alt="Screenshot 2023-06-09 at 09 13 38" src="https://github.com/TobyKeech/python_project/assets/124391586/b9cbb96c-022a-4641-afd2-3787634b3e92">
<img width="1440" alt="Screenshot 2023-06-09 at 09 13 56" src="https://github.com/TobyKeech/python_project/assets/124391586/32f3de2b-422c-4f30-8b5a-d5dd168f6f95">
<img width="1440" alt="Screenshot 2023-06-09 at 09 14 09" src="https://github.com/TobyKeech/python_project/assets/124391586/68190578-c105-48fc-9349-df53b19513bd">
<img width="1440" alt="Screenshot 2023-06-09 at 09 14 20" src="https://github.com/TobyKeech/python_project/assets/124391586/22fd95c8-aefa-41c1-afaa-b4c22c372698">
<img width="1440" alt="Screenshot 2023-06-09 at 09 14 28" src="https://github.com/TobyKeech/python_project/assets/124391586/8aa7b128-52d7-40ce-ba13-bcaad1b2b711">





