# Joke Generator Web App

## Overview

This project is a dynamic web application built using the FastHTML framework—a new Python-based tool for creating modern, efficient web applications. The goal of this project is to exhaustively explore and discover all parts of FastHTML, testing its capabilities and features to fully understand its potential and limitations.

## Features

- **Dynamic Joke Generation:** Get jokes tailored to your chosen categories.
- **Responsive Layout:** Adapts to various screen sizes for optimal user experience..
- **Interactive UI:** Utilizes Pico CSS for a modern design for a lively user experience.

## Technologies Used

- **FastHTML:** For building the web application's structure.
- **Pico CSS:** For efficient styling.
- **Custom CSS:** Additional styling for unique design elements.
- **Asyncio:** To handle asynchronous tasks for joke generation.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hajjarali736/joke-generator-app.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd joke-generator-app
   ```
3. **Install dependencies:**
   ```bash
   pip install python-fasthtml
   ```

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```
2. **Open your browser and go to `http://localhost:5001` (by default) to use the app.**

## API Integration and FastHTML

### API Integration

The Joke Generator Web App integrates with a backend API to handle joke requests and category management. Here’s how the API is utilized:

- **Category Management:** Users can select or deselect joke categories through the interface. The application sends these updates to the server using POST requests, which are processed to update the list of active categories.
  ```python
  @app.post("/add/{categorie}")
  def add_cat(categorie: str):
      global categories
      # Update categories based on user input
      if categorie in categories:
          categories.remove(categorie)
      else:
          if "any" in categories:
              categories.remove("any")
          categories.append(categorie)
      if len(categories) == 0:
          categories = ["any"]
      print(categories)
Joke Generation: When a user requests a joke, the application sends a POST request to the API endpoint. The server processes this request asynchronously, retrieves a joke from the joke generator, and returns the joke data to be displayed.
   ```python
   @app.post("/generate")
   def generate():
       global categories, first_line, second_line
       joke = asyncio.run(list_joke(categories))
       joke_card()
       first_line = joke[0]
       second_line = joke[1]
       return Div(
           Div(
               Ul(
                   ft.Li(
                       f"{first_line}",
                       id="first_line",
                       cls="joke-text",
                   ),
                   ft.Li(f"{second_line}", id="joke-text", cls="joke-text"),
               ),
               id="joke-card",
               cls="joke-card",
           ),
           cls="centered-container",
       )
   ```

How FastHTML Helped
FastHTML played a crucial role in the development of this application by simplifying HTML structure creation and enhancing code maintainability. Here’s how FastHTML contributed:

Simplified HTML Structure: FastHTML allows for a more Pythonic approach to defining HTML structures. This makes it easier to manage and generate complex HTML layouts directly from Python code.

```python
Copy code
def nav_bar():
return Header(
Nav(
   A(
       Img(
           src="/assets/k.svg", alt="Joke generator", width="105", height="24"
       ),
       href="/",
   ),
   A("About the Developer", href="/about", cls="about_home"),
   cls="bar",
),
cls="nav",
)
```
Dynamic Content Rendering: FastHTML’s integration with asynchronous functions facilitates dynamic content updates without the need for traditional page reloads. This results in a more responsive user experience.

```python
Copy code
def generate():
joke = asyncio.run(list_joke(categories))
return Div(
Div(
   Ul(
       ft.Li(f"{first_line}", id="first_line", cls="joke-text"),
       ft.Li(f"{second_line}", id="joke-text", cls="joke-text"),
   ),
   id="joke-card",
   cls="joke-card",
),
cls="centered-container",
)
```

Modular Components: FastHTML’s ability to create modular components like Div, Header, and Nav allows for easy composition and reuse of HTML elements. This modularity helps in maintaining a clean and organized codebase.

By leveraging FastHTML, the development process became more streamlined, making it easier to build and maintain the web app’s structure and dynamic functionalities.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## How LLM (Large Language Models) Helped

Leveraging Large Language Models (LLMs) significantly accelerated the development process. Here’s how:

### Prompt Engineering for Code Generation

To enhance the app’s functionality and streamline development, specific prompts were used with LLMs. Examples include:

- **Prompt for Generating Code Snippets:**
```plaintext
"Generate a Python function to create a joke card in FastHTML with dynamic content."
```
This prompt helped generate the code for the `joke_card` function, streamlining the development of the joke display component.

## How LLMs Helped

In developing this web app, targeted prompts to an LLM like GPT-4 were crucial for refining and enhancing the code. Here's how LLMs contributed:

- **Prompt for Debugging and Optimization:**
    ```plaintext
    "How can I optimize the joke generation function in FastHTML for better performance?"
    ```
    This prompt provided insights into optimizing asynchronous tasks and improving overall performance.

- **Prompt for Styling Recommendations:**
    ```plaintext
    "Suggest some modern CSS styling techniques for a floating effect on containers."
    ```
    This helped in refining the UI with a floating effect, enhancing the visual appeal.

Although GPT-4 did not learn fast-HTML directly, it was highly effective when given the right prompts. One method involved providing snapshots of already written code and asking the LLM to add specific features like CSS styling, `href` attributes, and HTMX integration. This approach ensured that the output was aligned with the project requirements and enhanced the application’s functionality and design.

By using these targeted prompts, the LLMs offered valuable assistance in generating code, optimizing performance, and improving the application's design.
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
