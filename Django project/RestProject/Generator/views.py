from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from transformers import pipeline

# Load model once
text_generator = pipeline("text-generation", model="gpt2")

def home(request):
    generated_text = ""
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            result = text_generator(prompt, max_length=100, num_return_sequences=1)
            generated_text = result[0]['generated_text']
    return render(request, "home.html", {"generated_text": generated_text})