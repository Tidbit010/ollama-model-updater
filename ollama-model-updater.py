import subprocess
import time

# Function to run shell commands and get the output
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode('utf-8')}")
    return stdout.decode('utf-8'), stderr.decode('utf-8'), process.returncode

# Function to update models
def update_models():
    confirmation = input("Are you sure you want to update your models? (yes/no): ")
    if confirmation.lower() != 'yes':
        print("Update cancelled.")
        return

    # Get the list of models
    list_command = "ollama list"
    models_output, models_error, exit_code = run_command(list_command)

    if exit_code != 0:
        print("Failed to get the list of models.")
        return

    # Parse the output to get model names
    models = [line.split()[0] for line in models_output.strip().split('\n')[1:]] # skipping the header

    # Iterate through the models and update them one by one
    for model in models:
        print(f"Updating model: {model}")
        pull_command = f"ollama pull {model}"
        pull_output, pull_error, exit_code = run_command(pull_command)
        if exit_code != 0:
            print(f"Failed to update model: {model}")
        else:
            print(f"Model updated: {model}")
        print(pull_output)  # print the output in real time
        time.sleep(1)  # wait for the command to complete

# Run the update models function
update_models()

