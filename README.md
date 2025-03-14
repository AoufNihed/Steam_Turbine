# Steam Turbine Calculator

## Description

This Streamlit application calculates the performance of a steam turbine based on either the **Rankine** or **Carnot** cycle. It utilizes the `pyXSteam` library to determine thermodynamic properties and provides key performance metrics such as thermal efficiency, turbine work, and pump work. Additionally, the app generates a **T-S diagram** using Plotly for visualization.

## Features

- **Supports Rankine and Carnot Cycles**
- **User input for pressure values**
- **Calculation of key parameters**: temperature, entropy, enthalpy, efficiency, turbine work, and pump work
- **Interactive T-S diagram visualization**
- **Export results to CSV**

## Installation

### Prerequisites

Ensure you have Python installed on your system.

### Install Required Packages

Run the following command to install dependencies:

```bash
pip install streamlit plotly pyXSteam pandas
```
## Usage

To run the application, use the following command:
```bash
streamlit run app.py
```
## User Inputs

1.Cycle Type: Select between Carnot and Rankine cycles.

2.High Pressure (bar): Input a value between 10 and 300 bar.

3.Low Pressure (bar): Input a value between 0.03 and 0.5 bar.

4.Click Calculate to compute results and display the T-S diagram.

5.Option to Download CSV of results.

## Output

1.Table of thermodynamic properties

2.T-S diagram plot

3.Downloadable CSV report

# Developed by Nihed Aouf
