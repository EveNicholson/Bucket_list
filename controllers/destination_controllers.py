from flask import Blueprint, render_template, redirect, request
from app import db
from models.destination import Destination
from models.user import User
import os
from models.comment import Comment


destinations_blueprint = Blueprint('destinations', __name__)

@destinations_blueprint.route('/users/destinations', methods=['POST'])
def user_destinations():
    user_id = request.form['user_id']
    users = User.query.all()
    user = User.query.get(user_id)
    
    return render_template('index.jinja', destinations=user.destinations, users=users)


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
    date = request.form['date']
    destination = Destination(user_id = user_id, country=country , city=city,date=date)
    db.session.add(destination)
    db.session.commit()
    return redirect('/destinations')

@destinations_blueprint.route('/destinations/<id>')
def show_destination(id):
    destination = Destination.query.get(id)
    print(destination.comments)
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
    date = request.form['date']
    destination = Destination.query.get(id)
    destination.country = country
    destination.city = city
    destination.date = date
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

@destinations_blueprint.route('/destinations/<id>/comments', methods=['POST'])
def show_comments(id):
   comment = request.form['comment']
   comment = Comment(destination_id=id, comment=comment)
   db.session.add(comment)
   db.session.commit()
   return redirect(f'/destinations/{id}')

@destinations_blueprint.route('/destinations/<destination_id>/comments/<comment_id>/delete', methods=["POST"])
def delete_comment(destination_id, comment_id):
    comment = Comment.query.get(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(f'/destinations/{destination_id}')


@destinations_blueprint.route('/destinations/<id>/want_to_visit', methods=['POST'])
def want_to_visit(id):
   want_to_visit = "want_to_visit" in request.form
   destination = Destination.query.get(id)
   destination.want_to_visit = want_to_visit
   db.session.commit()
   return redirect(f'/destinations/{id}')

@destinations_blueprint.route('/destinations/<id>/visited', methods=['POST'])
def visited(id):
   visited = "visited" in request.form
   destination = Destination.query.get(id)
   destination.visited = visited
   db.session.commit()
   return redirect(f'/destinations/{id}')







