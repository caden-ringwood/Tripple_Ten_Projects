# Gold Recovery Prediction

This project analyzes industrial ore processing data and applies machine learning to **predict gold recovery efficiency**.  
It was completed as part of a data science portfolio and demonstrates skills in data exploration, feature engineering, and predictive modeling.

## Project Structure

gold-recovery-prediction/
│
├── data/ # Datasets
│ ├── gold_train.csv
│ ├── gold_test.csv
│ └── gold_full.csv
│
├── notebooks/
│ └── gold-recovery-prediction.ipynb # Main notebook
│
├── reports/ # Reports and visuals
│ ├── figures/ # Plots & visualizations
│ └── final-report.pdf # (Optional) Project summary
│
├── src/ # Python scripts (optional modularization)
│ ├── data_preprocessing.py
│ └── model_training.py
│
├── .gitignore
├── README.md
└── requirements.txt


## Project Overview

The task is to build a model that predicts the amount of gold recovered from ore after different stages of processing.  
This prediction helps **optimize efficiency in gold extraction** and reduce losses in production.

### Objectives
1. **Data Analysis (EDA)**  
   - Explore training and test datasets  
   - Clean and validate features  
   - Visualize processing metrics  

2. **Model Development**  
   - Prepare features and targets  
   - Train multiple ML models  
   - Evaluate using metrics such as RMSE / MAE  

3. **Prediction & Insights**  
   - Select the best-performing model  
   - Generate predictions on unseen data  
   - Provide recommendations for optimization  

## Technologies Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

## Notebook

- [Gold Recovery Prediction Notebook](notebooks/gold-recovery-prediction.ipynb)  

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/gold-recovery-prediction.git
   cd gold-recovery-prediction

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt

3. Open the Notebook:
    ```bash
    jupyter notebook notebooks/gold-recovery-prediction.ipynb
## Auther
**Caden Ringwood**
- [LinkedIn](www.linkedin.com/in/caden-ringwood)
