from flask import Flask, render_template 
# from modue flask import class Flask
app = Flask(__name__) # this app is simply an object of class Flask

JOBS =[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Edinburgh, Scotland',
    'salary': '£50,000'
  },

 {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Manchester, England',
    'salary': '£45,000'
  },

   {
    'id': 3,
    'title': 'Frontend Engenier',
    'location': 'Edinburgh, UK',
    'salary': '£55,000'
  },
  {
    'id': 3,
    'title': ' Backend Engenier',
    'location': 'Edinburgh, UK',
    'salary': '£88,000'
  }
]


@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs = JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug =True)