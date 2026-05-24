# Reproducing the Data Pipeline

## 1. Clone the Repository

```bash
git clone https://github.com/bemnetne/Insurance-Risk-Analytics-Predictive-Modeling.git
cd Insurance-Risk-Analytics-Predictive-Modeling/
```

---

## 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Initialize DVC

```bash
dvc init
```

---

## 5. Pull the Data from DVC Remote Storage

```bash
dvc pull
```

This retrieves all tracked dataset versions, including the raw and cleaned datasets.

---

## 6. Run the EDA Notebook

```bash
jupyter notebook
```

Then open and run:

```text
notebooks/eda.ipynb
```

The notebook performs:
- data loading
- preprocessing
- missing value handling
- exploratory data analysis (EDA)
- visualization generation

---


## 7. Track New Dataset Versions (Optional)

```bash
dvc add data/processed/cleaned_insurance_data.csv

git add .

git commit -m "Update processed dataset"

dvc push
```

This stores the updated dataset version in DVC remote storage.