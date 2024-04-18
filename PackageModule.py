import pandas as pd

def calculate_mean(data):
    return data.mean()

def calculate_median(data):
    return data.median()

def calculate_mode(data):
    return data.mode()

def calculate_standard_deviation(data):
    return data.std()

# Contoh penggunaan:
if __name__ == "__main__":
    # Data contoh
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Menghitung statistik
    print("Mean:", calculate_mean(data))
    print("Median:", calculate_median(data))
    print("Mode:", calculate_mode(data))
    print("Standard Deviation:", calculate_standard_deviation(data))
