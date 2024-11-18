import os
import requests

projects = [
    {
        "slug": "tech-innovations-inc",
        "banner": "https://placehold.co/2000x872/1e90ff/ffffff?text=Tech+Innovations+Inc.&font=Lora",
        "thumbnail": "https://placehold.co/1080x1080/1e90ff/ffffff?text=Tech+Innovations\nInc+Thumbnail&font=Lora",
        "gallery": [
            "https://placehold.co/1080x1080/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+1&font=Lora",
            "https://placehold.co/1080x1080/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+2&font=Lora",
            "https://placehold.co/1080x1920/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+3&font=Lora",
            "https://placehold.co/1080x1920/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+4&font=Lora",
            "https://placehold.co/1080x1080/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+5&font=Lora",
            "https://placehold.co/1920x1920/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+6&font=Lora",
            "https://placehold.co/1080x1080/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+7&font=Lora",
            "https://placehold.co/1920x1080/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+8&font=Lora",
            "https://placehold.co/1080x1080/1e90ff/ffffff?text=Tech+Innovations\nInc+Gallery+9&font=Lora",
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
