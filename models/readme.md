# Model Merging Instructions

This directory contains a script `merge.py` to combine the split parts of a model into a single file.

## Steps to Combine the Model Parts

1. Ensure all the model parts (`model_part0.pkl`, `model_part1.pkl`, ..., `model_partN.pkl`) are present in this directory.
2. Open the `merge.py` script and verify the `NUMBER_OF_PARTS` variable matches the total number of parts.
3. Run the script using the following command:
   ```bash
   python merge.py
   ```
4. After execution, the combined model will be saved as `model.pkl` in the same directory.

## Notes

- Ensure Python is installed on your system.
- Do not modify the individual model parts before running the script.
