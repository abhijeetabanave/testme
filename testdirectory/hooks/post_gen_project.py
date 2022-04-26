import os
import subprocess

base_dir = os.getcwd()
project_name = '{{cookiecutter.project_name}}'
repo_dir = '{{cookiecutter.repo_dir}}'
project_path = f'{base_dir}/{project_name}'
repo = '{{cookiecutter.repo_name}}'

subprocess.check_call("./sonar.sh %s %s %s" % (str(repo_dir), str(repo)), shell=True)



