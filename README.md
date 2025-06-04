# Book-Recommendation
📚 Book Recommendation API
A content-based book recommendation system built with Python and Flask. This API takes a book title as input and returns similar book recommendations using TF-IDF vectorization and cosine similarity on author and genre/description data.

🚀 Features
Recommends similar books based on content (author + genre/description)

API built with Flask for easy integration into apps or frontends

Scalable to thousands of books (tested with Goodbooks-10k dataset)

Case-insensitive title matching

## 📦 Requirements
Install dependencies using:

pip install flask pandas scikit-learn
## 📁 Dataset
Place a books.csv file in the project directory. It should include at least the following columns:

title,author,genre
1984,George Orwell,Dystopian Fiction
Pride and Prejudice,Jane Austen,Romance Classic
...
You can use datasets like Goodbooks-10k or create your own.

## 🧠 How It Works
The API reads a CSV file of books.

It combines text features (like author and genre) for each book.

These features are vectorized using TF-IDF.

Cosine similarity is calculated between all books.

When a user queries a book, the most similar ones are returned.

## ⚙️ How to Run

python app.py
Then visit:

arduino
http://127.0.0.1:5000/recommend?title=BookTitle
Example:

arduino

http://127.0.0.1:5000/recommend?title=1984
## 📤 Example JSON Response

{
  "input": "1984",
  "recommendations": [
    "Brave New World",
    "Fahrenheit 451",
    "Animal Farm",
    "The Handmaid's Tale",
    "Lord of the Flies"
  ]
}
## 🔄 API Endpoint
Method	Endpoint	Description
GET	/recommend	Returns similar book titles

📌 Parameters
title – The title of the book you want recommendations for

📌 Error Handling
If no title is provided:
{ "error": "Please provide a book title using ?title=bookname" }

If book is not found:
{ "error": "Book not found in the database" }

## 🌐 Deployment
You can deploy this API using:

Render

Heroku

Railway

Dockerized containers (optional)

## 💡 Future Enhancements
Add user-based collaborative filtering

Include book summaries/descriptions for better accuracy

Enable fuzzy matching for similar book titles

Frontend using Streamlit or React

