from app import create_app
app = create_app()

@app.route("/")
def healthy():
    return "<h1>Austrian Notes service: Healthy</h1> \n <footer>Developed by: Vladimir Alfaro</footer>"

if __name__ == '__main__':
    app.run(debug=True)
