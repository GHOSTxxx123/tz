import io, base64
import os, secrets  
from flask import abort, json, make_response
from application import app, db
from application.model import *
from flask import send_from_directory, request, jsonify
from PIL import Image
from application.save_image import save_picture_1


@app.route('/upload/', methods=['POST', 'GET'])
def upload_files():
    data = request.form
    user = data['user']
    resp = make_response()
    picture_fn = secrets.token_hex(16)
    picture_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], f"{picture_fn}.png")
    request.files['image'].save(picture_path)
    
    print(user)

    data = {'form': 'Hello', 'user':'Azam'},

    return jsonify(data)


@app.route('/Birds/Card/', methods=('GET', 'POST'))
def data_card_birds():
    data = request.form
    token = data['token']
    user = "Я-Хочу-У-Вас-Работать"
    if user == token:   
        data = Birds.query.all()
        return jsonify(data)


@app.route('/Card/', methods=('GET', 'POST'))
def data_card_bird():   
    data = Birds.query.all()
    return jsonify(data)


@app.route('/Histori/Card/', methods=('GET', 'POST'))
def data_card_histori():
    data = request.form
    token = data['token']
    user = "Я-Хочу-У-Вас-Работать"
    if user == token:   
        data = Histori.query.all()
        return jsonify(data)


@app.route('/Birds/Histori/', methods=('GET', 'POST'))
def birds_histori():
    data = request.form
    token = data['token']
    birds_id = data['birds_id']
    user = "Я-Хочу-У-Вас-Работать"
    if user == token:
        search_birds = db.session.query(Birds).filter(Birds.id == birds_id).first(), 
        if search_birds:
            return jsonify(search_birds)
        else:
            data = {"birds_histroi": False},
            return jsonify(data)


@app.route('/Birds/Save/', methods=('GET', 'POST'))
def data_save_birds():
    data = request.form
    token = data['token']
    is_image = data['is_image']
    name = data['name']
    color_feather = data['color_feather']
    user = "Я-Хочу-У-Вас-Работать"
    if user == token:
        bu = db.session.query(Birds).filter(Birds.name == name).first()
        if bu:
            data = {'birds_save': 'False'}
            return jsonify(data)
        else:
            if is_image == 'True':
                picture_fn = secrets.token_hex(16)
                picture_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], f"{picture_fn}.png")
                request.files['image'].save(picture_path)
                busy = Birds(
                    name=name,
                    color_feather=color_feather,
                    cover=f"{picture_fn}.png"
                )
                db.session.add(busy)
                db.session.commit()
                data = {'birds_save': 'True'}
                return jsonify(data)
            else:
                busy = Birds(
                    name=name,
                    color_feather=color_feather,
                    cover="default.png"
                )
                db.session.add(busy)
                db.session.commit()
                data = {'birds_save': 'False'}
                return jsonify(data)


@app.route("/Birds/Image/")
def birds_image():
    data = request.form
    picture_fn = secrets.token_hex(16)
    picture_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], f"{picture_fn}.png")
    request.files['image'].save(picture_path)
    

@app.route('/Birds/Search/', methods=('GET', 'POST'))
def birds_search():
    data = request.form
    token = data['token']
    name = data['name']
    user = "Я-Хочу-У-Вас-Работать"
    if user == token:
        search_birds = db.session.query(Birds).filter(Birds.name == name).first(), 
        if search_birds:
            return jsonify(search_birds)
        else:
            data = {"birds_search": False},
            return jsonify(data)

def save_picture(cover):
    picture_fn = secrets.token_hex(16)
    #picture_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], f"{picture_fn}.png")

    output_size = (220, 340)
    #img = Image.open(io.BytesIO(base64.b64decode(bytes(str(cover), "utf-8"))))
    #img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
    img = Image.open(io.BytesIO(base64.b64decode(cover)))
    img.thumbnail(output_size)
    img.save(f"/uploads/{picture_fn}.png")
    #img = np.array(img)

    return f"{picture_fn}.png"

@app.route('/Histori/', methods=('GET', 'POST'))
def histori_look_birds():
    data = request.form
    token = data['token']
    birds_id = data['birds_id']
    user = "Я-Хочу-У-Вас-Работать"
    if user == token:
        bu = db.session.query(Histori).filter(Histori.birds_id == birds_id).first()
        if bu:
            data = {'birds_histori_save': False},
            return jsonify(data)
        else:
            busy = Histori(
                birds_id=birds_id
                )
            db.session.add(busy)
            db.session.commit()
            data = {'birds_histori_save': True},
            return jsonify(data)

@app.route('/uploads/cover/<filename>', methods=('GET', 'POST'))
def send_file_cover(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


#@app.before_first_request
@app.before_request
def create_tables():
    #app.app_context().push()
    db.create_all()