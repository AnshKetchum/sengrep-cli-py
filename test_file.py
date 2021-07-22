import flask
app = flask.Flask()

@app.route("/echo/<msg>", methods=["POST"])
@login_required
def echo(msg):
    return msg

@app.route("/reverse/<msg>")
def echo_reverse(msg):
    return msg.reverse()