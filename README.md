# Atoms repeatedly traversing a cavity
## Quantistic simulation of a Cavity QED System and Trapping States 

**Informatics Tools Exam** - **Student:** Cecilia Bertolini - **Date:** September 2026

This project analyses the time evolution of a magnetic field inside an optical cavity initially in the vacuum state ($\vert 0 \rangle$), interacting with a sequence of two level atoms prepared in the excited state ($\vert e \rangle$). The system is described by the **Jaynes-Cummings model** at resonance.
Cavity leakage ($\kappa = 0$) and spontaneous decay of the atom ($\gamma = 0$) are assumed to be negligible. The product of the interaction time $T_{\text{int}}$ and the coupling $g$ can be varied from run to run. You will be asked for this value by the terminal at the beginning of every run.

## Requirements
* Python 3.x installed on your computer.

## How to use
1. Clone this repository.
```bash
git clone https://github.com/ceciliabertolinii/IT-Exam.git
```
2. Enter the project folder, create and activate a virtual environment.
```bash
cd IT-Exam
python -m venv venv
source venv/bin/activate
```
3. Install required libraries.
```bash
 pip install -r requirements.txt
 ```
4. To run the python script, execute the command:
 ```bash
 python3 prob_distribution.py
 ```
5. To run the notebook, execute the command:
```bash
 jupyter notebook
 ```
then open the file .ipynb and run all the cells. 
   
