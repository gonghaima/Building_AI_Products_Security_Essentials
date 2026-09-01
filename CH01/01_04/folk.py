from transformers import pipeline

pipe = pipeline(
    "text-generation", 
    model="vicclab/FolkGPT",
    device="cuda"
)

x = pipe("There was a kind man who")
print(x[0]['generated_text'])
