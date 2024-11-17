import os
import requests

projects = [
    {
        "slug": "bright-future-non-profit",
        "banner": "https://placehold.co/2000x872/ff4081/ffffff?text=Bright+Future+Non-Profit&font=Raleway",
        "thumbnail": "https://placehold.co/1080x1080/ff4081/ffffff?text=Bright+Future+Non-Profit\n\nThumbnail&font=Raleway",
        "gallery": [
            "https://placehold.co/1080x1080/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+1&font=Raleway",
            "https://placehold.co/1080x1080/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+2&font=Raleway",
            "https://placehold.co/1080x1920/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+3&font=Raleway",
            "https://placehold.co/1080x1920/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+4&font=Raleway",
            "https://placehold.co/1080x1080/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+5&font=Raleway",
            "https://placehold.co/1920x1920/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+6&font=Raleway",
            "https://placehold.co/1080x1080/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+7&font=Raleway",
            "https://placehold.co/1920x1080/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+8&font=Raleway",
            "https://placehold.co/1080x1080/ff4081/ffffff?text=Bright+Future+Non-Profit\nGallery+9&font=Raleway",
        ],
    },
    {
        "slug": "green-retail-co",
        "banner": "https://placehold.co/2000x872/4caf50/ffffff?text=Green+Retail+Co.&font=Montserrat",
        "thumbnail": "https://placehold.co/1080x1080/4caf50/ffffff?text=Green+Retail+Co.\n\nThumbnail&font=Montserrat",
        "gallery": [
            "https://placehold.co/1080x1080/4caf50/ffffff?text=Green+Retail+Co.\nGallery+1&font=Montserrat",
            "https://placehold.co/1080x1080/4caf50/ffffff?text=Green+Retail+Co.\nGallery+2&font=Montserrat",
            "https://placehold.co/1080x1920/4caf50/ffffff?text=Green+Retail+Co.\nGallery+3&font=Montserrat",
            "https://placehold.co/1080x1920/4caf50/ffffff?text=Green+Retail+Co.\nGallery+4&font=Montserrat",
            "https://placehold.co/1080x1080/4caf50/ffffff?text=Green+Retail+Co.\nGallery+5&font=Montserrat",
            "https://placehold.co/1920x1920/4caf50/ffffff?text=Green+Retail+Co.\nGallery+6&font=Montserrat",
            "https://placehold.co/1080x1080/4caf50/ffffff?text=Green+Retail+Co.\nGallery+7&font=Montserrat",
            "https://placehold.co/1920x1080/4caf50/ffffff?text=Green+Retail+Co.\nGallery+8&font=Montserrat",
            "https://placehold.co/1080x1080/4caf50/ffffff?text=Green+Retail+Co.\nGallery+9&font=Montserrat",
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
