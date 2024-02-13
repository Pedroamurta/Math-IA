from generate_feedback import word_feedbacks


    
word_feedback_probability = {}
for word in word_feedbacks:
    checked_feedbacks = []
    feedback_probability = []
    feed_list = word_feedbacks[word]
    for feedback in feed_list:
        if feedback in checked_feedbacks:
            pass
        else:
            pattern = feed_list.count(feedback)
            prob = pattern/len(feed_list)
            feedback_probability.append(prob)
    word_feedback_probability[word] = feedback_probability

