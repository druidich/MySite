from os import abort

from flask import render_template, session, redirect, url_for, flash, request, current_app, make_response
from flask_login import login_required, current_user

from app.decorators import admin_required, permission_required
from app.main.forms import EditProfileAdminForm, PostForm, CommentForm
from app.auth.forms import EditProfileForm
from . import admin
from .. import db
from ..model import User, Role, Permission, Post, Comment


@admin.route('/<username>')
def index(username):
    user = User.query.filter_by(username=username).first()
    return render_template('admin/index.html', user=user, page_header='Dash Board')


@admin.route('addmessage/<username>')
def add_message(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('admin/new_material.html', user=user, page_header='Create new Material')
