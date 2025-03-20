import pickle
NUMBER_OF_PARTS = 3

with open("model.pkl", "wb") as f:
    for i in range(NUMBER_OF_PARTS):
        with open(f"model_part{i}.pkl", "rb") as part:
            f.write(part.read())