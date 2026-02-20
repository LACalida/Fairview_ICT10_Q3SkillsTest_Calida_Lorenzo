from pyscript import display, document

def submit(e):
    e.preventDefault() 

    document.getElementById("output").innerHTML = ""  # Clear previous output

    username = document.getElementById("username").value
    unamelength = len(username)
    password = document.getElementById("pw").value
    needed = 7 - unamelength  
    # check if all fields are answered
    if username == "" or password == "":
         display(f"Please fill in all fields. / Mangyaring punan ang lahat ng mga patlang.", target="output")
    if unamelength < 7:

        display(
            f"Username must be at least 7 characters long. / Ang username ay dapat hindi bababa sa 7 karakter. "
            f"Please add {needed} more character/s to your username. / Mangyaring magdagdag ng {needed} pang karakter sa iyong username.",
            target="output"
        )

    elif password.isalpha():
        display(f"Password must have at least ONE number and ONE letter. / Ang password ay dapat magkaroon ng hindi bababa sa ISANG numero at ISANG titik.", target="output")

    elif password.isdigit():
        display(f"Password must have at least ONE number and ONE letter. / Ang password ay dapat magkaroon ng hindi bababa sa ISANG numero at ISANG titik.", target="output")

    elif password.isalnum() and len(password) >= 8 and username.isalnum() and len(username) >= 7:
        display(f"Congratulations! You may now continue. / Pagbati! Maaari nang magpatuloy.", target="output")

    else:
        display(f"Password must be at least 8 characters long and contain both letters and numbers. / Ang password ay dapat hindi bababa sa 8 karakter at magkaroon ng mga titik at numero.", target="output")
    
    # Show the output div
    document.getElementById("output").classList.remove("d-none")