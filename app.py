from flask import Flask, render_template, request

from dim_sum_helper import dim_sum_dish, chinese_name, cook_method, dim_sum_img

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', dim_sum_dish=dim_sum_dish)

@app.route('/about')
def about():
    return f"""
        <h1> About me </h1>
    """

@app.route('/dimsum/<int:dim_sum_id>')
def dim_sum(dim_sum_id):
    item = dim_sum_dish[dim_sum_id]
    name = chinese_name[dim_sum_id] 
    
    return render_template('dim_sum_info.html', item=dim_sum_dish[dim_sum_id], name=chinese_name[dim_sum_id], dim_sum_img=dim_sum_img[dim_sum_id], cook_method=cook_method[dim_sum_id])

