# JamieLiu_Mini9

## Colab Link

## Demo Link

[Demo Link](https://youtu.be/CilIVwqyJcU)

## Overview

This repo contains work for Data Engineering class, individual project 1. This project practices continuous integration in data science. I use the airline safety dataset and generates descriptive statistics and visualizations.

## Project Structure

```
JAMIELIU_INDIV_PROJ1/
├── .devcontainer/
│ ├── devcontainer.json
│ └── Dockerfile
├── .github/
│ └── workflows/
│ ├── format.yml
│ ├── install.yml
│ ├── lint.yml
│ └── test.yml
├── mylib/
│ ├── **init**.py
│ └── lib.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── main.ipynb
├── main.py
├── Makefile
├── repeat.sh
├── report.md
├── requirements.txt
├── setup.sh
├── test_lib.py
├── test_main.py
```

## Features

- `.devcontainer` configuration for a consistent Python development environment using Docker.
- **Makefile** to streamline common tasks like setup, testing, linting.
- **GitHub Actions** for automated CI/CD pipeline (testing, linting, and deployment).
- `requirements.txt` for managing Python dependencies.

## Usage

1. **Clone the repository:**

   ```bash
   git clone git@github.com:nogibjj/JamieLiu_Mini9.git
   ```

2. **Install dependencies:**

   ```bash
   make install
   ```

3. **Format code:**

   ```bash
   make format
   ```

   ![Alt text](format.png)

4. **Lint code:**

   ```bash
   make lint
   ```

   ![Alt text](lint.png)

5. **Test code:**

   ```bash
   make test
   ```

   ![Alt text](test.png)

6. **Run all steps (Install, Format, Lint, Test):**

   ```bash
   make all
   ```

## **Summary Statistics**:

![Alt text](statistics.png)

## **Example Visualization**:

### Incidents 00-14

![Incidents 00-14](incidents_00_14.png)

![Incidents 00-14](Frequency_incidents_00_14_hist.png)

See detailed statistics and visualizations in this [report](/report.md)
