from flask import Flask

app = Flask(__name__)

@app.route("/search/<document>")
def search_on_elastic(document):
    
    response = str(document).replace("_", " ")
    # ...
    # Ciao
    
    return f"Searching this doc: {response}\n"