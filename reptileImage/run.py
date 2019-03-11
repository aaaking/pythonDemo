# http://tuchong.com/rest/tags/%E7%A7%81%E6%88%BF/posts?page=1&count=20&order=weekly
# "http://photo.tuchong.com/"+AuthorID+"/f/"+ImageID+".jpg"

from flask import request
# import requests
import hashlib

def RunCrawler(url):
    response = requests.get(url, headers=header)
    data = json.loads(response, text)
    ImageBox = [];
    for UserAlbum in data["postList"]:
        AuthorID = str(UserAlbum["author_id"])
        for s_image in UserAlbum["images"]:
            ImageID = str(s_image["img_id"])
            ImgURL = "http://photo.tuchong.com/" + AuthorID + "/f/" + ImageID + ".jpg"
            ImageName = AuthorID + "-" + ImageID + ".jpg"
            ImageInfo = {
                "ImgURL": ImgURL,
                "ImageName": ImageName,
            }
            print(ImgURL)
            ImageBox.append(ImageInfo)
    print("total images:" + str(len(ImageBox)) + " page")

    for img in ImageBox:
        if os.path.isfile("./ImageBox/" + img["ImageName"]):
            print(img["ImageName"] + "----already exists!")
            continue
        else:
            time.sleep(randint(1, 3))
        DownImage(img["ImageUrl"], img["ImageName"])

def DownImage(ImageUrl, FileName):
    if not os.path.isdir("./ImageBox"):
        os.makedirs("./ImageBox")
    response = requests.get(ImageUrl, headers = header, stream = True)
    chunk_size = 1024 * 1024
    with open("./ImageBox/" + FileName, "wb+") as f:
        for data in response.iter_content(chunk_size = chunk_size):
            f.write(data)
        print(FileName + "----save success.")

RunCrawler("http://tuchong.com/rest/tags/%E7%A7%81%E6%88%BF/posts?page=1&count=20&order=weekly")