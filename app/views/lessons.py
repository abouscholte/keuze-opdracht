from app import db
from app.models import Course, Lesson
from flask import Blueprint, render_template, abort, flash, url_for, redirect
from flask_login import login_required, current_user

from app.forms import NewCourseForm

lessons = Blueprint('lessons', __name__)

@lessons.route('/')
def index():
  beginnerLessons = Lesson.query.filter_by(course_id=1).all()
  websiteLessons = Lesson.query.filter_by(course_id=2).all()
  
  return render_template('index.html', beginnerLessons=beginnerLessons, websiteLessons=websiteLessons)

@lessons.route('/lessons/lesson-<id>/')
def lesson(id):
  lesson = Lesson.query.filter_by(id=id).first_or_404()
  previous = db.session.query(Lesson).order_by(Lesson.id.desc()).filter(Lesson.course_id == lesson.course_id).filter(Lesson.id < lesson.id).first()
  next = db.session.query(Lesson).order_by(Lesson.id.asc()).filter(Lesson.course_id == lesson.course_id).filter(Lesson.id > lesson.id).first()

  return render_template('lessons/lesson.html', lesson=lesson, next=next, previous=previous)

@lessons.route('/lessons/new/', methods=['GET', 'POST'])
@login_required
def new_course():
  if not current_user.admin:
    abort(403)

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