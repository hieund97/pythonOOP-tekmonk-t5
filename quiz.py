class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self._answer = answer

    @property
    def answer(self):
        """Getter method to access the answer."""
        return self._answer

    @answer.setter
    def answer(self, new_answer):
        """Setter method to update the answer."""
        if not new_answer:
            raise ValueError("Answer cannot be empty")
        self._answer = new_answer

    @answer.deleter
    def answer(self):
        """Deleter method to delete the answer."""
        print("Deleting the answer...")
        del self._answer

    def check_answer(self, user_answer):
        """Regular method to check if the user's answer is correct."""
        return self.answer.lower() == user_answer.lower()

    @staticmethod
    def print_welcome_message():
        """Static method to print a welcome message."""
        print("Welcome to the Python Quiz! Let's test your knowledge.")

    @classmethod
    def create_default_questions(cls):
        """Class method to create a default set of questions."""
        default_questions = [
            cls("What is the capital of France? ", "Paris"),
            cls("What is 2 + 2? ", "4"),
            cls("What is the color of the sky on a clear day? ", "Blue"),
        ]
        return default_questions


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        """Start the quiz and ask all questions."""
        for question in self.questions:
            user_answer = input(question.prompt)
            if question.check_answer(user_answer):
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
        self.display_score()

    def display_score(self):
        """Display the final score."""
        print(f"Your final score is: {self.score} out of {len(self.questions)}")


# Sử dụng chương trình
if __name__ == "__main__":
    Question.print_welcome_message()
    
    # Tạo câu hỏi mặc định sử dụng class method
    questions = Question.create_default_questions()
    
    # Tạo quiz với các câu hỏi
    quiz = Quiz(questions)
    
    # Bắt đầu quiz
    quiz.start()
