from pyscript import document


# Have pyclick and define the events
# create a div tag for the result for it to display 
#footer is optional but if you want to add a footer, you can do so by creating a footer tag and adding it to the HTML structure.
# specify the club members ??? ig like broo idk 
# event CLICK 


def candidate_checker(e):
    club_members = ["Lara Ferrer", "Czyke Lizarda", "Marinette Dupain-Cheng", "Adrien Agreste", "Alya Césaire", "Nino Lahiffe", "Luka Couffaine","Katniss Everdeen", "Peeta Mellark", "Diana Akari", "Lea Johnson"]
    
    f_name = document.getElementById("first_name").value
    l_name = document.getElementById("last_name").value # fron the html
candidate_name = f_name + ' ' + l_name # concatenates everything together to make a full name
checker = candidate_name.title() in club_members # asks if Charlie is in the club members in there

messages = (f'Sorry {candidate_name}, your name is not on the list of club members.', f'Congratulations {candidate_name}, you are a member of the club!') #0 or 1

document.getElementById("candidate_checker").innerHTML = messages[checker] # displays the message in the result div tag

