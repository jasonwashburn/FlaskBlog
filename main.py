from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_blog_data():
    blog_data_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_data = requests.get(blog_data_url).json()
    return blog_data

@app.route('/')
def home():
    blog_data = get_blog_data()
    return render_template("index.html", blog_data=blog_data)


@app.route('/post/<int:blog_id>')
def get_blog_post(blog_id):
    blog_data = get_blog_data()
    title = "No Data"
    subtitle = "No Data"
    body = "No Data"
    for blog_post in blog_data:
        if blog_post['id'] == blog_id:
            title = blog_post['title']
            subtitle = blog_post['subtitle']
            body =  blog_post['body']
            break

    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
