from flask import Flask, render_template, request
app = Flask(__name__)
 
# http://python.zombie-hunting-club.com/entry/2017/11/03/223503

@app.route('/')
def index():
    s_def1 = "abc"
    lis_def1 = ["a1", "a2", "a3"]
    dic_def1 = {"name":"John", "age":24}
    bl_def1 = True
    
    # templatesフォルダ直下にindex.htmlを置く
    # staticフォルダ直下にindex.css、index.jsを置く
    # 第1引数で指定したファイル中の変数を第2引数以降で指定することで、python→index.htmlに値を渡せる。
    html = render_template('index.html', s1=s_def1, lis1=lis_def1, dic1=dic_def1, bl1=bl_def1)
    return html
 
@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = request.form['post_value']

    return res

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)