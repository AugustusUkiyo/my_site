from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image" : "images.jpeg",
        "author" : "Ukiyo",
        "date" : date(2021, 7, 21),
        "title" : "Mountain Hiking",
        "excerpt" : "Mountain here !!!",
        "content" : """
            lorem ffd sfh ! hgfkjnkjgd

            lorem ffd sfh ! hgfkjnkjgd

            lorem ffd sfh ! hgfkjnkjgd
        """
    },
    {
        "slug" : "programming-is-fun",
        "image" : "google-css-images.jpg",
        "author" : "Ukiyo",
        "date" : date(2021, 3, 11),
        "title" : "Programming Is Great",
        "excerpt" : "Searching error in your code",
        "content" : """
            abcxyw 1231234 14124wqrsdf

            abcxyw 1231234 14124wqrsdf

            lorem ffd sfh ! hgfkjnkjgd abcxyw 1231234 14124wqrsdf
        """
    },
    {
        "slug" : "into-the-woods",
        "image" : "photo-1.jpeg",
        "author" : "Ukiyo",
        "date" : date(2022, 12, 15),
        "title" : "Nature At Its Best",
        "excerpt" : "Nature is amazing !!!",
        "content" : """
            lorem ffd sfh ! hgfkjnkjgd akjdgfhkvsdaf

            lorem ffd sfh ! hgfkjnkjgd Nature jnkjgd akjdgfhkvsdaf

            lorem ffd sfh ! hgfkjnkjgd Nature jnkjgd akjdgfhkvsdaf
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    # print(latest_posts)
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_post
    })