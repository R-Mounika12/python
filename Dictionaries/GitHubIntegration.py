# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

output_list = response.json()
for output in output_list:
    print(output["user"]["login"])

