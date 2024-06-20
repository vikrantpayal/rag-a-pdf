from torch import cuda 
from langchain_community.llms import HuggingFaceEndpoint # NEXT how do I import HF endpoint?
from langchain.prompts import PromptTemplate
import os
from getpass import getpass

device      = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu' 
device

hfapi_key = getpass("Enter you HuggingFace access token:")
os.environ["HF_TOKEN"] = hfapi_key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = hfapi_key

