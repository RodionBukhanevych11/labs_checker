# Labs Checker
## Content
- [Project structure](#project-structure)
- [Installation](#installation)

### Project structure
![Alt text](image.png)

### Installation
1. Create venv for backend
```
python3 -m venv .\src\backend
source .\src\backend\bin\activate
python3 -m pip3 install -r .\src\backend\requirements.txt
```
2. Create venv for ui
```
python3 -m venv .\src\ui
source .\src\ui\bin\activate
python3 -m pip3 install -r .\src\ui\requirements.txt
```
3. Run application
```
python3 .\src\backend\app.py
python3 .\src\ui\ui.py
streamlit run .\src\ui\ui.py
```
### Installation (Windows Edition)
1. Create venv for backend
```
python -m venv .\src\backend
.\src\backend\Scripts\activate.bat
python -m pip install -r .\src\backend\requirements.txt
```
2. Create venv for ui
```
python -m venv .\src\ui
.\src\ui\Scripts\activate.bat
python -m pip install -r .\src\ui\requirements.txt
```
3. Run application
```
python .\src\backend\app.py
python .\src\ui\ui.py
streamlit run .\src\ui\ui.py
```