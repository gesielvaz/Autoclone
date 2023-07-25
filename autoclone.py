import os
from git import Repo

def clone_repositories(repositories):
    for repository_url in repositories:
        repository_name = repository_url.split("/")[-1].replace(".git", "")
        folder_path = os.path.join(os.getcwd(), repository_name)
        if os.path.exists(folder_path):
            print(f"O repositório {repository_name} já existe. Pulando...")
            continue
        print(f"Clonando o repositório {repository_name}...")
        Repo.clone_from(repository_url, folder_path)
        print(f"Repositório {repository_name} clonado com sucesso!")

#Colocar os links dos repositorios que deseja clonar abaixo
repositories = [
    "https://github.com/seuRepositorio.git",
    
]

clone_repositories(repositories)

#Instalar o python
#Instalar biblioteca  pip install GitPython
