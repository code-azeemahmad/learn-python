import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data
        first_name = user_data['data']['name']['first']
        country = user_data['data']['location']['country']  # inspect with .key() at each level
        return first_name, country
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        first_name, country = fetch_random_user()
        print(f"First name: {first_name}, Country: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()


'''
print(data.keys())
print(data["data"].keys())
print(data["data"]["location"].keys())
print(data["data"]["location"]["country"])
'''