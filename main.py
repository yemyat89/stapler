from flask import Flask, render_template, request, redirect, url_for
from models import db, Topic, Link
import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    all_topics = Topic.query.all()
    return render_template('index.html', topics=all_topics)

@app.route('/new_topic', methods=['GET', 'POST'])
def create_topic():
    if request.method == 'POST':
        topic = Topic(request.form['name'], request.form['desc'])
        db.session.add(topic)
        db.session.commit()
    return render_template('new_topic_form.html')


@app.route('/view_topic/<tid>')
def view_topic(tid):
    topic = Topic.query.filter_by(tid=tid).one()
    links = Link.query.filter_by(fk_tid=topic.tid).all()
    links = list(sorted(links, key=lambda x: x.timestamp))
    return render_template('view_topic.html', topic=topic, links=links)


@app.route('/add_url', methods=['POST'])
def add_url():
    soup = BeautifulSoup(urllib2.urlopen(request.form['url']))
    title = soup.title.string
    dt = datetime.strptime('%s-%s' % (request.form['month'], 
                                      request.form['year']),
                            '%m-%Y')
    link = Link(request.form['tid'], request.form['url'], title, dt)
    db.session.add(link)
    db.session.commit()
    return redirect(url_for('view_topic', tid=request.form['tid']))


if __name__ == '__main__':
    app.run(debug=True)
