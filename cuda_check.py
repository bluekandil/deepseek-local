import torch

if torch.cuda.is_available():
    print("PyTorch is running on GPU")
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
else:
    print("PyTorch is running on CPU")