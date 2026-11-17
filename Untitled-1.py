
import pandas as pd

data = {
    "id": [1, 2, 3],
    "text": [
        "We need political change.",
        "Our opponents are all dangerous.",
        "I disagree with this policy."
    ],
    "likes": [12, 45, 8]
}

df = pd.DataFrame(data)

print(df)

for index, row in df.iterrows():
    print(index, row["text"])


for index, row in df.iterrows():
    print("Index:", index)
    print("Post:", row["text"])
    print("Likes:", row["likes"])
    print("----------")
