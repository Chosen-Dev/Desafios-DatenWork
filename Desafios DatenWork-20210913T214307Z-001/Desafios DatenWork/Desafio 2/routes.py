from flask import Flask 

app = Flask("Eu na Daten") 

@app.route('/olamundo', methods=["GET"])
def olamundo():
    return{"Hello Word": "I am at DatenWork"}

app.run()