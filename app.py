from flask import Flask, render_template, request

from dim_sum_helper import dim_sum_dish, chinese_name, cook_method, dim_sum_img

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Welcome to Dim Sum 101"

@app.route('/about')
def about():
    return f"""
        <h1> About me </h1>
    """

@app.route('/dimsum/<int:dim_sum_id>')
def dim_sum(dim_sum_id):
    item = dim_sum_dish[dim_sum_id]
    name = chinese_name[dim_sum_id] 
    return f"""
        <h1> {item} </h1>
        <h2><em> {name} </em></h2>
        <img src='{dim_sum_img[dim_sum_id]}'></img>
        <br>
        <p> Cooking Method: {cook_method[dim_sum_id]} <p>
    """

