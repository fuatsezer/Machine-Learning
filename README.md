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
#### Show Missingness Statistics
```python
  # show non-null count of every columns
  college.info()
  # or
  import missingno
  missingno.bar(college)
```
```python
  # show  amaount of missing values for every columns
  college.isnull().sum()
```
```python
  # show  percentage of missingness for every columns
  college.isnull().mean() * 100
```
#### Nullity Matrix
```python
  msno.matrix(college)
```
<img src="https://camo.githubusercontent.com/3cd5f7b2a0576e30d855caaf5ebf51e7c4af338c5cb68ef2a63951e041d8cd53/687474703a2f2f692e696d6775722e636f6d2f714c367a4e516a2e706e67" width="75%" height="75%">

#### Fine tuning the matrix

```python
  msno.matrix(college.loc["May-1976":"July-1976"],freq="M")
```

<img src="https://camo.githubusercontent.com/af8f61b4bdbe6267d766333993daaf7ff554d1affdd57fe2797a238cddd41edc/68747470733a2f2f692e696d6775722e636f6d2f564c76577073562e706e67" width="75%" height="75%">

### Is Data missing at Random?
#### Type of missingness 
1. Missing Completely at Random (MCAR)
2. Missing at Random (MAR)
3. Missing Not at Random (MNAR)

#### Missing Completeletly at Random (MCAR)
> Missingness has no relationship between any values, observed or missing
#### Missing at Random (MAR)
> There is a systematic relationship between missingness and other observed data, but not the missing data
#### Missing not a Random (MNAR)
> There is a relationship between missingness and its values, missing or non-missing.

# MNAR - An example
* Missingness pattern of the `diabetes` sorted by `Serum_Insulin`

```python
  sorted = diabetes.sort_values("Serum_Insulin")
  msno.matrix(sorted)
```

### Finding patterns in missing data
#### Finding correlations between missingness
* Missingness heatmap or correlation map
#### Missingness Heatmap
* Graph of correlation of missing values between columns
* Explans the dependencies of missingness between columns.

```python
  msno.heatmap(college)
```

<img src="https://miro.medium.com/max/1400/1*otOG9Vgs1wckfKZzJ-f_8g.png" width="75%" height="75%">

#### Missingness Dendogram
* Tree diagram of missingness
* Describes correlation of variables by grouping them

```python
  msno.dendrogram(college)
```
<img src="https://camo.githubusercontent.com/71e3000e568686bafd60d4a54101da60b8577f373fe124cc8baad4bfef4d4b21/68747470733a2f2f692e696d6775722e636f6d2f6f4969523463742e706e67" width="75%" height="75%">

### When and how to delete missing data
#### Types of deletions
1. Pairwise deletion
2. Listwise deletion

Note: Used when the values are MCAR

### Imputation Techniques
#### Basic Imputation Techniques
#### Mean Imputation

```python
  from sklearn.impute import SimpleImputer
  mean_imputer = SimpleImputer(strategy="mean")
  diabetes.iloc[:,:] = mean_imputer.fit_transform(diabetes)
```

#### Median Imputation

```python
  from sklearn.impute import SimpleImputer
  median_imputer = SimpleImputer(strategy="median")
  diabetes.iloc[:,:] = median_imputer.fit_transform(diabetes)
```


#### Mode Imputation

```python
  from sklearn.impute import SimpleImputer
  mode_imputer = SimpleImputer(strategy="most_frequent")
  diabetes.iloc[:,:] = mode_imputer.fit_transform(diabetes)
```

#### Imputing a constant

```python
  from sklearn.impute import SimpleImputer
  constant_imputer = SimpleImputer(strategy="constant", fill_value=0)
  diabetes.iloc[:,:] = constant_imputer.fit_transform(diabetes)
```
### Time Series Imputation
#### Forward and Backward Imputation

```python
  airquality.fillna(method="ffill",inplace=True) # forward fill
  airquality.fillna(method="bfill",inplace=True) # backward fill
```
#### Imputing with Interpolation
* The `.interpolate()` method extends the sequence of values to the missing values
* The attribute method in `.interpolate()` can be set to
  * `'linear'` 
  * `'quadratic'`
  * `'nearest'`


```python
  airquality.interpolate(method="linear",inplace=True) # linear
  airquality.interpolate(method="quadratic",inplace=True) # quadratic
  airquality.interpolate(method="nearest",inplace=True) # nearest
```

### Advanced Imputation Techniques

#### K-Nearest Neighbor (KNN) Imputation
* Select K nearest or similar data points using all the non-missing features
* Take average of the selected data points to fill in the missing feature

<img src="https://machinelearningknowledge.ai/wp-content/uploads/2018/08/KNN-Classification.gif" width="75%" height="75%">


```python
  from fancyimpute import KNN
  knn_imputer = KNN()
  diabetes_knn = diabetes.copy(deep=True)
  diabetes_knn.iloc[:,:] = knn_imputer.fit_transform(diabetes_knn)
```
#### Multiple Imputations by Chained Equations (MICE)
* Perform multiple regressions over random sample of the data
* Take average of the multiple regression values
* Impute the missing feature value for the data point

```python
  from fancyimpute import IterativeImputer
  MICE_imputer = IterativeImputer()
  diabetes_MICE = diabetes.copy(deep=True)
  diabetes_MICE.iloc[:,:] = MICE_imputer.fit_transform(diabetes_MICE)
```

### Imputing Categorical Values

<img src="https://womaneng.com/wp-content/uploads/2018/09/onehotencoding.jpg" width="75%" height="75%">

#### Imputing with KNN


```python
  users_KNN_imputed = users.copy(deep=True)
  # Create MICE imputer
  KNN_imputer = KNN()
  users_KNN_imputed.iloc[:,:] = np.round(KNN_imputer.fit_transform(imputed))
  
  for col in imputed:
    reshaped_col = imputed[col].values.reshape(-1, 1)
    users_KNN_imputed[col] = ordinal_enc[col].inverse_transform(reshaped_col)
```







