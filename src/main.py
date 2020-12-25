from snapchat import snapchat
from instagram import instagram 

def main():
    ig = instagram.Instagram()
    snap = snapchat.Snapchat()
    ig.run()
    snap.run()
    print("here")

if __name__ == "__main__":
    main()