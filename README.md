# Context Gated Mixture of Experts

![LICENSE](https://img.shields.io/badge/license-MIT-green)
[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
![PyTorch](https://img.shields.io/badge/pytorch-2.1-yellow)

Demo of Context Gated Mixture of Experts using T-5 base for generative MCQ tasks. 

All Context Gated Mixing source code can be found under `loralib/layers_cgm.py`. Our implementation is built on the original LoRA repository found here: https://github.com/microsoft/LoRA


# Setup
We provide an `environment.yml` file for easy environment setup. The demo only needs a few libraries to run. A list of libraries is provided in `environment_setup.txt` if you wish to manually install the libraries.


# Download
All preprocessed datasets are availible in `datasets`. There is no additional preprocessing needed to run the training and evaluation notebooks in this repository.

If you wish to download the original datasets and preprocess yourself, please visit the pages below:

CommonsenseQA: https://github.com/jonathanherzig/commonsenseqa

MedicalQA: https://github.com/jind11/MedQA

ScienceQA: https://github.com/lupantech/ScienceQA

After downloading, preprocessing can be done in `format_datasets.ipynb`.

# Training and evaluation
All training and evaluation demos are notebooks. Before running training or evaluation, save T-5 base weights by running `python save_base_statedict.py`

The training notebooks can be configured to save checkpoints and figures to a specified directory. 

Use `T5_base_lora_training.ipynb` to train baseline experiments including fully finetuning model weights as well as LoRA finetunes.

Use `T5_base_lora_training_combined_data.ipynb` to train baseline experiments using combined datasets.

Use `T5_lora_cgm_training.ipynb` to train CGM module weights useing finetuned LoRAs.

Use `T5_base_lora_evaluating.ipynb` and `T5_lora_cgm_evaluating.ipynb` to perform standalone evaluation.

We provide finetuned LoRA weights and trained CGM weights in `results/released_weights`.



