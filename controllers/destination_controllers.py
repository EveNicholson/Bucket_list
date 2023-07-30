from flask import Blueprint, render_template, redirect, request
from app import db
from models.destination import Destination
from models.user import User
import os



destinations_blueprint = Blueprint('destinations', __name__)


@destinations_blueprint.route('/destinations')
def destinations():
    destinations = Destination.query.all()
    users = User.query.all()
    return render_template('index.jinja', destinations=destinations, users=users)

@destinations_blueprint.route('/destinations/add', methods=["POST"])
def add_destination():
    user_id = request.form['user_id']
    country = request.form['country']
    city = request.form['city']
    destination_date = request.form['date']
    destination = Destination(user_id = user_id, country=country , city=city,date = destination_date)
    db.session.add(destination)
    db.session.commit()
    return redirect('/destinations')

@destinations_blueprint.route('/destinations/<id>')
def show_destination(id):
    destination = Destination.query.get(id)
    user = User.query.get(destination.user_id)
    return render_template('destination.jinja', destination=destination, user=user)

@destinations_blueprint.route('/destinations/<id>/update')
def update_destination(id):
    destination = Destination.query.get(id)
    users = User.query.all()
    return render_template('update.jinja', destination=destination, users=users)

@destinations_blueprint.route('/destinations/<id>/update', methods=["POST"])
def confirm_update(id):
    user_id = request.form['user_id']
    country = request.form['country']
    city = request.form['city']
    destination_date = request.form['date']
    destination = Destination.query.get(id)
    destination.country = country
    destination.city = city
    destination.date = destination_date
    destination.user_id = user_id
    db.session.commit()
    return redirect(f'/destinations/{destination.id}')
    
@destinations_blueprint.route('/destinations/<id>/delete', methods=["POST"])
def delete_destination(id):
    destination = Destination.query.get(id)
    db.session.delete(destination)
    db.session.commit()
    return redirect('/destinations')

@destinations_blueprint.route('/destinations/add/user', methods=['POST'])
def add_new_user():
    user_name = request.form['username']
    nationality = request.form['nationality']
    user = User(username = user_name, nationality=nationality)
    db.session.add(user)
    db.session.commit()
    return redirect('/destinations')

comments = []

@destinations_blueprint.route('/destinations/<id>')
def show_comments():
   return render_template('destination.jinja', comments=comments)

@destinations_blueprint.route('/destinations/<id>/comment', methods=['POST'])
def add_comment():
    content = request.form['content']
    comments.append(content)
    db.session.add(content)
    db.session.commit()
    return redirect('/destinations/<id>')







# ************************************************************************

# @destinations_blueprint.route('/destinations/<id>', methods=['POST'])
# def upload_form():
#     db.session.add(upload_form)
#     db.session.commit()
#     return render_template('destination.jinja')
    

# @destinations_blueprint.route('/destinations/<id>', methods=['POST'])
# def upload_picture():
#     if 'picture' not in request.files:
#         flash('No picture part in the request', 'error')
#         db.session.add(upload_picture)
#         db.session.commit()
#         return redirect(url_for('/destinations'))



#     file = request.files['picture']
#     if file.filename == '':
#         flash('No selected file', 'error')
#         return redirect(url_for('upload_form'))

   
#     if file:
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         flash('File uploaded successfully', 'success')
#     else:
#         flash('Invalid file', 'error')

#     return redirect(url_for('upload_form'))
   
  
# @destinations_blueprint.route('/destinations/<id>', methods=['POST'])
# def get_uploaded_pictures():
#     pictures = []
#     for filename in os.listdir(app.config['UPLOAD_FOLDER']):
#             if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
#                 pictures.append(filename)
#                 db.session.add(get_uploaded_pictures)
#                 db.session.commit()
#     return pictures

