# wordscores
Command Line Tool for scoring words as it is very needed

### Assumptions
 
1. The default values set to the given text files

2. CLT designed for giving different file paths or list of words as well

# Setup And Configuration


## Initialize virtual machine and run the code
1. ```python3 -m venv venv```
2. ```source . venv/bin/activate```
3. make sure that you are at /cinemator/
4. ```make setup```  
5. ```ln -s wordscores/wording/__main__.py wordscores```

## CINEMATOR Commands
1. ```wordscores topwords``` builds leaderboards for given words or default words.
2. ```wordscores letters``` builds leaderboards for the letters with given words or default words.


## MAKE Commands
1. ``` make clean``` to clean unnecessary files before commits
2. ```make lint``` to check linting with flake8
3. ``` make lint-fix``` to fix code with black
4. ```make setup``` to build and install the application


### notes

1. Copied some parts from my command linetool for the command options; if you are interested in searching movies try:

 ```pip install cinemator```

repo: https://github.com/helixphoenix/cinemator 

2. python sorted does not sort alphabetically once in a while, known bug