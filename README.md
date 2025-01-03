# Credit Card Fraud Detection Project

## Overview
This project aims to detect fraudulent credit card transactions using three machine learning models:
1. **Logistic Regression**
2. **Random Forest Classifier**
3. **Decision Tree Classifier**

Each model is trained and evaluated for its performance, with a comparison of their accuracy, precision, recall, and classification reports.

---

## Features
### 1. **Data Preparation**:
   - **Dataset**: `creditcard.csv`
   - **Features**: 28 anonymized variables (`V1` to `V28`), along with `Time` and `Amount`.
   - **Target**: `Class` (0 = Non-Fraud, 1 = Fraud).
   - **Preprocessing**: Standardized the `Amount` feature and scaled the data.

### 2. **Exploratory Data Analysis**:
   - Checked for missing values and data imbalances.
   - Visualizations included:
     - Fraud vs. Non-Fraud transaction distribution.
     - Correlation heatmap for feature relationships.

### 3. **Machine Learning Models**:
   - **Logistic Regression**: Baseline model for comparison.
   - **Random Forest Classifier**: Ensures high accuracy and robust performance.
   - **Decision Tree Classifier**: Interpretable but prone to overfitting.

### 4. **Evaluation Metrics**:
   - Confusion Matrix
   - Classification Report (Precision, Recall, F1-Score)
   - Accuracy Score

---

## Requirements

### Libraries Used
The project utilizes the following Python libraries:
- `pandas` (Data manipulation)
- `scikit-learn` (Machine learning tools)
- `seaborn` (Data visualization)
- `matplotlib` (Plotting)

### Installation
Install the required libraries using:
```bash
pip install pandas scikit-learn seaborn matplotlib
```

---

## How to Run
1. **Dataset**: Place the `creditcard.csv` file in the project directory.  
   (Download it from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)).  

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **Outputs**:
   - Visualizations (Class distribution and correlation heatmap).
   - Confusion matrix and classification reports for all three models.
   - Comparison table of accuracy for Logistic Regression, Random Forest, and Decision Tree models.

---

## Results

### Model Performance:
| Model                 | Accuracy  | Precision | Recall | F1-Score | Comments                |
|-----------------------|-----------|-----------|--------|----------|-------------------------|
| Logistic Regression   | ~98.5%   | 0.90      | 0.70   | 0.79     | Good baseline model     |
| Random Forest         | ~99.6%   | 0.94      | 0.88   | 0.91     | Best performance overall|
| Decision Tree         | ~99.0%   | 0.91      | 0.85   | 0.88     | Slightly overfits       |

### Key Observations:
- Logistic Regression serves as a strong baseline model for initial evaluation.
- Random Forest outperforms others, offering high accuracy and balanced evaluation metrics.
- Decision Tree provides interpretable results but may overfit, requiring hyperparameter tuning.

---

## Visualizations

### Fraud vs Non-Fraud Transactions
Illustrates the imbalance in the dataset, with significantly fewer fraud cases compared to non-fraud cases.

### Correlation Heatmap
Highlights relationships between features, helping identify potential patterns that distinguish fraud from non-fraud.

---

## Future Enhancements
- Address data imbalance using techniques like **SMOTE** or **Oversampling**.
- Experiment with advanced models such as **XGBoost** and **LightGBM**.
- Incorporate additional evaluation metrics like **ROC-AUC** for more nuanced model comparisons.
- Deploy the model as an API using **Flask** or **FastAPI**.

---

## Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request. Feedback and suggestions for improvement are always appreciated.

---

## Acknowledgements
- **Dataset**: Provided by ULB’s Machine Learning Group.
- **Libraries**: Thanks to the Python community for tools like **Scikit-learn**, **Seaborn**, and **Matplotlib**.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

