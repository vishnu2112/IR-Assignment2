from sklearn.feature_extraction.text import TfidfVectorizer
args = {
    "stop_words": "english",
    "lowercase": True,
    "norm": "l2",
    "use_idf": True,
    "smooth_idf": True,
    "sublinear_tf": True
}
vectorizer = TfidfVectorizer(**args)
docs = [
    "The boxer rebellion",
    "The boxer",
    "The rebellion"
]
train_tdm = vectorizer.fit_transform(docs)

new_doc = ["boxer in rebellion"]
test_tdm = vectorizer.transform(new_doc)

from sklearn.metrics.pairwise import linear_kernel
similarities = linear_kernel(train_tdm, test_tdm)
index = similarities.argsort(axis=None)[-1]
score = similarities[index]
article = docs[index]
print("The query " + new_doc[0] + " is having more similarities with " + article)