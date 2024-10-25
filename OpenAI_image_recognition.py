import os
from openai import OpenAI # pip install openai
from keys import open_ai_api_key # you must enter your OpenAI API key in a file called keys.py

client = OpenAI(
    api_key=open_ai_api_key
)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What type of plant is this? What are some of it's characteristics? please output raw text instead of markdown."},
        {
          "type": "image_url",
          "image_url": {
            "url": "http://res.cloudinary.com/de24b2xsz/image/upload/v1729885095/rmqdrdldxa9cpmxfl3wx.jpg",
          },
        },
      ],
    }
  ],
  temperature=0,
  max_tokens=300,
)

print(response.choices[0].message.content)



#https://perenual.com/storage/species_image/8652_maranta_leuconeura_erythroneura/og/Maranta_leuconeura_erythroneura_2zz.jpg