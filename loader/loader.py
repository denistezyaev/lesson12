from flask import Blueprint, request, render_template

from functions import load_posts, uploads_posts
import logging

logging.basicConfig(encoding='utf=8', level=logging.INFO)
loader_bluprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static', template_folder='templates')


@loader_bluprint.route('/form/')
def form():
    return render_template('post_form.html')


@loader_bluprint.route('/upload/', methods=["POST"])
def upload():
    try:
        file = request.files.get('picture')
        filename = file.filename
        content = request.values['content']
        posts = load_posts()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        uploads_posts(posts)
        file.save(f'./uploads/images/{filename}')
        if filename.split('.')[-1] in ['png', 'jpeg', 'jpg']:
            return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)
        else:
            logging.info('Файл не изображение')
    except FileNotFoundError:
        logging.error('Ошибка при загрузке файла')
        return "<h1> Файл не найден <h1>"
