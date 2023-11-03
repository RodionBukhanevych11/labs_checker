# Labs Checker
## Content
- [Project structure](#project-structure)
- [Installation](#installation)

### Project structure
![Alt text](image.png)

### Installation
1. Create venv for backend
```
python3 -m venv .\labs_checker\src\backend
source .\labs_checker\src\backend\bin\activate
python3 -m pip3 install -r .\labs_checker\src\backend\requirements.txt
```
2. Create venv for ui
```
python3 -m venv .\labs_checker\src\ui
source .\labs_checker\src\ui\bin\activate
python3 -m pip3 install -r .\labs_checker\src\ui\requirements.txt
```
3. Run application
```
python3 .\labs_checker\src\backend\app.py
python3 .\labs_checker\src\ui\ui.py
streamlit run .\labs_checker\src\ui\ui.py
```
### Installation (Windows Edition)
1. Create venv for backend
```
python -m venv .\labs_checker\src\backend
.\labs_checker\src\backend\Scripts\activate.bat
python -m pip install -r .\labs_checker\src\backend\requirements.txt
```
2. Create venv for ui
```
python -m venv .\labs_checker\src\ui
.\labs_checker\src\ui\Scripts\activate.bat
python -m pip install -r .\labs_checker\src\ui\requirements.txt
```
3. Run application
```
python .\labs_checker\src\backend\app.py
python .\labs_checker\src\ui\ui.py
streamlit run .\labs_checker\src\ui\ui.py
```