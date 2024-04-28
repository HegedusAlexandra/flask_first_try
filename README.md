# flask_first_try

# steps : 

## venv added automatically with command 

### create .venv
py -3 -m venv .venv
### permanent permission
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
### temporary for this session
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
### activate enviroment
.venv\Scripts\activate

### install flask
pip install Flask

### create python file
### run python file
flask --app hotel run

### switch on debug
flask --app hotel run --debug

### install dependencies
pip install flask_wtf

https://testdriven.io/blog/flask-sessions/