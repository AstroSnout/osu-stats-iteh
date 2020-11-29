import os

os.environ["FLASK_APP"] = "app.py"
os.system('cmd /k flask run --port=5001')
