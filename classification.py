# import streamlit as st
# from PIL import Image
# from keras.preprocessing.image import load_img, img_to_array
# import numpy as np
# from keras.models import load_model
# import requests
# from bs4 import BeautifulSoup
# import cv2

# model1 = load_model('FV.h5')

# labels1 = {0: 'Beans ', 1:'Beetroot ' , 2:'Brinjal',  3:'Broadbeas',4:'Cabbage', 5:'Carrot', 
#           6: 'Chilly', 7:'Chowchow',8:'Drumstick',9:'Guava', 10:'Ladysfinger', 11:'Lemon',12:'Ridgeguard',13:'Tomato ',14:'Turkey berry'}
# model2=load_model('MODEL2.h5')
# labels2={0:'Preserved',1:'Unpreserved'}

# def fetch_calories(prediction):
#     try:
#         url = 'https://www.google.com/search?&q=calories in ' + prediction
#         req = requests.get(url).text
#         scrap = BeautifulSoup(req, 'html.parser')
#         calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
#         return calories
#     except Exception as e:
#         st.error("Can't able to fetch the Calories")
#         print(e)

# def fetch_potassium(prediction):
#     try:
#         url = 'https://www.google.com/search?&q=potassium in ' + prediction
#         req = requests.get(url).text
#         scrap = BeautifulSoup(req, 'html.parser')
#         calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
#         return calories
#     except Exception as e:
#         st.error("Can't able to fetch the potassium")
#         print(e)
# def fetch_iron(prediction):
#     try:
#         url = 'https://www.google.com/search?&q=iron in ' + prediction
#         req = requests.get(url).text
#         scrap = BeautifulSoup(req, 'html.parser')
#         iron = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
#         return iron
#     except Exception as e:
#         st.error("Can't able to fetch the iron")
#         print(e)
# def fetch_calcium(prediction):
#     try:
#         url = 'https://www.google.com/search?&q=calcium in ' + prediction
#         req = requests.get(url).text
#         scrap = BeautifulSoup(req, 'html.parser')
#         calcium = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
#         return calcium
#     except Exception as e:
#         st.error("Can't able to fetch the calcium")
#         print(e)
# def fetch_protein(prediction):
#     try:
#         url = 'https://www.google.com/search?&q=protein in ' + prediction
#         req = requests.get(url).text
#         scrap = BeautifulSoup(req, 'html.parser')
#         protein = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
#         return protein
#     except Exception as e:
#         st.error("Can't able to fetch the protein")
#         print(e)


# def processed_img(img_path,model):
#     img=load_img(img_path,target_size=(224,224,3))
#     img=img_to_array(img)
#     img=img/255
#     img=np.expand_dims(img,[0])
#     answer=model.predict(img)
#     y_class = answer.argmax(axis=-1)
#     res=labels1[y_class[0]] if model==model1 else labels2[y_class[0]]
#     return res.capitalize()

# vegetable_conditions = {
#     'Carrot': {
#         'preserved': 'Carrots can typically be stored for 2-4 weeks in the refrigerator.',
#         'unpreserved': 'Carrots should be stored in a plastic bag in the refrigerator for up to 2 weeks.'
#     },
#     'Beans': {
#         'preserved': 'Beans can be canned and stored for up to 1 year in a cool, dark place.',
#         'unpreserved': 'Fresh beans should be stored in a perforated plastic bag in the refrigerator for up to 1 week.'
#     },
#     # Add more vegetables and their conditions as needed
# }

# def ripe_status(avgR, avgG, avgB):
#     # Define threshold values for ripe carrots
#     ripe_thresholdR = 20  # Adjust these threshold values as needed
#     ripe_thresholdG = 20
#     ripe_thresholdB = 10
    
#     # Check if average values of all three channels meet the ripe conditions
#     if avgR >= ripe_thresholdR and avgG >= ripe_thresholdG and avgB >= ripe_thresholdB:
#         return "Ripe"
#     else:
#         return "Not Ripe"

# def run():
#     # Add a dictionary mapping predictions to static image files
#     prediction_to_image = {
#         'Carrot': 'static_image/carrot_image.jpeg',
#         'Beans':  'static_image/beans_image.jpg',
#         'Brinjal': 'static_image/brinjal_image.jpg',
#         'Beetroot': 'static_image/Beetroot_image.jpg',
#         'Lemon':   'static_image/lemon_image.jpg',
#         'Cabbage' : 'static_image/cabbage.jpg'
#         # Add more mappings as needed
#     }
    
#     st.title("Nutritional Evaluation In Regional 🍍 Fruits And 🍅 Vegetables")
#     img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
#     if img_file is not None:
#         img = Image.open(img_file).resize((250,250))
#         st.image(img,use_column_width=False)
#         save_image_path = './upload_images/'+img_file.name
#         with open(save_image_path, "wb") as f:
#             f.write(img_file.getbuffer())       

