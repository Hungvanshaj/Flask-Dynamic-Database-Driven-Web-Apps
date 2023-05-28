from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Ho Chi Minh City, Vietnam',
  'salary': 'VND. 7.500.000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Ha Noi, Vietnam',
  'salary': 'VND. 9.000.000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Da Lat City, Vietnam',
  'salary': 'VND. 8.000.000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Da Nang City, Vietnam',
  'salary': 'VND. 10.000.000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Hung')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
