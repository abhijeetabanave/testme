import os
from invoke import run

base_dir = os.getcwd()
project_name = '{{cookiecutter.project_name}}'
repo_dir = '{{cookiecutter.repo_dir}}'
project_path = f'{base_dir}/{project_name}'
repo = '{{cookiecutter.repo_name}}'
run("git init");
run("git add .");
command = "git commit --message {}".format("\"Initial Commit\"")
run(command)
run("git branch -M {}").format(repo);
run("git remote add origin https://abhijeetabanave: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@github.com/abhijeetabanave/testme.git");
run("git push -u origin {}").format(repo);
