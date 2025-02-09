import csv

# 1) Create a list for compromised users
compromised_users = []

# 2) Open passwords.csv and read it using csv.DictReader
with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)

    # 3) Loop through each row, grabbing the 'Username' column
    for password_row in password_csv:
        compromised_users.append(password_row["Username"])

# 4) Write all compromised users to a new file: compromised_users.txt
with open("compromised_users.txt", "w") as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + "\n")

# 5) Import JSON
import json

# 6) Create boss_message.json with a dictionary
with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {
        "recipient": "The Boss",
        "message": "Mission Success"
    }
    json.dump(boss_message_dict, boss_message)

# 7) Create a multiline “signature” string
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

# 8) Open new_passwords.csv in write mode and write the signature
with open("new_passwords.csv", "w") as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)