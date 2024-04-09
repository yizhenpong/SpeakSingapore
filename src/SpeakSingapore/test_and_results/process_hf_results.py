import pandas as pd
pd.set_option('display.max_columns', 500)

df = pd.read_parquet("./src/SpeakSingapore/test_and_results/test.parquet")

rs = pd.read_parquet("./src/SpeakSingapore/test_and_results/test_result.parquet")

print(df["output"]) # Expected output
print(rs["results"]) # Actual output

result_dataframe = pd.DataFrame({
    "expected_output": df["output"],
    "actual_output": rs["results"]
})

result_dataframe.to_csv("./src/SpeakSingapore/test_and_results/result_df.csv")