import pandas as pd

if __name__ == "__main__":
    df = pd.read_parquet('/data/datasets/train.parquet')
    path = '/data/datasets/mygenerated.txt'
    with open(path, 'a') as f:
        for i, row in df[['TEXT']].iterrows():
        # df_string = df[['TEXT']].to_string(header=False, index=False)w
            f.write(row['TEXT'] + '\n')