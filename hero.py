class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check(self, answer):
        return answer == self.answer

question_1 = Question("Текст вопроса?", "правильный ответ")
print(question_1.check("test"))
print(question_1.check("правильный ответ"))