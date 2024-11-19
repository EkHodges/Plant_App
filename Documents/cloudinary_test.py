import cloudinary
import cloudinary.uploader

from keys import cloud_name, api_key, api_secret

cloudinary.config(
  cloud_name = cloud_name,
  api_key = api_key,
  api_secret = api_secret
)

response = cloudinary.uploader.upload('Images\purple-coneflower.jpg')
image_url = response['url']
public_id = response['public_id']
print(f"Image URL: {image_url}")

# for deleting the image after getting OpenAI to recognize it
'''
response = cloudinary.uploader.destroy(public_id)

if response['result'] == 'ok':
    print(f"Image with public_id '{public_id}' deleted successfully.")
else:
    print(f"Failed to delete image with public_id '{public_id}'.")
'''
# https://cloudinary.com/documentation/django_image_and_video_upload