import galai as gal
from flask import Flask, request
import json

app = Flask(__name__)
model = gal.load_model("standard")

@app.route("/galactica", methods=["POST"])
def get_response():
    request_data = request.json
    if request_data is None:
        return "No data provided"
    if request_data["input"] is None:
        return "No input provided"
    # call the function that generates the response
    response = model.generate(request_data['input'])
    return response

# @app.route('/galactica')
# def galactica_generate(text):
#     output = model.generate(text)
#     return output

# print(output)

if __name__ == "__main__":
    app.run()