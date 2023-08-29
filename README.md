# Lesson Planning with AOI

This project aims to provide educators with tools to efficiently create lesson plans, generate quizzes, and interact with curriculum content through a chat interface.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Creating Lesson Plans](#creating-lesson-plans)
  - [Generating Quizzes](#generating-quizzes)
  - [Using the Chat Interface](#using-the-chat-interface)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Lesson Planning with AOI is a project that aims to streamline the process of creating educational materials and interacting with curriculum content. This repository provides tools and resources that empower educators to design effective lesson plans, generate quizzes from the curriculum, and facilitate learning through a chat-based interface.

## Features

- **Lesson Planning:** Leverage the provided content to design comprehensive and engaging lesson plans tailored to your students' needs.

- **Quiz Generation:** Automatically generate quizzes based on the curriculum content, helping you assess students' understanding effectively.

- **Chat Interface:** Interact with the curriculum content using a chat-based interface, allowing students to ask questions and engage with the material interactively.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites:

- [Python](https://www.python.org/) (version 3.X)
- [Node.js](https://nodejs.org/) (version 18)
- [Database System] (e.g., MySQL, MongoDB)

### Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/BethanyJep/Lesson-Planning-with-AOI.git
   cd Lesson-Planning-with-AOI
 ```
--- 
2. Setup Backend
 
```sh
cd backend
pip install -r requirements.txt
# Configure database and API settings in config.py
python manage.py migrate
python manage.py runserver
```
---

3. Setup the Frontend
```sh
  cd frontend
  npm install
  # Configure API endpoint in src/config.js
  npm start
```

## Usage

### Creating Lesson Plans

1. Log in to the system.
2. Navigate to the "Lesson Plans" section.
3. Use the provided curriculum content to design your lesson plan.

### Generating Quizzes

1. Access the "Quiz Generator" tool.
2. Select the curriculum topics for the quiz.
3. Customize quiz parameters (e.g., number of questions, difficulty).
4. Generate the quiz and review/edit if necessary.

### Using the Chat Interface

1. Open the chat interface from the "Chat" section.
2. Select the curriculum module or topic you want to interact with.
3. Engage in a dynamic chat-based learning experience.

## Contributing

We welcome contributions from the community! To contribute to this project:

1. Fork the repository.
2. Create a new branch.
3. Make your enhancements or fixes.
4. Submit a pull request explaining your changes.

## License

This project is licensed under the [MIT License](LICENSE).
```
