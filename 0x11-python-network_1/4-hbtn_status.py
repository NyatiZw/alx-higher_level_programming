#!/usr/bin/python3
"""
Script to fetch https resources
"""


from requests import get

url = "https://alx-intranet.hbtn.io/status"

res = get(url)
body = res.text

res_type = type(body).__name__
formatted_body = f"- type: {res_type}"

print("Body response:")
print(formatted_body)
print ("- content:", body)


if __name__ == "__main__":
    pass
