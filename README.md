# Fenway-Forecast

## About
The **Fenway-Forecast** project is a **machine learning implementation focused on predicting Boston Housing Prices** [1, 2]. It showcases an end-to-end development and deployment workflow utilizing modern tools and practices, including Docker and GitHub Actions [1, 2].

## Live Demo
A live version of this project is deployed and accessible online at:
**[fenway-forecast.onrender.com](https://fenway-forecast.onrender.com/)** [2, 3]

## Key Features & Technologies
This project integrates several key technologies to demonstrate a robust machine learning application:
*   **Machine Learning Development**: The core machine learning model development and data preprocessing are primarily conducted within **Jupyter Notebook** (`Main.ipynb`) [2, 3]. The project also includes pre-trained model (`RegrModel.pkl`) and scaling artifacts (`scaling.pkl`) [3].
*   **Containerization**: The application is containerized using **Docker**, as indicated by the presence of a `Dockerfile` [1-3].
*   **Automation & CI/CD**: **GitHub Actions** are leveraged to automate workflows, which likely include continuous integration and continuous deployment processes, managed within the `.github/workflows` directory [1-3].
*   **Python Application**: The project includes a Python application (`app.py`) with its dependencies listed in `requirements.txt` [3].
*   **Deployment Configuration**: A `Procfile` is included, which typically defines how the application should be run on a platform like Render [3].

## Project Structure
The repository is organized with the following key files and directories [3]:
*   `.github/workflows/`: Contains configuration files for GitHub Actions.
*   `templates/`: Likely holds HTML templates for the web interface.
*   `BostonHousing.csv`: The dataset used for training the Boston housing price prediction model.
*   `Dockerfile`: Defines the environment and steps to build the Docker image for the application.
*   `LICENSE`: Specifies the project's licensing terms.
*   `Main.ipynb`: The main Jupyter Notebook where the machine learning model development is documented.
*   `Procfile`: A configuration file used by deployment platforms to specify the command to run the application.
*   `README.md`: This file, providing an overview of the project.
*   `RegrModel.pkl`: A serialized (pickled) file containing the trained regression model.
*   `app.py`: The Python script for the web application interface.
*   `requirements.txt`: Lists all Python package dependencies required for the project.
*   `scaling.pkl`: A serialized (pickled) file containing the data scaler used for preprocessing.

## Project Status
As of the available information, the "Fenway-Forecast" repository has:
*   **0 stars** [1-3]
*   **0 forks** [1-3]
*   **1 watcher** [2]
*   A history of **23 commits** [3]

## License
This project is open-source and distributed under the **CC0-1.0 License** [2, 3].
