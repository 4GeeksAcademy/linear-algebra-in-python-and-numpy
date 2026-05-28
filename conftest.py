import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")
def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
      if hasattr(metafunc,"config"):
          metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))
      elif hasattr(metafunc,"configuration"):
          metafunc.parametrize("stdin",metafunc.configuration.getoption('stdin'))
      else:
          raise Exception("Imposible to retrieve text configuration object")
    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
    if 'configuration' in metafunc.fixturenames:
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"os":"win32","editor":{"mode":"extension","agent":"vscode","version":"5.0.385"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"http://localhost:3000","contact":"https://github.com/learnpack/learnpack/issues/new","language":"python","autoPlay":true,"projectType":"tutorial","grading":"isolated","exercisesPath":"./exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":[],"actions":[],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"suggestions":{"agent":null},"warnings":{},"difficulty":"beginner","duration":5,"description":{"us":"Exercises and examples for linear algebra using Python and NumPy, covering topics such as vectors, matrices, and linear transformations.","es":"Ejercicios y ejemplos de álgebra lineal utilizando Python y NumPy, cubriendo temas como vectores, matrices y transformaciones lineales."},"title":{"us":"Linear Algebra in Python and NumPy","es":"Álgebra Lineal en Python y NumPy"},"preview":"https://github.com/4GeeksAcademy/linear-algebra-in-python-and-numpy/blob/main/.learn/assets/preview.png","slug":"linear-algebra-in-python-and-numpy","repository":"https://github.com/4GeeksAcademy/linear-algebra-in-python-and-numpy","bugsLink":"https://github.com/4GeeksAcademy/linear-algebra-in-python-and-numpy/issues","technologies":["python","numpy","linear-algebra","data-analysis"],"gitpod":true,"translations":[]}')])
