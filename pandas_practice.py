
import pandas as pd

data = {
    "id": [1, 2, 3, 4],
    "text": [
        "We need political change.",
        "Our opponents are all dangerous.",
        "I disagree with this policy.",
        "Let's go",
    ],
    "likes": [12, 45, 8, 12]
}

df = pd.DataFrame(data)

print(df)
df.to_csv("test_posts.csv", index=False)
df_loaded = pd.read_csv("test_posts.csv")

print(df_loaded.head())

# 1. Nur die Texte auswählen
print(df["text"])

# 2. Nur Posts mit mehr als 10 Likes
popular_posts = df[df["likes"] > 10]
print(popular_posts)

# 3. Durchschnittliche Likes berechnen
mean_likes = df["likes"].mean()
print(mean_likes)



for index, row in df.iterrows():
    
    print("Index:", index)
    print("Post:", row["text"])
    print("Likes:", row["likes"])
    print("----------")

