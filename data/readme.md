# Brain Tumor MRI Dataset

This directory contains a sample dataset that is part of a larger dataset available on Kaggle.

## Downloading the Full Dataset

To download the full dataset, use the following Python code:

```python
import kagglehub

# Download the latest version of the dataset
path = kagglehub.dataset_download("masoudnickparvar/brain-tumor-mri-dataset")

print("Path to dataset files:", path)
```

## Notes

- Ensure you have the `kagglehub` library installed. You can install it using:
  ```bash
  pip install kagglehub
  ```
- You may need to configure your Kaggle API credentials. Refer to the [Kaggle API documentation](https://www.kaggle.com/docs/api) for setup instructions.
- The dataset contains MRI images categorized into different classes for brain tumor detection.

## Sample Dataset

The sample dataset provided here is a subset of the full dataset and can be used for testing purposes.
