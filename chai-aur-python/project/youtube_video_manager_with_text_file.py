import time, json, os
clear = lambda:os.system("cls")

def query():
    name = input("Enter video name: ")
    duration = input("Enter video time: ")
    return name, duration

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']} - Duration: {video['duration']} minutes")
    time.sleep(2)

def add_video(videos):
    name, duration = query()
    videos.append({'name':name, 'duration':duration})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video no to update: "))
    if 1 <= index <= len(videos):
        name, duration = query()
        videos[index-1] = {'name': name, 'duration': duration}
        save_data_helper(videos)
    else:
        print("Choose correct index!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video index to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Choose correct index!")


def main():
    videos = load_data()
    while True:
        print("Youtube Video Manager")
        print('_' * 44)
        print("Choose any option:")
        print(' '* 17, "1) List all youtube videos")
        print(' '* 17, "2) Add a youtube video")
        print(' '* 17, "3) Update a youtube video")
        print(' '* 17, "4) Delete a youtube video")
        print(' '* 17, "5) Exit the app")
        choice = input("Enter your option: ")
        match choice:
            case "1":
                clear()
                list_all_videos(videos)
                clear()
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Choose correct option!")
                time.sleep(2)

if __name__ == "__main__":
    main()  # main entry point just like main in c++


'''
JSON Structure
JSON consists of two main structures:

1. Object
An object is a collection of key-value pairs.
{
    "name": "Azeem",
    "age": 20,
    "city": "Lahore"
}
Python equivalent:
student = {
    "name": "Azeem",
    "age": 20,
    "city": "Lahore"
}
A JSON object is very similar to a Python dictionary.

2. Array
An array stores multiple values.
[
    "Python",
    "C++",
    "Java"
]
Python equivalent:
languages = ["Python", "C++", "Java"]

Function	    Purpose
json.dump()	    Write JSON to a file
json.dumps()	Convert a Python object to a JSON string
json.load()     Read JSON from a file
json.loads()	Convert a JSON string to a Python object
'''