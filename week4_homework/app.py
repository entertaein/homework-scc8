from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)



client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 여길 채워나가세요!
    name_recieve = request.form['name_give']
    count_recieve = request.form['count_give']
    address_recieve = request.form['address_give']
    phone_recieve = request.form['phone_give']

    data = {'name':name_recieve,'count':count_recieve,'address':address_recieve,'phone':phone_recieve}
    db.order.insert_one(data)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 여길 채워나가세요!
    orders = list(db.order.find({},{'_id':False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)