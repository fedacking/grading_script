# Grading Script

## Requisitos

- Instalar los requisitos de python definidos en requirements.txt
- Tener autorizada la conexion ssh a la cuenta de github con acceso a los repos de los alumnos.


## Ayuda

    usage: grade_fork.py [-h] [-l LABS_TEST] [alumno]

    Programa que descarga el repo de uno o varios alumnos y corre labs-tests

    positional arguments:
      alumno                Nombre del repo del alumno. Formato "fiubatps/sisop_2022a_gauna" Si no esta, se lee del archivo repos.txt

    optional arguments:
      -h, --help            show this help message and exit
      -l LABS_TEST, --labs_test LABS_TEST                        Carpeta con la direccion de los labs-tests. Si no esta, se descarga automaticamente.