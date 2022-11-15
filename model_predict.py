import pickle
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from sklearn.preprocessing import PolynomialFeatures
def prediction(img):
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
    mydata = [max_gry, min_gry, mean_gry, std_gry, mean_lu, std_lu, mean_r, std_r, mean_g, std_g, mean_b, std_b]
    final_data = [np.array(mydata)]
    poly = PolynomialFeatures(degree=3)
    model = pickle.load(open('linearmodel.pkl', 'rb'))
    data = poly.fit_transform(final_data)
    output = model.predict(data)
    final_output = abs(output)
    return final_output

