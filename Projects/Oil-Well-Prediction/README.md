# OilyGiant Oil Well Development Project

This project applies machine learning and statistical analysis to determine the most profitable region for developing new oil wells.  
It was completed as part of a data science program and demonstrates skills in predictive modeling, financial analysis, and risk evaluation.

---

## Table of Contents
- [About](#about)
- [Dataset](#dataset)
- [Technologies](#technologies)
- [Features](#features)
- [Getting Started](#getting-started)
- [Results](#results)
- [Contact](#contact)

---

## About
OilyGiant, an oil company, needs to decide where to open a new drilling site.  
The project uses data from three regions, trains machine learning models to predict well reserves, and applies profit and risk calculations to recommend the optimal location.

---

## Dataset
Each dataset (`geo_data_0.csv`, `geo_data_1.csv`, `geo_data_2.csv`) contains:  
- **id**: Unique well identifier  
- **f0, f1, f2**: Geological features  
- **product**: Predicted reserves (thousand barrels)  

*The data is synthetic and provided for educational purposes.*

---

## Technologies
- Python 3.x  
- Pandas, NumPy  
- Scikit-learn (Linear Regression, train/test split, metrics)  
- Matplotlib / Seaborn (visualizations)  
- Jupyter Notebook  

---

## Features
- Data preprocessing and exploration of three oil regions  
- Linear regression modeling to predict oil reserves  
- Profit calculation under fixed budget and well selection rules  
- Bootstrapping (1,000 iterations) to estimate confidence intervals and risk of losses  
- Final recommendation of the best region to maximize profit with <2.5% risk of losses  

---

## Getting Started

**Clone the repository**  
          or
**Install the required dependencies:**

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
