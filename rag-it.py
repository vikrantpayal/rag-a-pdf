from torch import cuda 

device      = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu' 
device

from langchain_community.llms import HuggingFaceEndpoint # NEXT how do I import HF endpoint?
from langchain.prompts import PromptTemplate