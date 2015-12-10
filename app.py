from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
callers = {
    "+17815261943": "Mikey",
    "+19173316040": "Ronald",
    "+16303104161": "Boots",
    "+14158675311": "Virgil",
}

@app.route("/", methods=['GET', 'POST'])
def response():
    """Respond to incoming calls with a simple text message."""
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"

    print request.values

    # message = 'Hey there, little fella!'
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True, port=8000)