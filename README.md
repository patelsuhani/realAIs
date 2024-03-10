# [2024 Health Hackathon: *RealAIs*](https://github.com/patelsuhani/realAIs)

### Contribution: [Suhani Patel](https://github.com/patelsuhani/), [Rishi Shah](https://github.com/rishis123/), [Saanvi Mehra](https://github.com/saanvimehra), [Chimdi Ejiogu](https://github.com/cejiogu/), [Dwight Koyner](https://github.com/dwightkoyner/)

## Introduction
RealAIs is an application designed to aid in the early diagnosis of congenital disorders in children aged from just born to 5 years old. It empowers parents and healthcare providers by providing them with a tool to screen for potential health concerns in their children, enabling timely intervention and support.

## Description
RealAIs allows parents to input detailed information about their child, including age, gender, race, ethnicity, behavioral patterns, and completion of expected milestones. By capturing images of the child's front and side profile views and running them through machine learning algorithms, the app calculates the likelihood of the child having specific congenital disorders.

## Features
User Authentication: Parents can create an account and log in securely.
Input Patient Information: Parents can input detailed information about their child, including demographics and behavioral patterns.
Image Capture: Parents are prompted to take pictures of their child's front and side profile views.
Screening Tests: RealAIs conducts screening tests for congenital disorders, including Down syndrome, Cleft lip, and Fetal Alcohol Syndrome.
ML Algorithm: Our app utilizes machine learning algorithms trained on images of children aged 0 to 5 years old with Down syndrome. The ML model compares the provided images to the dataset to calculate the likelihood of the child having a particular disorder.
Results Display: Results are displayed separately for each individual disease, indicating whether the child has a high or low chance of developing the disorder.
Resource Provision: Parents are provided with help resources, relevant information, and contact details of nearby hospitals, doctors, or geneticists.

## Development
Frontend Development: We used JavaScript in React Native to build the front end of the RealAIs app. React Native allowed us to develop a cross-platform application with a native-like user experience. We followed component-based architecture and utilized Redux for state management to maintain a clear and organized codebase.

Machine Learning Integration: Google Cloud ML was chosen for training and deploying our machine learning models. We collected a dataset of images of children aged 0 to 5 years old with and without congenital disorders, focusing on Down syndrome, Cleft lip, and Fetal Alcohol Syndrome. We used Vertex AI for model development and training, focusing on facial phenotypes associated with each disorder.

Image Processing: Image processing techniques were implemented to preprocess and analyze the images captured by users. This involved tasks such as facial feature detection and measurement extraction to extract relevant data for the machine learning models.

Backend Services: Backend services were developed to handle user authentication, data storage, and communication with the machine learning models. We used serverless architecture with Google Cloud Functions for scalability and cost-effectiveness.

API Integration: Integration with external APIs was implemented to provide resources, information, and contact details for further assistance to parents. This involved communication with healthcare providers, hospitals, and support organizations.

## Technology Stack
Frontend: JavaScript in React Native
Machine Learning: Google Cloud ML

## How to Use

## Installation
Clone the repository: 'git clone https://github.com/patelsuhani/realAIs.git'
Navigate to the project directory: 'cd realAIs'
Install dependencies: 'npm install'
Start the application: 'npm start'

## Feedback

## License
This project is licensed under the MIT License.
