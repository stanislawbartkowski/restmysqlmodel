from whelper import respondrest, uploadfile


@respondrest
def keepfile():
    uploadfile()


if __name__ == "__main__":
    keepfile()
