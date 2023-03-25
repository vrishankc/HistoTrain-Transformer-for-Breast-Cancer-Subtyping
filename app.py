import gradio as gr
import torch
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image

from ensemble_transformers import EnsembleModelForImageClassification
ensemble = EnsembleModelForImageClassification.from_multiple_pretrained(
    "tcvrishank/histo_train_vit", "tcvrishank/histo_train_segformer", "tcvrishank/histo_train_swin"
)

candidate_labels = ["Benign", "InSitu", "Invasive", "Normal"]

def return_prediction(image):
  
    with torch.no_grad():
        outputs = ensemble(image, mean_pool = True)

    logits = outputs.logits[0]
    probs = logits.softmax(dim=-1).numpy()
    scores = probs.tolist()

    result = [
        {"score": score, "label": candidate_label}
        for score, candidate_label in sorted(zip(probs, candidate_labels), key=lambda x: -x[0])
    ]
    result = result[0]
    final = f"This histopathology image shows cells that are {round(result['score'] * 100, 2)}% certain to be {result['label']}."
    return final


demo = gr.Interface(fn=return_prediction, inputs="image", outputs="text")
    
demo.launch(share = True)
