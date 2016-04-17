"""
1.  What are the three main design advantages that object orientation can provide?
    Explain each concept.

    Abstraction: Hides the nuts and bolts of the code from people who only need
        a basic view of the object (e.g. An engineer maintaining code at Ubermelon
        doesn't need to know how the pickerbot chooses melons, only that it has a
        choose melons method that returns a Melon)

    Encapsulation: Classes keep all the methods and attributes of an object in
        one place. I can look up the Cat class and see all the things that Cats
        do.

    Polymorphism: Allows programmers to focus on what an object does, rather than
        what it is under the hood. If it has a .quack() function, you can call it,
        regardless of whether you're calling mallard.quack() or duck.quack().
        This allows for looping over a collection of different types fo objects,
        as long as they have the method being called.


2.  What is a Class?

    A class is a type of object. It has attributes and methods that have been
    assigned to it, that exist on all instances of that particular Class. (All
    lists have a .append() method, regardless of what they are holding or what
    they are called.)


3.  What is an instance attribute?

    An instance attribute is an attribute that is assigned individually to an 
    instance/instances of a given class. (e.g. There might be no color_color assigned
    to the class Dog(), but fido, an instance of Dog(), might have his color_color
    bound to'Green'. Likewise, the default .breed attribute of Dog() might be 'golden
    retriever', but arfy (an instance of Dog()) might have his .breed attribute set
    to 'beagle'.)


4.  What is a method?

    A method is a function that can be called on a particular object. (.append()
    can be called on all strings).


5.  What is an instance in object orientation?

    In object-orientation, an instance is one particular example of a given class.
    For example, if my_circle = Circle(), my_circle is an instance of the Circle
    class.


6.  How is a class attribute different than an instance attribute?
    Give an example of when you might use each.

    A class attribute is an attribute held by all members of a given class, whereas
    and instance attribute is individual to a particular instance of that class.

    Class attributes should be used when you want to have the same default attribute
    for all members of a class: for instance, all members of the Dog() class have
    a species attribute of 'dog' and a greet attribute of 'woof'.

    Instance attributes are used when you want to differentiate members of a class
    from each other. Not all Dog()s, for example, will have the same name or breed,
    so these attributes should be set individually at the instance level.

"""

"""Crate Python classes to store the given data."""


class Student(object):
    """Student"""

    first_name = None
    last_name = None
    addresss = None


class Question(object):
    """A Question"""

    question = None
    answer = None

    def ask_and_evaluate(self):
        """Prints a question and evaluates the submitted answer"""

        student_answer = raw_input(self.question + "\n")

        return student_answer == self.answer


class Exam(object):
    """An exam"""

    def __init__(self, name):
        """"Initializes Exam with questions"""

        self.questions = []

    def add_question(self, query, correct_answer):
        """Adds a question to the exam"""

        question = Question()

        question.question = query
        question.answer = correct_answer

        self.questions.append(question)

    def administer(self):
        """Asks and evaluates all questions in questions"""

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return score


myquestion = Question()
myquestion.question = 'What is Balloonicorn\'s favorite color?'
myquestion.answer = 'sparkles'

