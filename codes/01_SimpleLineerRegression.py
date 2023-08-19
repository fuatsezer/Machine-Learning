import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from sklearn.metrics import mean_squared_error
from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.stats.diagnostic import het_breuschpagan
from matplotlib.colors import ListedColormap
import numpy as np
matplotlib.use("Qt5Agg")
df = pd.read_csv("./datasets/Advertising.csv")
df.head()
input_parameter = "TV"
output_parameter = "sales"

X = df[[input_parameter]]
y = df[[output_parameter]]

class SimpleLinearRegression():
    def __init__(self,dataframe,input_parameter, output_parameter):

        self.dataframe = dataframe
        self.input_parameter = input_parameter
        self.output_parameter = output_parameter

    def fit(self):
        df = self.dataframe
        X = df[[self.input_parameter]]
        y = df[[self.output_parameter]]
        lr = LinearRegression()
        model = lr.fit(X, y)


        g = sns.regplot(x=df[input_parameter], y=df[output_parameter], scatter_kws={'color': 'r', 's': 9})
        g.set_title(
            f"Model Function: {output_parameter} = {round(float(model.intercept_[0]), 2)}+ {round(float(model.coef_[0]), 2)}*{input_parameter}",
            fontsize=20, fontweight='bold')
        g.set_ylabel(f"{output_parameter}", fontsize=20)
        g.set_xlabel(f"{input_parameter}", fontsize=20);

        y_pred = model.predict(X)
        residual = (y - y_pred)
        print(f"""
            1) For each 1 unit increase in  {input_parameter} variable there will be an average increase in {output_parameter} variable is {round(float(model.coef_[0]), 2)} units.
            2) When {input_parameter} variable is 0 then  {output_parameter} variable will on average is {round(float(model.intercept_[0]), 2)} units.
            3) Residual sum of squares (RSS) = {round((residual**2).sum()[0],2)}
        
        """)
        return residual



    def beta_validation(self):
        df = self.dataframe
        X = df[[self.input_parameter]]
        y = df[[self.output_parameter]]
        X = sm.add_constant(X)
        lr = LinearRegression()
        model = lr.fit(X, y)
        lm = sm.OLS(y, X)
        model_sm = lm.fit()
        beta_ttest_pvalue = round(model_sm.pvalues, 3)
        beta_se_value = round(model_sm.bse, 3)
        beta_tvalue = round(model_sm.tvalues, 3)
        beta_conf_int_values = round(model_sm.conf_int(), 3)
        print(model.coef_[0])
        beta_coef = pd.Series([round(float(model.intercept_[0]), 3), round(float(model.coef_[0][1]), 3)],
                              index=["const", "TV"])

        beta_valid_df = pd.concat([beta_coef, beta_se_value, beta_conf_int_values, beta_tvalue, beta_ttest_pvalue],
                                  axis=1)
        beta_valid_df.columns = ["Coef", "SE.", "CI [0.025]", "CI [0.975]", "T Value", "P Value"]

        print(f"""
         Comment1.) When {input_parameter} variable is 0 then  {output_parameter} variable will on average fall somewhere between {beta_valid_df["CI [0.025]"][0]} and {beta_valid_df["CI [0.975]"][0]} with 95% probability
         Comment2.) For each 1 unit increase in  {input_parameter} variable, there will be an average increase in {output_parameter} variable of  between {beta_valid_df["CI [0.025]"][1]} and {beta_valid_df["CI [0.975]"][1]} units with 95% probability""")
        if beta_valid_df["P Value"][0] > 0.05:
            print("         Comment3.) Beta_0 = 0. According to T Test")
        else:
            print("         Comment3.) Beta_0 != 0. According to T Test")
        if beta_valid_df["P Value"][1] > 0.05:
            print("         Comment4.) Beta_1 = 0. According to T Test")
        else:
            print("         Comment4.) Beta_1 != 0. According to T Test")

    def model_validation(self):
        df = self.dataframe
        X = df[[self.input_parameter]]
        y = df[[self.output_parameter]]
        X = sm.add_constant(X)
        lr = LinearRegression()
        model = lr.fit(X, y)
        y_pred = model.predict(X)
        lm = sm.OLS(y, X)
        model_sm = lm.fit()
        mse = mean_squared_error(y, y_pred)
        rse = round(np.sqrt(mse), 2)
        mean_y = round(y.mean()[0], 2)
        percentage_error = round(rse / mean_y * 100, 2)
        print(
            f"RSE (residual standard error): {rse}, \nMean of {output_parameter}: {mean_y}, \nPercentage Error: {percentage_error}%")
        ### 2.) f-Statistics
        if model_sm.f_pvalue > 0.05:
            print("Comment1.) All Beta Coeff. = 0. According to f Test")
        else:
            print("Comment1.) At least one of Beta Coeff. not equal to 0. According to f Test")

        ### 3.) R^2
        r2 = round(model_sm.rsquared, 2)
        print(
            f"R^2: {r2} so, {r2}% of variability in {output_parameter} is explained by a lineer regression on {input_parameter}")

slr = SimpleLinearRegression(df,input_parameter,output_parameter)
resid = slr.fit()
slr.beta_validation()
slr.model_validation()