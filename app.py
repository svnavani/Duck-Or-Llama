from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', src_link='static/assets/llama_1.jpg')

@app.route('/process', methods=['POST'])
def process():
    button_name = request.form['button_name']
    image_src = request.form['image_src']
    image_name, image_number = get_name_and_number(image_src)

    next_picture = get_next_picture(image_name, image_number)

    to_return = {
        'button_name': button_name,
        'image_name': image_name,
        'next_picture': next_picture
    }
    return jsonify(to_return)

# parse the name of the animal from the picture tag
def get_name_and_number(image_src):
    path_words = image_src.split('/')
    file_name = path_words[-1]
    file_name = file_name.split('.')[0]
    return file_name.split('_')[0], file_name.split('_')[0]

# choose the next picture to be shows
def get_next_picture(image_name, image_number):
    num = image_number
    while (num == image_number):
        # choose one out of the 5 pictures that is not it's own
        num = random.randint(1,5)

    # choose which animal to show
    animal = random.randint(0,2)
    if animal == 1:
        next_image = 'static/assets/llama_' + str(num) + '.jpg'
    else:
        next_image = 'static/assets/duck_' + str(num) + '.jpg'

    # returns the path of the image to be shown next
    return next_image

if __name__ == '__main__':
    app.run(debug=True)