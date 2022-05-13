import os

from display_objects import ImageFile, ImageFileProxy

if __name__ == '__main__':
    resources = "./resources"
    images = []
    for file in os.listdir(resources):
        images.append(ImageFile(os.path.join(resources, file)))

    for image in images:
        image.display()

    proxies = []
    for file in os.listdir(resources):
        proxies.append(ImageFileProxy(os.path.join(resources, file)))

    for proxy in proxies:
        proxy.display()
