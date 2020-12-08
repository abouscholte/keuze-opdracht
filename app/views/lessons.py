from app import db
from app.models import Course, Lesson
from flask import Blueprint, render_template, abort, flash, url_for, redirect, request
from flask_login import login_required, current_user

from app.forms import NewCourseForm, EditLessonForm

lessons = Blueprint('lessons', __name__)

@lessons.route('/')
def index():
  beginnerLessons = Lesson.query.filter_by(course_id=1).all()
  websiteLessons = Lesson.query.filter_by(course_id=2).all()
  
  return render_template('index.html', beginnerLessons=beginnerLessons, websiteLessons=websiteLessons)

@lessons.route('/courses/beginners/')
def beginners():
  lessons = Lesson.query.filter_by(course_id=1).all()
  return render_template('courses/beginners.html', lessons=lessons)

@lessons.route('/courses/website/')
def website():
  lessons = Lesson.query.filter_by(course_id=2).all()
  return render_template('courses/website.html', lessons=lessons)

@lessons.route('/lessons/lesson-<id>/')
def lesson(id):
  lesson = Lesson.query.filter_by(id=id).first_or_404()
  if not current_user.is_authenticated and lesson.locked:
    abort(401)

  previous = db.session.query(Lesson).order_by(Lesson.id.desc()).filter(Lesson.course_id == lesson.course_id).filter(Lesson.id < lesson.id).first()
  next = db.session.query(Lesson).order_by(Lesson.id.asc()).filter(Lesson.course_id == lesson.course_id).filter(Lesson.id > lesson.id).first()

  return render_template('lessons/lesson.html', lesson=lesson, next=next, previous=previous)

@lessons.route('/lessons/new/', methods=['GET', 'POST'])
@login_required
def new_course():
  if not current_user.admin: abort(401)

  form = NewCourseForm()
  form.course.choices = [(g.id, g.name) for g in Course.query.order_by('name')]

  if form.validate_on_submit():
    lesson = Lesson(title=form.title.data, body=form.body.data, course_id=form.course.data)
    db.session.add(lesson)
    db.session.commit()

    course = Course.query.get(form.course.data)
    flash('De les is toegevoegd aan de ' + course.name)
    return redirect(url_for('lessons.index'))

  return render_template('lessons/new.html', form=form)

@lessons.route('/lessons/lesson-<id>/edit/', methods=['GET', 'POST'])
@login_required
def edit_lesson(id):
  lesson = Lesson.query.filter_by(id=id).first_or_404()
  if not current_user.admin: abort(401)

  form = EditLessonForm()

  if form.validate_on_submit():
    lesson.title = form.title.data
    lesson.body = form.body.data

    db.session.commit()
    flash('De les is succesvol aangepast')
    return redirect(url_for('lessons.lesson', id=lesson.id))
  elif request.method == 'GET':
    form.title.data = lesson.title
    form.body.data = lesson.body

  return render_template('lessons/edit.html', lesson=lesson, form=form)

@lessons.route('/lessons/lesson-<id>/delete/', methods=['GET', 'POST'])
@login_required
def delete_lesson(id):
  lesson = Lesson.query.filter_by(id=id).first_or_404()
  if not current_user.admin: abort(401)

  db.session.delete(lesson)
  db.session.commit()

  flash('De les is verwijderd')
  return redirect(url_for('lessons.index'))