#         if img_file is not None:
#             result1= processed_img(save_image_path,model1)
#             result2= processed_img(save_image_path,model2)
#             st.success("**Predicted : "+result1+'**')
#             st.success("**Predicted : "+result2+'**')

#             if result1 in prediction_to_image:
#                 prediction_image_path = prediction_to_image[result1]
#                 prediction_img = Image.open(prediction_image_path).resize((250, 250))
#                 st.image(prediction_img, caption=f"Image for {result1}", use_column_width=False)
#             else:
#                 st.warning("Static image for this prediction is not available.")

#             cal = fetch_calories(result1)
#             if cal:
#                 st.warning('**'+cal+'(100 grams)**')
#             cal = fetch_potassium(result1)
#             if cal:
#                 st.warning('**'+cal+ '(Potassium)**')
#             ir=fetch_iron(result1)
#             if ir:
#                 st.warning('**'+ir+'(Iron)**')
#             ca=fetch_calcium(result1)
#             if ca:
#                 st.warning('**'+ca+'(Calcium)**')
#             pro=fetch_protein(result1)
#             if pro:
#                 st.warning('**'+pro+'(Protein)**')

#             if result2 == 'Preserved':
#                st.info('**This item is preserved.**')
#                if result1 in vegetable_conditions:
#                   st.info(vegetable_conditions[result1]['preserved'])
#                else:
#                   st.warning('Preservation information for this item is not available.')
#             elif result2 == 'Unpreserved':
#                   st.info('**This item is unpreserved. Additional nutritional information may vary.**')
#                   if result1 in vegetable_conditions:
#                      st.info(vegetable_conditions[result1]['unpreserved'])
#                   else:
#                       st.warning('Storage information for this item is not available.')

#             # Display ripeness status
#             img_cv2 = cv2.imread(save_image_path)
#             r_values = img_cv2[:, :, 2].flatten()
#             g_values = img_cv2[:, :, 1].flatten()
#             b_values = img_cv2[:, :, 0].flatten()
#             avgR = np.mean(r_values)
#             avgG = np.mean(g_values)
#             avgB = np.mean(b_values)
#             st.success("**Average RGB Values: R=" + str(avgR) + ", G=" + str(avgG) + ", B=" + str(avgB) + "**")
#             ripeness_status = ripe_status(avgR, avgG, avgB)
#             st.success("**Ripeness Status: " + ripeness_status + "**")
#         else:
#             st.error("Failed to save the image file. Please check the save path.")

# run()

import streamlit as st
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model
import requests
from bs4 import BeautifulSoup
import cv2

model1 = load_model('FV.h5')

labels1 = {0: 'Beans', 1:'Beetroot' , 2:'Brinjal',  3:'Broadbeas',4:'Cabbage', 5:'Carrot', 
          6: 'Chilly', 7:'Chowchow',8:'Drumstick',9:'Guava', 10:'Ladysfinger', 11:'Lemon',12:'Ridgeguard',13:'Tomato',14:'Turkey berry'}
model2 = load_model('MODEL2.h5')
labels2 = {0:'Preserved',1:'Unpreserved'}

def fetch_calories(prediction):
    try:
        url = 'https://www.google.com/search?&q=calories in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return calories
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)

def fetch_potassium(prediction):
    try:
        url = 'https://www.google.com/search?&q=potassium in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        potassium = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return potassium
    except Exception as e:
        st.error("Can't able to fetch the Potassium")
        print(e)

def fetch_iron(prediction):
    try:
        url = 'https://www.google.com/search?&q=iron in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        iron = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return iron
    except Exception as e:
        st.error("Can't able to fetch the Iron")
        print(e)

def fetch_calcium(prediction):
    try:
        url = 'https://www.google.com/search?&q=calcium in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calcium = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return calcium
    except Exception as e:
        st.error("Can't able to fetch the Calcium")
        print(e)

def fetch_protein(prediction):
    try:
        url = 'https://www.google.com/search?&q=protein in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        protein = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return protein
    except Exception as e:
        st.error("Can't able to fetch the Protein")
        print(e)

def processed_img(img_path, model):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    res = labels1[y_class[0]] if model == model1 else labels2[y_class[0]]
    return res.capitalize()

vegetable_conditions = {
    'Carrot': {
        'preserved': 'Carrots can typically be stored for 2-4 weeks in the refrigerator.',
        'unpreserved': 'Carrots should be stored in a plastic bag in the refrigerator for up to 2 weeks.'
    },
    'Beans': {
        'preserved': 'Beans can be canned and stored for up to 1 year in a cool, dark place.',
        'unpreserved': 'Fresh beans should be stored in a perforated plastic bag in the refrigerator for up to 1 week.'
    },
    'Lemon': {
        'preserved': 'Preserved lemons can last up to 6 months in a cool, dark place.',
        'unpreserved': 'Unpreserved lemons can last 2-4 weeks in the refrigerator.'
    },
    'Brinjal': {
        'preserved': 'Preserved brinjals can last up to 3 months in a cool, dark place.',
        'unpreserved': 'Unpreserved brinjals should be stored in the refrigerator for up to 1 week.'
    },
    'Beetroot': {
        'preserved': 'Canned or pickled beetroots can last up to 1 year.',
        'unpreserved': 'Unpreserved beetroots can last 2-3 weeks in the refrigerator.'
    },
    'Guava': {
        'preserved': 'Preserved guavas can last up to 1 year in a cool, dark place.',
        'unpreserved': 'Unpreserved guavas can be stored for 3-5 days at room temperature.'
    },
    'Tomato': {
        'preserved': 'Canned or jarred tomatoes can last up to 2 years in a cool, dark place.',
        'unpreserved': 'Unpreserved tomatoes can last 1-2 weeks if stored at room temperature.'
    },
    # Add more vegetables and their conditions as needed
}


