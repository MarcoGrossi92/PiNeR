# INI file manager

import configparser
import json

# Function : check section presence -----------------------------------
def check_section(file_path, section):
    config = configparser.ConfigParser()
    config.read(file_path)

    # Check if the specified section exists in the INI file
    switch = True
    if section not in config:
        switch = False

    return switch

# Function : check section presence -----------------------------------


# Function : check option value -----------------------------------

def check_option(file_path, option, value):
    config = configparser.ConfigParser()
    config.read(file_path)

    # Check if the specified value of the input option exists in the INI file
    found = False
    for section_ in config:
        for option_ in config[section_]:
            if (option==option_):
                if (config[section_][option]==value):
                    section = section_
                    found = True

    if not found: return None

    # Return the value of the section
    return section

# Function : check option value -----------------------------------


# Function : get INI option -----------------------------------

def get(file_path, section, option, as_type=str):
    config = configparser.ConfigParser()
    config.read(file_path)

    if section not in config:
        return None

    if option not in config[section]:
        return None

    raw = config[section][option]
    
    # Use the `as_type` argument to specify the desired data type
    if as_type == int:
        value = int(raw)
    elif as_type == float:
        value = float(raw)
    elif as_type == bool:
        # Convert common boolean representations to actual boolean values
        value = raw in ('true', 'yes', '1', 'on', 'T', 'True')
    elif as_type == list:
        # Check if input is a list of floats
        value = [float(x) for x in raw.split(' ')]
    else:
        value = raw
    
    return value
    

# Function : get INI option -----------------------------------


# CONVERSION FUNCTIONS


# Function : INI to JSON -----------------------------------
def ini_to_json(file_path, json_file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    data = {}
    for section in config.sections():
        data[section] = {}
        for option in config.options(section):
            data[section][option] = config.get(section, option)

    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
# Function : INI to JSON -----------------------------------

# Function : JSON to INI -----------------------------------
def json_to_ini(json_file_path, ini_file_path):
    # Read JSON data from the file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Create a new ConfigParser object
    config = configparser.ConfigParser()

    # Iterate through the JSON data and write it to the ConfigParser object
    for section, section_data in data.items():
        config[section] = section_data

    # Write the INI data to the file
    with open(ini_file_path, 'w') as ini_file:
        config.write(ini_file)
# Function : JSON to INI -----------------------------------
