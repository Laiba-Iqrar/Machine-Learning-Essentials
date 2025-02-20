import pandas as pd

def filter_mnist(input_file="D:\Jupyter-Notebook-Crash-Course\Datasets\mnist.csv", output_file="filtered_mnist.csv"):
    # Load the dataset
    df = pd.read_csv(input_file)
    
    # Filter rows where the label column (index 0) is 4, 5, or 8
    filtered_df = df[df.iloc[:, 0].isin([4, 5, 8])]
    
    # Move the label column to the end
    label_column = filtered_df.iloc[:, 0]
    filtered_df = filtered_df.iloc[:, 1:]
    filtered_df["label"] = label_column
    
    # Save the filtered dataset to a new file
    filtered_df.to_csv(output_file, index=False)
    print(f"Filtered data saved to {output_file}")

# Run the function
filter_mnist()
