import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "User not found or invalid request", "status_code": response.status_code}

# 테스트 코드
def test_github_user_info():
    valid_username = "octocat"  # GitHub의 공식 테스트 계정
    invalid_username = "thisuserdoesnotexist123456"
    
    print("Testing with valid username:")
    valid_response = get_github_user_info(valid_username)
    print(valid_response)
    
    print("\nTesting with invalid username:")
    invalid_response = get_github_user_info(invalid_username)
    print(invalid_response)

if __name__ == "__main__":
    test_github_user_info()
