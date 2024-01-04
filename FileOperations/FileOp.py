# update server.config file properties

def updateServerConfig(filePath, key, value):
    # Read the existing content of the server configuration file
    with open(filePath, "r") as file:
        lines = file.readlines()
    
    # Update the configuration value for the specified key
    with open(filePath, "w") as file:
        for line in lines:
            # Check if the line starts with the specified key
            if key in line:
                # Update the line with the new value
                file.write(key + "="+value+"\n")
            else:
                # Keep the existing line as it is
                file.write(line)

# Path to the server configuration file
server_config_file = 'Server.conf'

# Key and new value for updating the server configuration
key_to_update = 'TIMEOUT'
new_value = '50'  # New maximum connections allowed

# Update the server configuration file

updateServerConfig(server_config_file, key_to_update,new_value)