# 14. Program to create an acronym or abbreviation for the name 'Python For Everyone':

def create_acronym(name):
    acronym = ""
    for word in name.split():
        acronym += word[0].upper()
    return acronym

# Input name
name = "Python For Everyone"

# Create acronym
acronym = create_acronym(name)

# Print the acronym
print("Acronym for 'Python For Everyone':", acronym)