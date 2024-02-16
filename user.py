current_users = ['John', 'kelvin', 'MILO', 'Addoi', 'KelTon']
new_users = ['John', 'Kreno', 'Maltey', 'Milo', 'Sindy']

for username in new_users:
    if username in current_users:
        print('Enter new username')
    else:
        print('Username is Available')
    