
============= Concept ==============

==> self

    Definition

    Represents the current object instance.

    Example

    class Product:
        def __init__(self):
            self.name = ""


==> raise

    Definition

    Raises an exception manually.

    When to use

    When validation fails.


===============> Git

pwd = Print word director
ls = list

Git init = Para inicializar 
git add = Prepara un cambio
git commit = Guarda un cambio en el historial
            -Un commit debería representar un cambio lógico y coherente

Git diff = Cambios fuera de staging, cambios que estan en Working tree
Git diff -staged = Cambios entre staging vs ultimo commit

Git show = Muestra el último commit completo y qué cambió
                Especifico: git show fbab48d

Git restore = Permite descartar cambios que todavía no hemos convertido en  un commit.

                INVENTORYPRO
                     │
                     ▼
              ┌─────────────┐
              │ Working Tree│
              │             │
              │ files       │
              └──────┬──────┘
                     │
                  git add
                     │
                     ▼
              ┌─────────────┐
              │   STAGING Area   │
              │             │
              │ files ready │
              │ for commit  │
              └──────┬──────┘
                     │
                 git commit
                     │
                     ▼
              ┌─────────────┐
              │  REPOSITORY │
              │             │
              │  history    │
              └─────────────┘

=> inspeccionar historial

Git log --oneline = Inspecciona historial
Git restore --staged = Lo saca de staging, pero No elimina el cambio en el archivo

=======> Github


                  GitHub ☁️
                     ▲
                     │
                  git push
                     │
                     │
            ┌────────┴────────┐
            │   InventoryPro  │
            │     Git local   │
            └─────────────────┘

git remote add origin <<URL>> = 

origin = Nombre del repositorio remoto
git remote -v = Muestra de donde se va a subir la inf y quien la va a recibir
git push -u origin main :
    git push: Envia nuestros commits al repositorio remoto
    origin: nuestro repositorio remoto de GitHub
    main: la rama que queremos enviar
    -u: Establece oring/main como la rama remota de seguimiento de nuestra rama local main.

git fetch = Consulta los cambios que se tienen en Github vs el repo local
git fetch origin = Consulta el remoto y actu la inf sobre el
NOTA: git fetch
        → actualiza lo que sabemos del remoto

      git pull
        → fetch + integra los cambios   


git pull =  Trae la informacion del remoto y luego intenta integrarla en la rama actual

git branch --v = Muesta inf sobre la rama main y la rama remotaque sigue



===> Glossaire <====

-Head: Es el commit en el que se esta trabajando
-fetch: La direccion desde la que git puede obtener la inf
-push: La direccion don de se enviaran nuestros commits
-stash: Guardar temporalemnte mis cambios locales para que pueda trabajar con un arbol limpio.  git stash
-git stash pop: para recuperar notas

=======> Branches

-git branch <<name>>= crea una rama
-git branch = muestra las ramas actuales y * en que rama estoy
-git switch = cambia de rama
-git branch -d git-practice: eliminar un branch

-git switch -c feature/branch-name:
    1.Crea el branch
    2. cambia a esa rama

-git push -u origin feature/git-workflow:
    git push: Subir commits 
    oring: A nuestro GitHub
    feature/git-workflow: La branch que se quiere publicar
    -u:Relacion entre branch local y remota

M docs/concepts.md = la M significa Modified

-Pull request:
    Solicitud de cambios en mi branch para ponerlos en main

