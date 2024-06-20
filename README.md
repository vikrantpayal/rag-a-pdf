# rag-a-pdf
Running RAG on a science textbook (pdf), uses langchain
A simple program to read a text-heavy pdf, give a user an interface to ask questions, then push answers. 

### Reference:
IISC-TalentSprint AIMLOps Cohort 2 Module 6, Mini-project 2

### Dependencies:
Install langchain, pypdf, torch, transformer, sentence-transformer, langchain_community
Use pip -q install <package>
The -q argument is for quiet install.

### What is:
**cuda** => NVIDIA's CUDA (Compute Unified Device Architecture) parallel computing platform and programming model.CUDA allows developers to use NVIDIA GPUs (Graphics Processing Units) for general purpose processing (GPGPU). This is particularly useful for tasks that require significant computational power, such as deep learning, neural networks, and other machine learning tasks.The torch.cuda module in PyTorch provides several functionalities to interact with CUDA, including but not limited to: Checking for CUDA Availability: You can check if a CUDA-capable GPU is available on your machine. Managing GPU Devices: You can manage multiple GPU devices and specify which device to use for computations.
Memory Management: Functions to allocate and manage GPU memory. Tensor Operations: Operations to move tensors to and from the GPU, and perform computations on GPU tensors.

**f''** => an f before quotes says what follows is a formatted string.

# NEXT
How do I import HF endpoint?
