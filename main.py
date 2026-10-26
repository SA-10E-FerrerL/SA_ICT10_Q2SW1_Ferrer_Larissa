from pyscript import document

def candidate_checker(e):
    club_members = ["Lara Ferrer", "Czyke Lizarda", "Marinette Dupain-Cheng", "Adrien Agreste", "Alya Césaire", "Nino Lahiffe", "Luka Couffaine","Katniss Everdeen", "Peeta Mellark", "Diana Akari", "Lea Johnson"]
    
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value # fron the html
    candidate_name = first_name + ' ' + last_name # concatenates everything together to make a full name
    checker = candidate_name.title() in club_members # asks if Charlie is in the club members in there
    messages = (f'Sorry {candidate_name}, your name is not on the list of club members.', f'Congratulations {candidate_name}, you are a member of the club!') #0 or 1
    document.getElementById("output").innerHTML = messages[checker] # displays the message in the result div tag
