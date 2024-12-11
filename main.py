from app import create_app
app = create_app()
from dotenv import load_dotenv
import os

load_dotenv()

@app.route("/")
def healthy():
    return "<h1>Austrian Notes service: Healthy</h1> \n <footer>Developed by: Vladimir Alfaro</footer>"

@app.route(f"/api/{os.getenv('API_VERSION')}")
def api():
    return f"<h1>Austrian Notes service API-{os.getenv('API_VERSION')}: Healthy</h1> \n <footer>Developed by: Vladimir Alfaro</footer>"

if __name__ == '__main__':
    app.run(debug=True)
