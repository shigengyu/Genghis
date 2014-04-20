import os
import MySQLdb
from articles.models import Article
from django.contrib.auth.models import User
from genghis.settings import DEBUG

class WordPressPost:
    
    def __init__(self, id, title, author, url, post_date):
        self.id = id
        self.title = title
        self.author = author
        self.url = url
        self.post_date = post_date
    

def fetch_articles():
    articles = list()
    
    if not DEBUG:
        sql = """
        SELECT p.ID, p.post_title, u.display_name as author, p.post_date_gmt
        FROM `wp_posts` p, `wp_users` u
        WHERE p.post_author = u.ID
        AND p.post_type = 'post'
        AND p.post_status = 'publish'
        ORDER BY p.post_date_gmt DESC
        """
    else:
        sql = """
        select a.id, a.subject, b.first_name, a.update_date_time
        from articles_article a, auth_user b
        where a.author_id = b.id
        order by a.create_date_time desc
        limit 10
        """
    
    connection = get_connection()
    
    cursor = connection.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        article = Article()
        article.id = row[0]
        article.subject = row[1]
        article.create_date_time = row[3]
        articles.append(article)
    
    connection.close()
    
    return articles

def get_connection():
    
    if not DEBUG:
        host = os.environ.get('WP_DATABASE_HOST', '')
        port = int(os.environ.get('WP_DATABASE_PORT', '3306'))
        user = os.environ.get('WP_DATABASE_USER', 'root')
        password = os.environ.get('WP_DATABASE_PASSWORD', '')
        db = os.environ.get('WP_DATABASE_NAME', '')
    else:
        host = os.environ.get('GENGHIS_DATABASE_HOST', '')
        port = int(os.environ.get('GENGHIS_DATABASE_PORT', '3306'))
        user = os.environ.get('GENGHIS_DATABASE_USER', 'root')
        password = os.environ.get('GENGHIS_DATABASE_PASSWORD', '')
        db = os.environ.get('GENGHIS_DATABASE_NAME', '')
    
    connection = MySQLdb.connect(host = host, port = port, user = user, passwd = password, db = db)
    return connection