import os
import requests

projects = [
    {
        "slug": "the-gadget-point",
        "banner": "https://placehold.co/2000x872/e72929/ffffff?text=The+Gadget+Point&font=lora",
        "thumbnail": "https://placehold.co/1080x1080/e72929/ffffff?text=The+Gadget+Point\n\nThumbnail&font=lora",
        "gallery": [
            "https://placehold.co/1080x1080/e72929/ffffff?text=The+Gadget+Point\nGallery+1&font=Lora",
            "https://placehold.co/1080x1080/e72929/ffffff?text=The+Gadget+Point\nGallery+2&font=Lora",
            "https://placehold.co/1080x1920/e72929/ffffff?text=The+Gadget+Point\nGallery+3&font=Lora",
            "https://placehold.co/1080x1920/e72929/ffffff?text=The+Gadget+Point\nGallery+4&font=Lora",
            "https://placehold.co/1080x1080/e72929/ffffff?text=The+Gadget+Point\nGallery+5&font=Lora",
            "https://placehold.co/1920x1920/e72929/ffffff?text=The+Gadget+Point\nGallery+6&font=Lora",
            "https://placehold.co/1080x1080/e72929/ffffff?text=The+Gadget+Point\nGallery+7&font=Lora",
            "https://placehold.co/1920x1080/e72929/ffffff?text=The+Gadget+Point\nGallery+8&font=Lora",
            "https://placehold.co/1080x1080/e72929/ffffff?text=The+Gadget+Point\nGallery+9&font=Lora",
        ],
    },
]


def download_images(project):
    # Create project folder
    folder_name = project["slug"]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Download banner image
    response = requests.get(project["banner"])
    with open(os.path.join(folder_name, "banner.svg"), "wb") as f:
        f.write(response.content)

    # Download thumbnail image
    response = requests.get(project["thumbnail"])
    with open(os.path.join(folder_name, "thumbnail.svg"), "wb") as f:
        f.write(response.content)

    # Download gallery images
    for i, url in enumerate(project["gallery"], 1):
        response = requests.get(url)
        with open(os.path.join(folder_name, f"gallery-{i}.svg"), "wb") as f:
            f.write(response.content)
        print(f"Downloaded gallery-{i} for {project['slug']}")


# Loop through all projects and download their images
for project in projects:
    download_images(project)
    print(f"Finished downloading images for {project['slug']}")
