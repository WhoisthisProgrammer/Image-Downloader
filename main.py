import urllib.request

def ImageDownloader(url,name_file,path="F:/Image Download/"):
    full_path = path + name_file + ".jpg"
    print("Download....")
    urllib.request.urlretrieve(url,full_path)
    print("Downloaded")


url = input("Enter Image URL : ")
name_file = input("Enter name of the file : ")

ImageDownloader(url,name_file)
