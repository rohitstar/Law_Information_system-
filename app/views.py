from flask import render_template
from app import app
from flask import request

import block
import blockchain
chain = blockchain.Blockchain()

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# @app.route('/top')
# def top():
# 	posts = [  # fake array of posts
#         { 
#             'firm': 'firm1', 
#             'body': 'Beautiful day in Portland!' 
#         },
#         { 
#             'firm': 'firm2', 
#             'body': 'The Avengers movie was so cool!' 
#         }
#     ]
# 	return render_template("top.html", posts=posts)

@app.route('/index2')
def index2():
	return render_template("index2.html")

@app.route('/index3')
def index3():
	return render_template("index3.html")

@app.route('/find_template')
def find_template():
	return render_template("find_template.html")


@app.route('/find_template', methods = ['POST'])
def top_firm_request():
	if request.method == 'POST':
		result = request.form
		print result
		# blockname = result["contract_number"] + result["name_assigner"]
		# print blockname
		new_block =  block.Block(result["public_key_assignee"])
		chain.add_block(new_block)
		print new_block.data
		print new_block.previous_hash
		return render_template("block_created.html", hash= new_block.previous_hash)

	