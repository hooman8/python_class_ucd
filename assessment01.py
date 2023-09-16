"""
Hooman Pegahmehr; Week 2, Assessment 01
Demonstrate an understanding of and create reusable code using functions and
call existing or custom packages, functions, and methods in their own
programming environment.
This tiny project tries to create functionality similar to last pass.
Second attempt; moved all the functionalities of the external api internally.
"""
import os
import json
import helper_functions


def ensure_json_file_exists(filename="data.json", default_content=[]):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump(default_content, file, indent=4)


def create_new_site(site, username):
    password = helper_functions.generate_password()
    with open("data.json", "r") as file:
        data = json.load(file)
    new_record = {"site": site, "username": username, "password": password}
    data.append(new_record)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    return f"a new record got created, {new_record}"


def read_all_sites():
    with open("data.json", "r") as file:
        data = json.load(file)
        for entry in data:
            print(entry)


def find_single_site(site):
    with open("data.json", "r") as file:
        data = json.load(file)
        for entry in data:
            if entry["site"] == site:
                return entry
        return f"Site: {site} was not found"


def update_existing_site(site, username, password):
    pass


def delete_site(site):
    pass


# print(create_new_site("gmail.com", "hpegahmehr@gmail.com"))
# print(create_new_site("discover", "hpegahmehr@gmail.com"))
# read_all_sites()
print(find_single_site("gmail.com"))
