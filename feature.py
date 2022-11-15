import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import json
import os
def feature_extraction(img):
    img = Image.open(img)
    gry = img.convert('L')
    img = np.array(img)
    enhancer = ImageEnhance.Contrast(gry)
    enhanced_im = enhancer.enhance(4)
    image_succ = enhanced_im.filter(ImageFilter.MinFilter)

    img_clean = np.asarray(image_succ)
    img_reshape = img_clean[np.newaxis,...]

    #img_gray = image_succ.getdata()
    min_gry = np.min(img_reshape[:])
    max_gry = np.max(img_reshape[:])
    mean_gry = np.mean(img_reshape[:])
    std_gry = np.std(img_reshape[:])
    avg_color = np.array(img).mean(axis=(0, 1))
    std_color = np.array(img).std(axis=(0, 1))
    avg_rgb = avg_color[::-1]
    std_rgb = std_color[::-1]
    mean_r = avg_rgb[0]
    mean_g = avg_rgb[1]
    mean_b = avg_rgb[2]
    std_r = std_rgb[0]
    std_g = std_rgb[1]
    std_b = std_rgb[2]
    pixelRGB1 = avg_rgb[0]*0.2126
    pixelRGB2 = avg_rgb[1]*0.7152
    pixelRGB3 = avg_rgb[2]*0.0722
    luminance = [pixelRGB1, pixelRGB2, pixelRGB3]
    mean_lu = np.mean(luminance)
    std_lu = np.std(luminance)
    min_gry = str(min_gry)
    max_gry = str(max_gry)
    mean_gry = str(round(mean_gry, 2))
    std_gry = str(round(std_gry, 2))
    mean_r = str(np.round(mean_r, 2))
    mean_g = str(np.round(mean_g, 2))
    mean_b = str(np.round(mean_b, 2))
    std_r = str(round(std_r, 2))
    std_g = str(round(std_g, 2))
    std_b = str(round(std_b, 2))
    mean_lu = str(np.round(mean_lu, 2))
    std_lu = str(np.round(std_lu, 2))

    data = {
        "feature": [
            {
                "max_gry": max_gry,
                "min_gry": min_gry,
                "mean_gry": mean_gry,
                "std_gry": std_gry,
                "mean_lu": mean_lu,
                "std_lu": std_lu,
                "mean_r": mean_r,
                "std_r": std_r,
                "mean_g": mean_g,
                "std_g": std_g,
                "mean_b": mean_b,
                "std_b": std_b,
                
            }
        ]
    }
    if os. path. exists('static/data/data.json'):
        os. remove('static/data/data.json')

    with open('static/data/data.json', 'w') as f:
        json.dump(data, f)
    return data
