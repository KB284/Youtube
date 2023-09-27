import yt_dlp


while True:
    #enter url for download
    url = input("Enter Youtube video url: ")

    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Video downloaded successfully!")

    response = input(str("Would you like to keep downloading videos?(yes/no)"))

    if response == "yes":
        print("")
    else:
        print("Thank you for using this software.")
        break

#convert to executable in near furute