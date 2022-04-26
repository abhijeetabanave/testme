import os

import invoke

base_dir = os.getcwd()
project_name = '{{cookiecutter.project_name}}'
repo_dir = '{{cookiecutter.repo_dir}}'
project_path = f'{base_dir}/{project_name}'
repo = '{{cookiecutter.repo_name}}'

    
invoke.run("git init");
command = "git commit --message {}".format(quote("initial commit"))
invoke.run("git add --all")
invoke.run(command)
invoke.run("git remote add origin {}".format(repo))
invoke.run(
        "git remote add origin {}".format(
        quote("https://abhijeetabanave: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@github.com/abhijeetabanave/testme.git")
    )
)
invoke.run("git push -u origin {}".format(repo))

