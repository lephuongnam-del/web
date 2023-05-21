from app import app
from flask import render_template, session, request, redirect, url_for, flash, make_response, session

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Attendees')
def attendees():
    attendees = [ { first_name: 'Lanice', last_name: 'Montre', job_position: 'Director', email: 'lamontre@gmail.com', company: 'Montreal Consulting Inc', city: 'Philadelphia', state: 'PA', interests: 'ML', submitted_date: '2020-05-07 00:00:00-04', comments: 'learn more' }, { first_name: 'Do', last_name: 'Ji', job_position: 'Director', email: 'mar@smith.org', company: 'Mafolab', city: 'Rockville', state: 'AZ', interests: 'CC', submitted_date: '2020-05-07 00:00:00-04', comments: 'networking' }, { first_name: 'Edem', last_name: 'Lamoine', job_position: 'Executive', email: 'lamoine@gmail.com', company: 'Paracetamole Pharma', city: 'Washington', state: 'DC', interests: 'DS', submitted_date: '2020-05-07 00:00:00-04', comments: 'Hands on experience' }, { first_name: 'Celine', last_name: 'Mabs', job_position: 'Developer', email: 'celinemabs@school.edu', company: 'Mabs Learning Center', city: 'Rawlings', state: 'WY', interests: 'DS', submitted_date: '2020-05-07 00:00:00-04', comments: 'Hand-ons experience and networking with engineers in the field' }, { first_name: 'Mary', last_name: 'Maine', job_position: '', email: 'mary.maine@noreply.com', company: 'Maine Co', city: 'Hanover', state: 'PA', interests: 'ML', submitted_date: '2020-05-07 00:00:00-04', comments: 'Looking forward to start the class' }, ]
    return render_template('attendees.html', attendees=attendees)



@app.route('/Notifications')
def notifications():
    notifications = [ { id: 1, status: 'Notifications submitted', message: '', submitted_date: null, completed_date: null, subject: '' }, { id: 2, status: 'Notifications submitted', message: 'uyt', submitted_date: '2020-05-07 18:00:38.573856-04', completed_date: '2020-05-07 18:00:39.124435-04', subject: 'Welcome Email' }, { id: 3, status: 'Notified 5 attendees', message: 'Welcome Email', submitted_date: '2020-05-07 18:14:04.239065-04', completed_date: '2020-05-07 18:14:04.271981-04', subject: 'Welcome Email' } , { id: 4, status: 'Notifications submitted', message: 'New Speaker Added: Dr Daniel Shu', submitted_date: '2020-05-07 23:24:00.504412-04', completed_date: null, subject: 'New Speaker Added: Dr Daniel Shu' } ]
    return render_template('notifications.html', notifications=notifications)