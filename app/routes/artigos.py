# Importação dos módulos e classes necessárias
from flask import render_template, redirect, session, jsonify, request, url_for, make_response, send_file, send_from_directory
from app.routes import artigos_bp
from app.models import Post, Comentarios
from app import db, app
import uuid
import markdown
import os


@artigos_bp.route("/")
def homepage():
  artigos = Post.query.order_by(Post.pub_date.desc()).all()
  return render_template("index.html", artigos=artigos)


@artigos_bp.route('/artigos/<id>')
def artigo(id):
  artigos = Post.query.filter_by(id=id).first()
  comentarios = Comentarios.query.filter_by(post=id).all()
  return render_template("artigo.html",
                         artigo=artigos,
                         comentarios=comentarios)


@artigos_bp.route('/edit/artigo/<id>', methods=['GET', 'POST'])
def editar_artigo(id):
  artigos = Post.query.filter_by(id=id).first()
  if request.method == 'POST':
    artigos.title = request.form['title']
    artigos.body = request.form['body']
    artigos.body_markdown = markdown.markdown(request.form['body'])

    artigos.endpoint = request.form['title'].replace(" ", "-")
    db.session.commit()
    return redirect(url_for('artigos.artigo', id=id))
  return render_template('edit-artigo.html', artigo=artigos)


@artigos_bp.route('/delete/artigo/<id>')
def deletar_artigo(id):
  artigos = Post.query.filter_by(id=id).first()
  db.session.delete(artigos)
  db.session.commit()
  return redirect(url_for('admin.admin'))


@artigos_bp.route('/create', methods=["GET", "POST"])
def createArtigo():
  if request.method == 'POST':
    file = request.files["img"]
    if file and (file.filename.endswith('.jpg')
                 or file.filename.endswith('.png')
                 or file.filename.endswith('.jpeg')):
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    artigos = Post(title=request.form['title'],
                   body=request.form['body'],
                   body_markdown=markdown.markdown(request.form['body']),
                   img=request.files['img'].filename,
                   endpoint=request.form['title'].replace(" ", "-"),
                   id=str(uuid.uuid4()))
    db.session.add(artigos)
    db.session.commit()
    return redirect(url_for('artigos.artigos', id=artigos.id))

  return render_template("create-artigo.html")


@artigos_bp.route('/api/send', methods=['POST'])
def criarArt():
  print(dict(request.form))
  file = request.files["img"]
  print('aqui foi file')
  if file and (file.filename.endswith('.jpg') or file.filename.endswith('.png')
               or file.filename.endswith('.jpeg')):
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
  artigos = Post(title=request.form['title'],
                 body=request.form['body'],
                 body_markdown=markdown.markdown(request.form['body']),
                 img=request.files['img'].filename,
                 endpoint=request.form['title'].replace(" ", "-"),
                 id=str(uuid.uuid4()))
  db.session.add(artigos)
  db.session.commit()
  return redirect(url_for('artigos.artigo', id=artigos.id))


@artigos_bp.route("/search", methods=["GET"])
def search():
  if request.method == 'GET':
    search = request.args.get('search')
    artigos = Post.query.filter(Post.title.contains(search)).all()
    return render_template("index.html", artigos=artigos)

  return render_template("search.html")
