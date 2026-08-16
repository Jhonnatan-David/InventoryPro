
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


===> Glossaire <====

Head: Es el commit en el que se esta trabajando