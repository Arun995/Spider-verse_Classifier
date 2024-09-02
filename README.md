# Spider-verse_Classifier

## Introduction

The Spider-Verse Classifier is a machine learning project aimed at classifying images of actors who have portrayed Spider-Man in various movies. The classifier uses machine learning algorithms to analyze images and predict which Spider-Man actor is featured. This project leverages automated data collection through a Pinterest scraper and machine learning techniques to achieve its goal.

## Objective

The primary goal of this project is to develop a machine learning model that can accurately classify images of Spider-Man actors. The project is interesting due to the diverse appearances of Spider-Man across different movies and the challenge of distinguishing between these variations.

## Data Collection

For data collection, images of Spider-Man actors were gathered using a Pinterest scraper. This tool was utilized to automate the process of collecting images from Pinterest, which significantly sped up the data gathering process. The scraper helped collect a large number of images, which were essential for training the machine learning model.

### Challenges

- **Data Volume**: Ensuring a large and diverse dataset for training the model.
- **Image Variability**: Handling different costumes, poses, and lighting conditions in images.

## Methodology

The classifier was built using traditional machine learning techniques rather than deep learning. The methodology includes:

1. **Data Preprocessing**: Images were resized and transformed to create feature vectors suitable for machine learning.
2. **Feature Extraction**: Features were extracted from the images using techniques such as histogram of oriented gradients (HOG).
3. **Model Training**: A machine learning model was trained using the processed image data.
4. **Evaluation**: The model's performance was evaluated using metrics such as accuracy.

## Implementation

Here’s a brief overview of the implementation:

1. **Data Preprocessing**: Images are cropped and resized.
2. **Feature Extraction**: HOG features are extracted and combined with raw pixel values.
3. **Model Training**: A machine learning model is trained on the processed data.

### Code Snippet

```python
def classify_image(image_base64_data):
    imgs = get_cropped_image_if_2_eyes(image_base64_data)
    result = []
    for img in imgs:
        scalled_raw_img = cv2.resize(img, (32, 32))
        img_har = w2d(img, 'db1', 5)
        scalled_img_har = cv2.resize(img_har, (32, 32))
        combined_img = np.vstack((scalled_raw_img.reshape(32 * 32 * 3, 1), scalled_img_har.reshape(32 * 32, 1)))
        final = combined_img.reshape(1, 32*32*3 + 32*32).astype(float)
        result.append({
            'class': class_number_to_name(__model.predict(final)[0]),
            'class_probability': np.around(__model.predict_proba(final)*100,2).tolist()[0],
            'class_dictionary': __class_name_to_number
        })
    return result

