# Case Study 7: Student Feedback Sentiment Scoring
positive_words = ["good", "excellent", "helpful", "clear", "interesting"]
negative_words = ["bad", "boring", "confusing", "slow", "difficult"]

feedback = input("Enter feedback: ").lower()
words = feedback.split()
positive = 0
negative = 0

for word in words:
    word = word.strip(".,!?")
    if word in positive_words:
        positive = positive + 1
    if word in negative_words:
        negative = negative + 1

score = positive - negative
print("Positive words:", positive)
print("Negative words:", negative)
print("Sentiment score:", score)
if score > 0:
    print("Classification: Positive")
elif score < 0:
    print("Classification: Negative")
else:
    print("Classification: Neutral")
