import json
import pickle
import os

def replace_author(d, author_map):
    if isinstance(d, dict):
        if "author" in d and d["author"] in author_map:
            d["author"] = author_map[d["author"]]
        for key in d:
            replace_author(d[key], author_map)
    elif isinstance(d, list):
        for item in d:
            replace_author(item, author_map)

ifile = open("author_map.pickle", "rb")
author_map = pickle.load(ifile)
posts = os.listdir('./posts')

os.mkdir('posts_author')

for post in posts:
    with open('./posts/'+post, 'r') as f:
        p = json.load(f)
        replace_author(p, author_map)

        with open("./posts_author/"+post, "w") as ofile: 
            json.dump(p, ofile, indent=2)