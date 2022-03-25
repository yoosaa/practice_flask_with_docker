from flask import Flask, render_template
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def index():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)