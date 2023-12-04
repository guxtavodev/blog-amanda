# Importação dos módulos e classes necessárias
from flask import render_template, redirect, session, jsonify, request, url_for, make_response, send_file, send_from_directory
from app.routes import comments_bp
from app.models import Post, Comentarios
from app import db, app
import uuid
import markdown
import os

# Rota para criar comentários
@comments_bp.route('/create/comentario/<id>', methods=['POST'])
def createComentario(id):
  if request.method == 'POST':
    comentarios = Comentarios(
      post=id,
      autor=request.form['nome'],
      id=str(uuid.uuid4()),
      text=request.form['comentario']
    )
    db.session.add(comentarios)
    db.session.commit()
    return redirect(url_for('artigos.artigo', id=id))