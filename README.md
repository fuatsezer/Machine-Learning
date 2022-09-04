# Machine Learning
## Dealing with Outlier
### Why deal with Missing Data?
#### Why does missing data exist?
* Values are missed during data acquisition process
* Values deleted accidentally
#### Workflow for treating missing values
1. Convert all missing values to null values
2. Analyze the amount and type of missingness in the data.
3. Appropriately delete or impute missing values.
4. Evaluating & compare the performance of the treated/imputed dataset.
#### Null value Operations
```python
  print(None == None) # True
```
```python
  print(np.nan == np.na) # False
```
```python
  print(np.nan is np.nan) # True
```
```python
  print(np.isnan(np.nan)) # True
```
#### Missing values
* Usually filled with values like `'NA'`, `'-'` or `'.'` etc.

#### Replace missing values
```python
  # if missing data reflect '.'
  college = pd.read_csv('college.csv',na_values='.')
```
```python
  # show non-null count of every columns
  college.info()
  # or
  import missingno
  missingno.bar(college)
```