def ripe_status(avgR, avgG, avgB):
    # Define threshold ranges for red, green, and blue mean values for different ripeness categories
    red_ranges = {
        'Underripe': (0.0, 30.0),
        'Ripe': (30.0, 100.0),
        'Overripe': (100.0, 255.0)
    }
    green_ranges = {
        'Underripe': (0.0, 29.0),
        'Ripe': (29.0, 100.0),
        'Overripe': (100.0, 255.0)
    }
    blue_ranges = {
        'Underripe': (0.0, 15.0),
        'Ripe': (15.0, 100.0),
        'Overripe': (100.0, 255.0)
    }
    
    # Check the red, green, and blue mean values against the defined ranges
    ripeness_status = None
    for category, (minR, maxR) in red_ranges.items():
        if minR <= avgR <= maxR:
            for cat, (minG, maxG) in green_ranges.items():
                if minG <= avgG <= maxG:
                    for c, (minB, maxB) in blue_ranges.items():
                        if minB <= avgB <= maxB and category == cat == c:
                            ripeness_status = category
                            break
                    if ripeness_status:
                        break
                if ripeness_status:
                    break
            if ripeness_status:
                break

    if ripeness_status:
        return ripeness_status
    else:
        return "Unknown"


def run():
    # Add a dictionary mapping predictions to static image files
    prediction_to_image = {
        'Carrot': 'static_image/carrot_image.jpeg',
        'Beans':  'static_image/beans_image.jpg',
        'Brinjal': 'static_image/brinjal_image.jpeg',
        'Beetroot': 'static_image/image.jpeg',
        'Lemon':   'static_image/lemon_image.jpeg',
        'Tomato' : 'static_image/tomato.jpg',
        'Guava' : 'static_image/guava_image.jpeg'
        # Add more mappings as needed
    }
    
    st.title("Nutritional Evaluation In Regional 🍍 Fruits And 🍅 Vegetables")
    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_column_width=False)
        save_image_path = './upload_images/' + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())       

        if img_file is not None:
            result1 = processed_img(save_image_path, model1)
            result2 = processed_img(save_image_path, model2)
            st.success("Predicted : " + result1 )
            st.success("Predicted : " + result2 )

            if result1 in prediction_to_image:
                prediction_image_path = prediction_to_image[result1]
                prediction_img = Image.open(prediction_image_path).resize((250, 250))
                st.image(prediction_img, caption=f"Image for {result1}", use_column_width=False)
            else:
                st.warning("Static image for this prediction is not available.")

            cal = fetch_calories(result1)
            if cal:
                st.warning('**'+cal+'(100 grams)**')
            cal = fetch_potassium(result1)
            if cal:
                st.warning('**'+cal+ '(Potassium)**')
            ir = fetch_iron(result1)
            if ir:
                st.warning('**'+ir+'(Iron)**')
            ca = fetch_calcium(result1)
            if ca:
                st.warning('**'+ca+'(Calcium)**')
            pro = fetch_protein(result1)
            if pro:
                st.warning('**'+pro+'(Protein)**')

            if result2 == 'Preserved':
                st.info('**This item is preserved.**')
                if result1 in vegetable_conditions:
                    st.info(vegetable_conditions[result1]['preserved'])
                else:
                    st.warning('Preservation information for this item is not available.')
            elif result2 == 'Unpreserved':
                st.info('**This item is unpreserved.**')
                if result1 in vegetable_conditions:
                    st.info(vegetable_conditions[result1]['unpreserved'])
                else:
                    st.warning('Storage information for this item is not available.')

            # Display ripeness status
            img_cv2 = cv2.imread(save_image_path)
            r_values = img_cv2[:, :, 2].flatten()
            g_values = img_cv2[:, :, 1].flatten()
            b_values = img_cv2[:, :, 0].flatten()
            avgR = np.mean(r_values)
            avgG = np.mean(g_values)
            avgB = np.mean(b_values)
            st.success("**Average RGB Values: R=" + str(avgR) + ", G=" + str(avgG) + ", B=" + str(avgB) + "**")
            ripeness_status = ripe_status(avgR, avgG, avgB)
            st.success("**Ripeness Status: " + ripeness_status + "**")
        else:
            st.error("Failed to save the image file. Please check the save path.")

run()

