# ==========================================
# AI Study Assistant CLI
# ==========================================

# ---------- Alias Mapping ----------
# Used to convert short forms into full forms
aliases = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "bfs": "breadth first search",
    "dfs": "depth first search"
}


# ---------- Normalize Function ----------
# Converts input to lowercase and replaces short forms
def normalize(text):
    text = text.lower()
    for short, full in aliases.items():
        text = text.replace(short, full)
    return text


# ---------- Knowledge Base ----------
# Stores questions and answers
knowledge = {
    "artificial intelligence": "AI is the simulation of human intelligence.",
    "machine learning": "ML is a subset of AI that learns from data.",
    "deep learning": "Deep Learning uses neural networks.",
    "search": "Search algorithms help solve problems.",
    "breadth first search": "BFS explores level by level.",
    "depth first search": "DFS explores depth first.",
    "classification": "Predicting categories.",
    "regression": "Predicting continuous values."
}


# ---------- Quiz Questions ----------
questions = [
    {"q": "What is AI?", "a": "artificial intelligence"},
    {"q": "What is ML?", "a": "machine learning"},
    {"q": "What does BFS stand for?", "a": "breadth first search"},
    {"q": "What does DFS stand for?", "a": "depth first search"},
    {"q": "What is classification?", "a": "predicting categories"},
    {"q": "What is regression?", "a": "predicting continuous values"}
]


# ---------- Weak Topics Tracking ----------
# Stores questions answered incorrectly
weak_topics = []


# ---------- Graph for BFS ----------
from collections import deque

graph = {
    "artificial intelligence": ["machine learning", "search"],
    "machine learning": ["deep learning"],
    "search": ["breadth first search", "depth first search"],
    "deep learning": [],
    "breadth first search": [],
    "depth first search": []
}


# ---------- BFS Function ----------
# Traverses related topics level by level
def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in graph.get(node, []):
                queue.append(neighbor)


# ---------- Question Answering ----------
# Matches user query with knowledge base
def ask_question():
    query = normalize(input("Ask your question: "))
    query_words = query.split()

    best_match = None
    max_score = 0

    for key in knowledge:
        score = 0
        for word in query_words:
            if word in key:
                score += 1

        if score > max_score:
            max_score = score
            best_match = key

    if best_match:
        print("Answer:", knowledge[best_match])
    else:
        print("Sorry, I don't know that yet.")


# ---------- Quiz System ----------
import random

# Stores performance scores (used for recommendation)
topic_scores = {}


def take_quiz():
    score = 0

    # Select 3 random questions
    selected_questions = random.sample(questions, 3)

    for item in selected_questions:
        ans = input(item["q"] + " ").lower()
        topic = item["q"]

        if ans == item["a"]:
            print("Correct!")
            score += 1

            # Increase score for correct answer
            topic_scores[topic] = topic_scores.get(topic, 0) + 1

        else:
            print("Wrong! Correct answer is:", item["a"])

            # Add to weak topics list
            if topic not in weak_topics:
                weak_topics.append(topic)

            # Decrease score for wrong answer
            topic_scores[topic] = topic_scores.get(topic, 0) - 1

    print("Your score:", score, "/", len(selected_questions))


# ---------- Weak Topics Display ----------
def show_weak_topics():
    if not weak_topics:
        print("No weak topics! Good job 🎉")
    else:
        print("You need to improve on:")
        for topic in weak_topics:
            print("-", topic)


# ---------- Topic Exploration ----------
# Uses BFS to show related topics
def explore_topics():
    topic = normalize(input("Enter topic: "))

    if topic not in graph:
        print("Topic not found.")
        return

    print("Related topics:")
    bfs(topic)


# ---------- Recommendation System ----------
# Suggests topics based on performance
def recommend_topics():
    print("Recommended topics to study:")

    found = False
    for topic, score in topic_scores.items():
        if score < 0:
            print("-", topic)
            found = True

    if not found:
        print("You're doing great! No weak topics 🎉")


# ---------- Main Menu ----------
def main():
    while True:
        print("\n==============================")
        print("   AI Study Assistant CLI")
        print("==============================")
        print("1. Ask Question")
        print("2. Take Quiz")
        print("3. Weak Topics")
        print("4. Explore Topics (BFS)")
        print("5. Recommended topics")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            ask_question()
        elif choice == "2":
            take_quiz()
        elif choice == "3":
            show_weak_topics()
        elif choice == "4":
            explore_topics()
        elif choice == "5":
            recommend_topics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


# ---------- Run Program ----------
main()