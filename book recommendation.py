import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset
def load_data():
    data = {
        'title': [
            'To Kill a Mockingbird',
            'Pride and Prejudice',
            'The Great Gatsby',
            '1984',
            'The Catcher in the Rye'
        ],
        'author': [
            'Harper Lee',
            'Jane Austen',
            'F. Scott Fitzgerald',
            'George Orwell',
            'J.D. Salinger'
        ],
        'genre': [
            'Classic Fiction',
            'Romance Classic',
            'Classic Tragedy',
            'Dystopian Political Fiction',
            'Coming-of-age Fiction'
        ]
    }
    return pd.DataFrame(data)

# Build TF-IDF matrix
def build_similarity_matrix(df):
    df['features'] = df['author'] + " " + df['genre']
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['features'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# Get recommendations
def get_recommendations(title, df, cosine_sim, top_n=3):
    title = title.strip()
    if title not in df['title'].values:
        return None

    idx = df.index[df['title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    book_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[book_indices].tolist()

# Main function
def main():
    df = load_data()
    cosine_sim = build_similarity_matrix(df)

    while True:
        title = input("\nEnter a book title (or type 'exit' to quit): ")
        if title.lower() == 'exit':
            print("Thank you for using the Book Recommender!")
            break
        recommendations = get_recommendations(title, df, cosine_sim)
        if recommendations:
            print("\n📚 Recommended Books:")
            for i, book in enumerate(recommendations, 1):
                print(f"{i}. {book}")
        else:
            print("❌ Book not found in the database. Please try again.")

# Run the recommender
if __name__ == "__main__":
    main()
