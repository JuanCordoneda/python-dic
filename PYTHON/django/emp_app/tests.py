import datetime

from django.test import TestCase
from django.utils import timezone
import unittest
# from .models import Question
import unittest

# Identificar el problema.
# Crear Test para solucionar el problema
# Correr los test
# Solucionar el problema
# Volver a correr los test

class TestAssertions(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(2 + 2, 4)  # Verifica si dos valores son iguales

    def test_assert_not_equal(self):
        self.assertNotEqual(2 + 2, 5)  # Verifica si dos valores no son iguales

    def test_assert_true(self):
        self.assertTrue(5 > 3)  # Verifica si una condición es verdadera

    def test_assert_false(self):
        self.assertFalse(5 < 3)  # Verifica si una condición es falsa

    def test_assert_is(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)  # Verifica si dos objetos son el mismo

    def test_assert_is_not(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertIsNot(a, b)  # Verifica si dos objetos no son el mismo

    def test_assert_in(self):
        lista = [1, 2, 3, 4]
        self.assertIn(3, lista)  # Verifica si un valor está presente en una lista

    def test_assert_not_in(self):
        lista = [1, 2, 3, 4]
        self.assertNotIn(5, lista)  # Verifica si un valor no está presente en una lista

    def test_assert_raises(self):
        def division(a, b):
            return a / b
        self.assertRaises(ZeroDivisionError, division, 5, 0)  # Verifica si se produce una excepción específica

    def test_assert_almost_equal(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3)  # Verifica si dos valores son casi iguales (dentro de una tolerancia)

    def test_assert_not_almost_equal(self):
        self.assertNotAlmostEqual(0.1 + 0.2, 0.5)  # Verifica si dos valores no son casi iguales (fuera de una tolerancia)

    def extras(self):
        self.assertEqual(response.status_code, 200)                 #testea que la vista se mande
        self.assertContains(response, "Present Question")           #testea que contenga
        self.assertNotContains(response, "Future Question")         #testea que NO contenga
        self.assertQuerysetEqual(response.context["latest_question_list"], []) #testea que la query sea vacia

if __name__ == '__main__':
    unittest.main()

# python3 manage.py tests emp_app
class QuestionModelTests(TestCase):

    def test_questions_with_future_pub_date(self):
        """Questions with date greater to timezone.now shouldn't be displayed"""
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(question_text = "This is a Question for the test", pub_date = time)
        future_question.save()
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)                 #testea que la vista se mande
        self.assertContains(response, "Present Question")           #testea que contenga
        self.assertNotContains(response, "Future Question")         #testea que NO contenga
        self.assertQuerysetEqual(response.context["latest_question_list"], []) #testea que la query sea vacia
