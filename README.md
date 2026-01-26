# UPHAAR
<img width="752" height="420" alt="image" src="https://github.com/user-attachments/assets/6f50c352-5ace-4775-9ed4-9eaa28e3f941" />

"UPHAAR" leverages deep learning to understand visitors' interactions and preferences, recommending gifts that showcase India's rich cultural heritage. The system uses factors like price and visitor traits to offer personalized suggestions of unique, authentic gifts. 


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Supriya Sharma | Java Projects</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background-color: #0d1117;
            color: #e6edf3;
        }

        header {
            background: linear-gradient(90deg, #0a3cff, #00c6ff);
            padding: 25px;
            text-align: center;
        }

        header h1 {
            margin: 0;
            color: white;
        }

        section {
            padding: 30px;
            max-width: 1000px;
            margin: auto;
        }

        h2 {
            color: #58a6ff;
            border-bottom: 1px solid #30363d;
            padding-bottom: 5px;
        }

        .qa {
            background-color: #161b22;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
        }

        .question {
            font-weight: bold;
            color: #79c0ff;
        }

        .answer {
            margin-top: 10px;
            line-height: 1.6;
        }

        pre {
            background-color: #010409;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            color: #c9d1d9;
        }

        code {
            color: #58a6ff;
        }

        .project-link {
            background-color: #161b22;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        a {
            color: #00c6ff;
            text-decoration: none;
            font-weight: bold;
        }

        a:hover {
            text-decoration: underline;
        }

        footer {
            text-align: center;
            padding: 15px;
            color: #8b949e;
            font-size: 14px;
        }
    </style>
</head>
<body>

<header>
    <h1>Supriya Sharma</h1>
    <p>Java Developer | Backend | Problem Solving</p>
</header>

<section>
    <h2>Java – Interview Q&A</h2>

    <div class="qa">
        <div class="question">
            Q1. What is Encapsulation in Java?
        </div>
        <div class="answer">
            Encapsulation is the process of wrapping data and methods together and hiding
            the internal state of an object using <code>private</code> variables and public getters/setters.
        </div>

        <pre><code>
class Employee {
    private int salary;

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public int getSalary() {
        return salary;
    }
}
        </code></pre>
    </div>

    <div class="qa">
        <div class="question">
            Q2. What is Inheritance in Java?
        </div>
        <div class="answer">
            Inheritance allows a child class to acquire properties and behavior of a parent class
            using the <code>extends</code> keyword.
        </div>

        <pre><code>
class Parent {
    void show() {
        System.out.println("Parent class");
    }
}

class Child extends Parent {
    void display() {
        System.out.println("Child class");
    }
}
        </code></pre>
    </div>
</section>

<section>
    <h2>Live Project</h2>

    <div class="project-link">
        <p>UPHAAR – AI Powered Gift Recommendation System</p>
        <a href="https://uphaar-511843972336.us-central1.run.app/home" target="_blank">
            🔗 Open Live Project
        </a>
    </div>
</section>

<footer>
    © 2026 Supriya Sharma | Java & Backend Projects
</footer>

</body>
</html>
