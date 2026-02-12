### California House Price Prediction Model

### Software and Tools Requirement
1. [GitHub Account](https://www.github.com)
2. [Render Account](https://render.com)
3. [VSCode IDE](https://code.visualstudio.com)

### Create Virtual Environment.
python -m venv .venv

## Activate it.
source .venv/Scripts/activate

## Install Requirements
pip install -r requirements.txt

## Run the app.py file
python app.py

## Deploy on Render
1. Push this repo to GitHub.
2. In Render, click New + -> Web Service -> select your repo.
3. Use these settings:
	- Runtime: Python
	- Build Command: pip install -r requirements.txt
	- Start Command: gunicorn app:app
4. Click Create Web Service.

## Deployed application link
https://housepricepredictionmodel.onrender.com/