import java.util.ArrayList;
import java.util.Scanner;

// Class representing a Question
class Question {
    private String questionText;
    private String[] options;
    private int correctOption; // 1-based index

    public Question(String questionText, String[] options, int correctOption) {
        this.questionText = questionText;
        this.options = options;
        this.correctOption = correctOption;
    }

    public String getQuestionText() {
        return questionText;
    }

    public String[] getOptions() {
        return options;
    }

    public int getCorrectOption() {
        return correctOption;
    }
}

// Class for Quiz logic
class Quiz {
    private ArrayList<Question> questions;
    private int score;

    public Quiz() {
        questions = new ArrayList<>();
        score = 0;
    }

    public void addQuestion(Question question) {
        questions.add(question);
    }

    public void startQuiz() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Online Quiz!");
        System.out.println("Please answer the following questions:");

        for (int i = 0; i < questions.size(); i++) {
            Question q = questions.get(i);
            System.out.println("\nQuestion " + (i + 1) + ": " + q.getQuestionText());

            String[] options = q.getOptions();
            for (int j = 0; j < options.length; j++) {
                System.out.println((j + 1) + ". " + options[j]);
            }

            System.out.print("Enter your answer (1-4): ");
            int userAnswer = scanner.nextInt();

            if (userAnswer == q.getCorrectOption()) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Wrong! The correct answer was: " + options[q.getCorrectOption() - 1]);
            }
        }

        System.out.println("\nQuiz Completed!");
        System.out.println("Your final score is: " + score + "/" + questions.size());
        scanner.close();
    }
}

// Main class to execute the program
public class OnlineQuizSystem {
    public static void main(String[] args) {
        Quiz quiz = new Quiz();

        // Adding questions to the quiz
        quiz.addQuestion(new Question(
            "Who is the Prime Minister of India in 2024?",
            new String[]{"Narendra Modi", "Rahul Gandhi", "Amit Shah", "Arvind Kejriwal"},
            1
        ));

        quiz.addQuestion(new Question(
            "What is the capital of Japan?",
            new String[]{"Seoul", "Tokyo", "Beijing", "Bangkok"},
            2
        ));

        quiz.addQuestion(new Question(
            "Which currency is used in the United Kingdom?",
            new String[]{"Dollar", "Euro", "Pound Sterling", "Yen"},
            3
        ));

        quiz.addQuestion(new Question(
            "Which movie won the Best Picture Oscar in 2023?",
            new String[]{"Everything Everywhere All At Once", "The Fabelmans", "Top Gun: Maverick", "Avatar: The Way of Water"},
            1
        ));

        // Starting the quiz
        quiz.startQuiz();
    }
}
