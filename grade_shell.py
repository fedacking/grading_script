from get_git_repo import get_repo_gh
import subprocess
import os


class Grade:
    name: str
    build_results: str
    test_results: str

    def __init__(self, name, test_results, build_results) -> None:
        self.name = name
        self.test_results = test_results
        self.build_results = build_results

def grade_alumno(url_github) -> Grade:
    folder = get_repo_gh(url_github, "entrega_shell") + "/shell"
    subprocess.run(["make", "clean"], cwd=folder)
    result = subprocess.run([
        "make", "-B", "-e", "SHELL_TEST=true"], 
        cwd=folder, 
        capture_output=True,
        text=True
    )
    build_results = result.stdout + '\n' + result.stderr
    cwd = os.getcwd() + '/'
    my_env = os.environ.copy()
    my_env["TARGET_SHELL"] = cwd + folder + '/sh'
    result = subprocess.run(
        ["make", "test"], 
        cwd="fisop/labs-tests/shell",
        capture_output=True, 
        text=True,
        env=my_env
    )
    name = folder.split("/")[-2]
    test_result = result.stdout + '\n' + result.stderr
    return Grade(name, test_result, build_results)

with open("repos.txt", "r+") as file:
    input = [x.strip() for x in file.readlines()]

output = []

if not os.path.exists("input"):
    os.mkdir("input")

if not os.path.exists("output"):
    os.mkdir("output")

get_repo_gh("https://github.com/fisop/labs-tests", folder="")


for alumno in input:
    output.append(grade_alumno("https://github.com/" + alumno))

for out in output:
    filename = "output/" + out.name + ".out"
    with open(filename, "w+", encoding='utf8') as file:
        file.write("#####\nBuild\n")
        file.write(out.build_results)
        file.write("#####\nTest\n")
        file.write(out.test_results)