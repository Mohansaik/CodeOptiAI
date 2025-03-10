import os
import sys
from openai import OpenAI

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '.')))

class PySparkOptimizerLLMApp:
    def __init__(self, user_prompt, file_type):
        self.system_prompt_path = './resources/system_prompt_python.txt'  if file_type == "Python" else './resources/system_prompt_sql.txt'
        self.user_prompt = user_prompt
        
        self.client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=os.getenv("GITHUB_TOKEN"),
        )

    def reader(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return file.read()
        else:
            raise FileNotFoundError(f"The file at {file_path} does not exist.")

    def run(self):
        system_prompt = self.reader(self.system_prompt_path)

        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": self.user_prompt,
                },
            ],
            model="gpt-4o-mini",
            temperature=1,
            max_tokens=4096,
            top_p=1,
        )

        return response.choices[0].message.content


if __name__ == "__main__":
    user_prompt = './python_files/user_py_file.py'
    system_prompt = './resources/system_prompt.txt'

    app = PySparkOptimizerLLMApp(user_prompt, system_prompt)
    print(app.run())
