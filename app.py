from flask import Flask, render_template 
# from modue flask import class Flask
app = Flask(__name__) # this app is simply an object of class Flask

JOBS =[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },

 {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },

   {
    'id': 3,
    'title': 'Frontend Engenier',
    'location': 'Edinburgh, UK',
    'salary': '£55000'
  },
  {
    'id': 3,
    'title': ' Backend Engenier',
    'location': 'Edinburgh, UK',
    'salary': '£88000'
  }
]


@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs = JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug =True)