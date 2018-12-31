from sympy import *
from random import *
import helper

class LinearEqns():
    def __init__(self, level, filename):
        x, y = symbols("x,y")
        self.level = level
        self.fn = filename
        self.quest = ""
        self.ans   = ""
        if self.level == 1:
            choice = randint(1, 2)
            if choice == 1:
                # Create equations of the type ax + b = c
                a = randint(2, 11)
                b = randint(1, 10)
                bs = randint(0, 1) * 2 - 1
                x = randint(1, 10)
                xs = randint(0, 1) * 2 - 1
                c = str(a * x * xs + b * bs)

                if bs == -1:
                    bt = '-' + str(b)
                else:
                    bt = '+' + str(b)

                self.quest = str(a) + 'x' + bt + '=' + c
                self.ans = x * xs
                expr = '$$' + str(a) + 'x' + ('+'if bs == 1 else '-') +str(b) + '=' + c + '$$'
            else:
                # Create equations of the type x/a + b = c
                a = randint(2, 11)
                b = randint(1, 10)
                bs = randint(0, 1) * 2 - 1
                c = randint(1, 10)
                cs = randint(0, 1) * 2 - 1
                x = str((c * cs - b * bs) * a)

                if bs == -1:
                    bt = '-' + str(b)
                else:
                    bt = '+' + str(b)
                self.ans = x
                expr = '$$' + '\\frac{x}{' + str(a) + '}'+ ('+'if bs == 1 else '-') +str(b) + '=' + str(c * cs) + '$$'


        preview(latex(expr), viewer='file', filename=self.fn, euler=False)
        helper.new_image(self.fn)

    def get_question(self):
        return self.quest

    def get_answer(self):
        return self.ans

    def check_ans(self, answer):
        return self.ans == answer


my_question = LinearEqns(1, 'test.png')
print(str(my_question.get_answer()))
