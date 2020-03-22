from pytube import YouTube
link = input("Enter the youtube link to be downloaded\n")
YouTube(link).streams.first().download(r"C:\Users\prajw\Downloads")
