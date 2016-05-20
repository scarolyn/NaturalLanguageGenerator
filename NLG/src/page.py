from flask import Flask
from flask import request
from flask import render_template
import NLG as nlg

app = Flask(__name__, static_folder='static')

@app.route('/')
def my_form():
    return render_template("Page.html")

@app.route('/Paragraph', methods=['POST'])
def my_form_post():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    if request.method == 'POST':
        d1 = request.form['date1']
        d2 = request.form['date2']

        year1 = d1[2:4]
        month1 = months[int(d1[5:7]) - 1]
        day1 = d1[8:]
        date1 = day1 + '-' + month1 + '-' + year1

        year2 = d2[2:4]
        month2 = months[int(d2[5:7]) - 1]
        day2 = d2[8:]
        date2 = day2 + '-' + month2 + '-' + year2

        if len(nlg.paragraph(date1, date2)) == 0:
            return render_template('Paragraph.html', paragraph='Data does not exist for these dates')
        return render_template('Paragraph.html', day1=date1, day2=date2, paragraph=nlg.paragraph(date1, date2))

if __name__ == '__main__':
    app.run(debug=True)