cd ..
python -m venv .venv
.\.venv\Scripts\activate.ps1
pip install -r .\langchain-llm-app\requirements.txt
cd langchain-llm-app
pip install ...
python -m pip freeze > requirements.txt

 git config --global user.email "ivanchinook@gmail.com"
  git config --global user.name "ivanchinook"
