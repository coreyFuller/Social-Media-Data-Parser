from snapchat import friends
def main():
    metadata = friends.readFile("Snapchat/json/friends.json")
    print(metadata)
    

if __name__ == "__main__":
    main()