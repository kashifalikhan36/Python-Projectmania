import requests
blog_url='https://api.npoint.io/5b86cb1c2278d8471563'
blog_posts=requests.get(url=blog_url)
print(blog_posts.json())