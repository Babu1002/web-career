from flask import Flask, render_template, jsonify

JOBS = [{
  'id': 1,
  'title': 'Data analyst',
  'location': 'delhi, India',
  'salary': '6,00,000'
}, {
  'id': 2,
  'title': 'Data sciencetist',
  'location': 'kolkata, India',
  'salary': '1,00,000'
}, {
  'id': 2,
  'title': 'Back-end devloper',
  'location': 'Remote',
  'salary': '50,000'
}, {
  'id': 3,
  'title': 'Front-end devloper',
  'location': 'Remote'
}]

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
