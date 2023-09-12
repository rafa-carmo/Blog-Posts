from datetime import datetime
from os import walk, stat, path, rename
from operator import itemgetter
from slugify import slugify
import json

FILE_ROOT = "posts"

def save_json(filePath, jsonDict) -> None:
    with open(filePath, "w+", encoding="utf-8") as f:
        json.dump(jsonDict, f, ensure_ascii=False, indent=4)
        
def clear_string(text: str):
    replace_list = ["#", "\n", ".md"]
    for replace_string in replace_list:
        text = text.replace(replace_string, "")
    return text.strip()

def list_files():
    items = []
    for _, __, files in walk(FILE_ROOT):
        for file in files :
            if("md" in file):
                create_time = stat(path.join(FILE_ROOT, file)).st_ctime
                filename = clear_string(file)
                
                slug = slugify(filename)
                
                item = dict()
                item["slug"] = slug
                item["title"] = filename
                with open(path.join(FILE_ROOT, file), "r") as f:
                    file_read = f.readlines()

                # item["created"] = str(datetime.fromtimestamp(create_time))
                item["created"] = clear_string(file_read[0])
                
                item["title"] = clear_string(file_read[1])
                item["subtitle"] = clear_string(file_read[2])
                item["subject"] = clear_string(file_read[3])

                items.append(item)
                
                if(slug != filename):
                    rename(path.join(FILE_ROOT, file), path.join(FILE_ROOT, slug + ".md"))

    sorted_list = sorted(items, key=itemgetter("created"), reverse=True)
    return sorted_list
    ...

if __name__ == '__main__':
    data = dict()
    data["posts"] = list_files()
    save_json("posts.json",data)