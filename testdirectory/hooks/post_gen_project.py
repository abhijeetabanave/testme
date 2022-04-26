import os
from invoke import run

base_dir = os.getcwd()
project_name = '{{cookiecutter.project_name}}'
repo_dir = '{{cookiecutter.repo_dir}}'
project_path = f'{base_dir}/{project_name}'
repo = '{{cookiecutter.repo_name}}'

run("git init");
command = "git commit --message {}".format("\"Initial Commit\"")
run("git add --all")
run(command)
run("git remote add origin {}".format(repo))
run(
        "git remote add origin {}".format(
        "\"https://abhijeetabanave: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@github.com/abhijeetabanave/testme.git\""
    )
)
invoke.run("git push -u origin {}".format(repo))



