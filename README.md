### Inspiration
Breast cancer is a common and severe disease that requires accurate diagnosis for effective treatment. Invasive ductal carcinoma, the most common type of breast cancer, is particularly challenging to diagnose due to the complex nature of its subtypes. Traditional diagnostic methods such as histopathological biopsy can be prone to errors, with misdiagnosis rates as high as 71% for physicians without specialized expertise. Deep learning models have the potential to improve the accuracy and reliability of breast cancer diagnosis by analyzing visual features of histopathology images and identifying biomarkers for different subtypes of the disease.

### What it does
HistoTrain is an ensemble deep-learning pipeline consisting of three state-of-the-art vision transformers (ViT, SegFormer, Swin Transformer) that utilize both image classification and attention-based saliency mapping to accurately diagnose invasive ductal carcinoma and identify potential biomarkers for different subtypes of the disease. The models were trained on the BACH dataset from the ICIAR 2018 Grand Challenge on Breast Cancer Histology Images, which contains both microscopy images and whole-slide images. After training each model for 20-25 epochs with different hyperparameters to ensure diversity, an ensemble pipeline was created to combine the logits from each transformer for improved diagnostic accuracy.

### How I built it
Preprocessing was a key challenge, as some images were highly similar and required dramatic transformations to capture important texture and structural features. Attention-based saliency mapping was used to understand which features of the histopathology images were most important in the diagnostic predictions, with the Swin Transformer producing two attention maps that required careful analysis to produce accurate heat maps. The resulting model achieved high accuracy rates on a test dataset of 40 images, with the Swin Transformer performing best at 92.5%. A web app was created using GradIO to provide an easy-to-read and aesthetically pleasing interface for physicians and patients.

### Accomplishments that I'm proud of
I am proud of building a robust deep-learning model that achieved high accuracy rates in diagnosing breast cancer subtypes. The challenge of developing effective saliency maps and creating an intuitive web app helped me to learn more about the architecture of the model and how to make it more explainable for physicians and patients.

### What I learned
Working on HistoTrain taught me how to plan short-term projects, work with pre-trained models from HuggingFace, and develop methods for making deep-learning models more explainable.

### What's next for HistoTrain – Revolutionizing Breast Cancer Diagnostics
The next step for HistoTrain is to share the tool with physicians and gather feedback for further improvements. This includes developing a mobile app for easier access and adding a gradient color map to the saliency maps for improved interpretability. Ultimately, HistoTrain has the potential to revolutionize breast cancer diagnostics and improve patient outcomes in the clinic.

![alt text](https://github.com/vrishankc/histo_train/blob/main/insitu.png)
In-Situ Cells 
![alt text](https://github.com/vrishankc/histo_train/blob/main/invasive.png)
Invasive Cells
![alt text](https://github.com/vrishankc/histo_train/blob/main/benign.png)
Benign Cells
![alt text](https://github.com/vrishankc/histo_train/blob/main/normal.png)
Normal Cells
