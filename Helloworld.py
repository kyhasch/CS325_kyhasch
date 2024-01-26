# File: hello_world.py

def get_user_name():
    name = input("What's your name? ")
    return name

def main():
    user_name = get_user_name()
    print(f"Hello, {user_name}! Welcome to the world of Python.")

if __name__ == "__main__":
    main()