import re

# Read the file
with open('data.txt', 'r') as file:
    data = file.read()


# Assuming 'data' contains the text from 'data.txt'
contacts = data.strip().split('\n\n')

# Extract names and emails and save them into a list
contact_list = []
for contact in contacts[:5]:  # limiting to first 5 contacts for brevity
    lines = contact.split('\n')
    name = lines[0].strip()
    email = re.search(r'\S+@\S+', contact).group()
    contact_list.append({'Name': name, 'Email': email})

print(contact_list)


