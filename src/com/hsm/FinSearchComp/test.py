import requests
from huggingface_hub.file_download import build_hf_headers
from mlcroissant import Dataset

# Login using e.g. `huggingface-cli login` to access this dataset
headers = build_hf_headers()  # handles authentication
jsonld = requests.get("https://huggingface.co/api/datasets/ByteSeedXpert/FinSearchComp/croissant", headers=headers).json()
ds = Dataset(jsonld=jsonld)
records = ds.records("default")
print(records)