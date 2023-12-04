# Importação dos módulos e classes necessárias
from flask import render_template, redirect, session, jsonify, request, url_for, make_response, send_file, send_from_directory
from app.routes import admin_bp
from app.models import Post, Comentarios
from app import db, app
import uuid
import markdown
import os

@admin_bp.route('/admin/amanda')
def admin():
  artigos = Post.query.all()
  comentarios = Comentarios.query.all()
  return render_template('admin.html', artigos=artigos, comentarios=comentarios)

@admin_bp.route("/delete-post/<id>")
def delete_post(id):
  post = Post.query.filter_by(id=id).first()
  db.session.delete(post)
  db.session.commit()
  return redirect(url_for('admin.admin'))

@admin_bp.route("/delete-comentario/<id>")
def delete_comentario(id):
  comentario = Comentarios.query.filter_by(id=id).first()
  db.session.delete(comentario)
  db.session.commit()
  return redirect(url_for('admin.admin'))

