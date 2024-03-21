
import subprocess

def terraform_apply():
    try:
        # Define the directory containing Terraform files
        terraform_directory = "c:/Users/ehong/OneDrive/Documents/Devops Projects/Python-program/demo1/Utrains_python_script/python-code-wekk22/lightsail"

        # Initialize Terraform (optional if already initialized)
        subprocess.run(["terraform", "init"], cwd=terraform_directory, shell=True)

        # Apply the Terraform configuration
        subprocess.run(["terraform", "apply", "-auto-approve"], cwd=terraform_directory, shell=True)

        print("Infrastructure created successfully!")

    except Exception as e:
        print("Error occurred while creating infrastructure:", e)

def main():
    try:
        # Run Terraform apply
        terraform_apply()
    except KeyboardInterrupt:
        print("Operation cancelled by user.")

if __name__ == "__main__":
    main()


import subprocess

def terraform_destroy():
    try:
        # Define the directory containing Terraform files
        terraform_directory = "c:/Users/ehong/OneDrive/Documents/Devops Projects/Python-program/demo1/Utrains_python_script/python-code-wekk22/lightsail"

        # Run Terraform destroy
        subprocess.run(["terraform", "destroy", "-auto-approve"], cwd=terraform_directory, shell=True)

        print("Infrastructure destroyed successfully!")

    except Exception as e:
        print("Error occurred while destroying infrastructure:", e)

def main():
    try:
        # Run Terraform destroy
        terraform_destroy()
    except KeyboardInterrupt:
        print("Operation cancelled by user.")

if __name__ == "__main__":
    main()
