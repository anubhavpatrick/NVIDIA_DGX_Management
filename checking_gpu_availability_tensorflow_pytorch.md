### Code to test GPU availability in Tensorflow 2:

```python
import tensorflow as tf
tf.config.list_physical_devices('GPU')
```

### Code to test GPU availability in PyTorch:

```python
# https://wandb.ai/ayush-thakur/dl-question-bank/reports/How-To-Check-If-PyTorch-Is-Using-The-GPU--VmlldzoyMDQ0NTU
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()
```
