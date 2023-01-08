from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
	msg = request.form["msg"]
	response = galactica(msg)
	return response

def galactica(textbox):
    # print(textbox)
    # a = textbox
    a = requests.post("http://backend-galactica:5000/galactica", json={"input": textbox}, headers={"Content-Type": "application/json"})
    #print(a.response)
    return str(a.text)


# @app.route("/galactica-test", methods=["POST"])
# def get_response():
#     # call the function that generates the response
#     data = request.json
#     print(data['input'])
#     #response = 'jo det går bra att fråga'
#     response = data['input']
#     #print(response)
#     #response = model.generate(request_data)
#     return response



try:
    a = requests.post("http://backend-galactica:5000/galactica", json={"input": "e2 annan mening"}, headers={"Content-Type": "application/json"})
    print(a.response)
except:
    print("Error")

if __name__ == "__main__":
    app.run()