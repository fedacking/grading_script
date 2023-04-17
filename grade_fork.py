from get_git_repo import get_repo_gh
import subprocess
import argparse
from os import mkdir, path, getcwd
import traceback


class Grade:
    name: str
    build_out: bytes
    build_err: bytes
    test_out: bytes
    test_err: bytes

    def __init__(self, name, build_out, build_err, test_out, test_err) -> None:
        self.name = name
        self.build_out = build_out
        self.build_err = build_err
        self.test_out = test_out
        self.test_err = test_err

def grade_alumno(url_github, tests_folder) -> Grade:
    folder = get_repo_gh(url_github, "entrega_fork") + "/fork"
    subprocess.run(["make", "clean"], cwd=folder, capture_output=True)
    build_res = subprocess.run(["make"], cwd=folder, capture_output=True)
    
    test_res = subprocess.run(
        ["python", "test-fork", path.join(getcwd(),folder)], 
        cwd=tests_folder + "/fork",
        capture_output=True
    )
    name = folder.split("/")[-2]
    return Grade(name, build_res.stdout, build_res.stderr, test_res.stdout, test_res.stderr)

def outpute_grade(grade: Grade):
    filename = "output/" + grade.name + ".out"
    with open(filename, "wb+") as file:
        file.write(b"#####\nBuild Out\n")
        file.write(grade.build_out)
        file.write(b"#####\nBuild Err\n")
        file.write(grade.build_err)
        file.write(b"#####\nTest Out\n")
        file.write(grade.test_out)
        file.write(b"#####\nTest Err\n")
        file.write(grade.test_err)


def main(lab_tests_folder=None, alumno=None):
    if lab_tests_folder == None:
        lab_tests_folder = get_repo_gh("git@github.com:fisop/labs-tests", folder="")
    
    if alumno == None:
        with open("repos.txt", "r+") as file:
            input = [x.strip() for x in file.readlines()]
    else:
        input = [alumno]

    output = []

    if not path.exists("input"):
        mkdir("input")

    if not path.exists("output"):
        mkdir("output")


    for alumno in input:
        try:
            output.append(grade_alumno("git@github.com:" + alumno, lab_tests_folder))
        except Exception as e:
            print(f"Alumno {alumno} fallo error:")
            print(traceback.format_exc())
            

    for out in output:
        outpute_grade(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa que descarga el repo de uno o varios alumnos y corre labs-tests")
    parser.add_argument('alumno', help="Nombre del repo del alumno. Formato \"fiubatps/sisop_2022a_gauna\"\
                        Si no esta, se lee del archivo repos.txt", 
                        nargs="?")
    parser.add_argument('-l', '--labs_test', help="Carpeta con la direccion de los labs-tests.\
                        Si no esta, se descarga automaticamente.")
    args = parser.parse_args()
    main(args.labs_test, args.alumno)