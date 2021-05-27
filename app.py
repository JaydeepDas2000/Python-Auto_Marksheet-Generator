# Import libaries

from flask import Flask, render_template, request, url_for, jsonify
import numpy as np
from utils import *

app = Flask(__name__)

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/')
def home2():
    return render_template("index.html")

@app.route('/analyse.html')
def analyse():
    return render_template("analyse.html")

@app.route('/analyse.html', methods=['GET', 'POST'])
def auto_calculation():
    if request.method == "POST":
        sname = request.form['sname']
        uroll = request.form['uroll']
        s1mark = request.form['s1mark']
        s2mark = request.form['s2mark']
        s3mark = request.form['s3mark']
        total = total_marks(int(s1mark), int(s2mark), int(s3mark))
        avg = avg_marks(int(s1mark), int(s2mark), int(s3mark))
        if avg < 50:
            message = 'You are Fail'
        else:
            message = 'You are Pass'
        return render_template('analyse.html', stu_name=sname, uni_roll=uroll, sub1_mark=s1mark, sub2_mark=s2mark, sub3_mark=s3mark, tmark=total, amark=avg, result=message)
    
if __name__ =="__main__":
    app.run(debug=True)