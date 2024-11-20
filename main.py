from flask import Flask, request, render_template

app = Flask(__name__)

# Creator details
CREATOR_FIRST_NAME = "Siddartha Reddy"
CREATOR_LAST_NAME = "Chinthala"
CREATOR_EMAIL = "chinthst@mail.uc.edu"

# Predefined responses for student queries
RESPONSES = {
    "Does the college have a football team?": (
        "Yes, the college has a football team! It is part of the regional championship league "
        "and has a strong record of achievements. The team practices in the state-of-the-art sports facility, "
        "and students have the opportunity to join various athletic programs and events. "
        "Football games are a major highlight of campus life, fostering a strong sense of community."
    ),
    "Does it offer a Computer Science major?": (
        "Yes, the college offers a comprehensive Computer Science major. The program includes courses in AI, "
        "Data Science, Cybersecurity, Software Development, and more. Students get hands-on experience through projects, "
        "internships, and access to modern computing labs. The faculty comprises industry experts and researchers "
        "who provide guidance for career advancement."
    ),
    "What is the in-state tuition?": (
        "The in-state tuition is $10,000 per semester. This covers access to all academic programs, library facilities, "
        "and campus activities. Financial aid and scholarships are available for eligible students to make education "
        "more affordable. Additionally, payment plans can be set up for flexible tuition fee payments."
    ),
    "Does the college provide on-campus housing?": (
        "Yes, the college provides on-campus housing for students. There are multiple residence halls, each offering "
        "a variety of room options, including single and shared accommodations. Housing includes amenities like high-speed internet, "
        "laundry facilities, and community spaces for socializing. Living on campus promotes a close-knit student community."
    )
}

@app.route('/')
def index():
    # Render the home page to collect user details
    return render_template('index.html')

@app.route('/questions', methods=['POST'])
def questions():
    # Collect user details
    user_first_name = request.form['first_name']
    user_last_name = request.form['last_name']
    user_email = request.form['email']

    # Pass user details to the questions page
    return render_template('questions.html',
                           first_name=user_first_name,
                           last_name=user_last_name,
                           email=user_email)

@app.route('/answers', methods=['POST'])
def answers():
    # Get selected question and user details
    selected_question = request.form['question']
    user_first_name = request.form['first_name']
    user_last_name = request.form['last_name']
    user_email = request.form['email']

    # Fetch response
    answer = RESPONSES.get(selected_question, "I'm sorry, I don't have an answer for that question.")

    # Render summary with response
    return render_template('summary.html',
                           first_name=user_first_name,
                           last_name=user_last_name,
                           email=user_email,
                           creator_first_name=CREATOR_FIRST_NAME,
                           creator_last_name=CREATOR_LAST_NAME,
                           creator_email=CREATOR_EMAIL,
                           question=selected_question,  # Pass full question
                           answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

