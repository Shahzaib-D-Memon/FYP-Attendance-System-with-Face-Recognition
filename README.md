# Attendance System with Face Recognition

## Project Overview

This project, undertaken by 18CS101 (Me), 18CS35, and 18CS15 under the guidance of Supervisor Engr. Arbab Ali Samejo, aims to revolutionize attendance monitoring in educational institutions. Leveraging facial recognition technology, the system enhances accuracy and efficiency in attendance management.

## Abstract

The primary objective of this project is to develop a facial recognition-based attendance monitoring system for educational institutions. The current attendance system is outdated, leading to inaccuracies and inefficiencies. The proposed solution employs deep learning to enhance facial recognition performance, turning video frames into photos for quick and accurate identification. Face databases are established to feed data into the recognizer algorithm, allowing real-time attendance updates. The system records recognized individuals' attendance, generating an Excel file accessible to faculty at the end of each day.

## Project Description

The Attendance System with Face Recognition combines elements of cyber security, data science, and computer engineering to provide a robust solution for attendance tracking. The utilization of deep learning algorithms enhances facial recognition performance, ensuring quick and accurate identification.

## Prerequisites

Before you begin with the project, ensure you have the following installed on your system:

1. [Visual Studio Community](https://visualstudio.microsoft.com/downloads/)
2. [Anaconda](https://www.anaconda.com/)

## Project Setup

Follow the steps below to set up and execute the project:

1. **Create Anaconda Environment:**
   - Open Anaconda prompt from the Windows search.
   - Run the command: `conda create -n FYP pip`
   - Respond with "yes" to all prompts.

2. **Activate Environment:**
   - Type `conda activate FYP` to activate the environment.

3. **Install Required Libraries:**
   - Run: `conda install -c conda-forge dlib` to install the Dlib library.
   - Navigate to the project directory using Anaconda prompt: `cd <path to project directory>`
   - Run: `pip install -r requirements.txt` to install project-specific requirements.
   - Run: `pip install pygame` to install the Pygame library.

## Running the Project

To run the project:

1. Open Anaconda prompt.
2. Activate the environment: `conda activate FYP`
3. Navigate to the project directory.
4. Run the Python script: `python menu.py`

A main menu will appear with the following options:

- **Start:** Initiates face recognition to mark attendance.
- **Register Face:** Opens the camera to register a face by pressing the "space" key.

To close the program, press `CTRL+C`.

## Contributors

- 18CS101
- 18CS35
- 18CS15

## Supervisor

Engr. Arbab Ali Samejo

Feel free to explore and enhance the functionality of the Attendance System with Face Recognition. If you encounter any issues, please refer to the troubleshooting section or contact the contributors. Thank you for using our system!
