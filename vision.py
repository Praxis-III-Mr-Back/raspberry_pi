from gradio_client import Client
from github import Github
import os
import time

class Vision:
    def __init__(self):
        self.client = Client("https://llava.hliu.cc/")
        github_key = os.environ.get('GITHUB_KEY')
        if not github_key:
            raise Exception('GITHUB_KEY not found')
        self.github = Github(github_key)
        self.repo = self.github.get_repo('con266667/Praxis-III-image-database')

    def upload_image(self, file_name):
        try:
            with open(file_name, 'rb') as file:
                data = file.read()
            self.repo.create_file('data/' + file_name, 'upload png', data, branch='main')
        except Exception as e:
            print('File already exists or error occurred:', e)

    def analyze_image(self, file_name):
        start_time = time.time()

        # First prediction
        result = self.client.predict(
            'A disease in plants is recognizable by unusual light discoloring and/or spotting. On a balance of probabilities, determine whether or not the plant in the image has this disease. Start your reply with "YES", "NO" or "NOT A PLANT".',
            "https://raw.githubusercontent.com/con266667/Praxis-III-image-database/main/data/" + file_name,
            "Crop",
            api_name="/add_text_1"
        )

        # Second prediction
        result = self.client.predict(
            "llava-v1.6-34b",
            0.2, # temperature
            0.7, # top_p
            10, # max_length
            api_name="/http_bot"
        )

        llm_result = result[0][1]
        if "YES" in llm_result.upper():
            print("Diseased")
        elif "NOT A PLANT" in llm_result.upper():
            print("Not a plant")
        else:
            print("Healthy")

        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    vision = Vision()
    file_name = 'notplant.png'
    vision.upload_image(file_name)
    vision.analyze_image(file_name)
