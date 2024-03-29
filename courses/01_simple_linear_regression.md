# Simple Linear Regression
Tek bir girdi değişkenini çıktı değişkenini tahmin etmek için kullandığımız bir yaklaşımdır. Girdi ve değişkeni arasında yaklaşık doğrusal bir ilişki olduğunu varsayar. Matematiksel olarak şu şekilde yazılabilir.
 ```math
  Y \approx \beta_{0} + \beta_{1} X
```
$\beta_{0}$ ve $\beta_{1}$ lineer modelde kesişim ve eğim terimlerini temsil eden iki bilinmeyen sabittir, bunlar model katsayıları veya parametreleri olarak adlandırılır.
$\beta_{0}$ ve $\beta_{1}$ tahmin etmek için eğitim verileri kullanılır. Bu katsayıları ve girdi değişkenini kullanarak çıktı değişkeni için tahminde bulunuruz.
```math
\hat{y} =  \hat{\beta_{0}} + \hat{\beta_{1}} x
```
$\hat{y}$, X=x iken Y'nin tahminini gösterir.Burada bilinmeyen bir parametre ve katsayı için tahmin edilen değeri belirtmek için şapka ( $\hat{}$ ) sembolü kullanılır.

Kod tarafında içersine veri setini, girdi ve çıktı değişkeninin özniteliğini alan bir sınıf oluşturuyoruz:

```python
class SimpleLinearRegression():
    def __init__(self,dataframe,input_parameter, output_parameter):

        self.dataframe = dataframe
        self.input_parameter = input_parameter
        self.output_parameter = output_parameter
```

## Estimating the Coefficient
Pratikte $\beta_{0}$ ve $\beta_{1}$ bilinmiyor, dolayısıyla tahminlerde bulunmadan önce katsayıları tahmin etmek için verileri kullanmalıyız. Amacımız en küçük kareler kriterini minimum yapacak katsayıları katsayıları bulmaktır.

```math
ith \; residual \; e_{i} = y_{i} - \hat{y_{i}}
```

```math
Residual \; sum \; of \; square \; RSS = e_{1}^2 + e_{2}^2 + ........ + e_{i}^2
```




![svg](https://github.com/fuatsezer/Machine-Learning/assets/63423939/9f5e7663-a1ba-4642-b414-9dbe9c775c0f)

![svg](https://github.com/fuatsezer/Machine-Learning/assets/63423939/0d9a6297-708b-4976-82f8-b336e371f829)

Kod tarafında SimpleLinearRegression sınıfımıza fit fonksiyonunu ekliyoruz ve bize katsayılar için yorumları regplotu ,artıkları (residuals) ve RSS değerini döndürüyor.

```python
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
```
![111](https://github.com/fuatsezer/Machine-Learning/assets/63423939/fc90a848-efac-4a5b-8eba-4e6eb1521794)


![ε (1)](https://github.com/fuatsezer/Machine-Learning/assets/63423939/68005f31-46a2-4502-84ca-a40f08d74628)


Yukarıdaki grafikte $\hat{\beta_{0}}$ = 7.03 ve $\hat{\beta_{1}}$ = 0.05 dir. Bu da şunu ifade eder;
* Girdi değişkenindeki her 1000 birimlik artış çıktı değişkeninin tahmininde 50'lik bir artışa sebep olur.
* Girdi değişkeni 0 değerini aldığında çıktı değişkeni için tahminimiz ortalama 6.97 birimdir.



## Katsayı Tahminlerinin Doğruluğunu Test Etme

Eğer f doğrusal bir fonksiyonla yaklaşık olarak hesaplanacaksa, bu ilişki şu şekilde yazılabilir.
 ```math
  Y = \beta_{0} + \beta_{1} X + \epsilon
```
* Burada $\beta_{0}$ intercept termdür, yani X=0 iken Y'nin beklenen değeridir.
* $\beta_{1}$ eğimdir, X'teki 1 birimlik artış ile Y'deki ortalama artıştır.
* Genellikle $\epsilon$'nin x'ten bağımsız olduğunu varsayarız. $\epsilon$ ortalaması sıfır olan bir normal dağılımdan türetilmiştir.

Katsayıların tahmininin doğruluğunu incelemek için katsayıların standart hatalarına, %95 güven aralıklarına ve katsayıların sıfıra eşitliğinin kontrol edildiği hipotez testine bakabiliriz. 

$\beta_{0}$ ve $\beta_{1}$'in standart hataları aşağıdaki formüllerle hesaplanır.

![svg](https://github.com/fuatsezer/Machine-Learning/assets/63423939/8d65e788-87ff-47aa-b365-19942b7b3832)

![svg](https://github.com/fuatsezer/Machine-Learning/assets/63423939/2758509f-bb8d-450d-8091-e4055e16c625)<?xml version='1.0' encoding='UTF-8'?>

$\sigma^2 = Var(\epsilon)$

Bu formüllerin geçerli olabilmesi için her gözlem için artıkların ($\epsilon_i$) varyanslarının sabit ve uncorrelated olması lazım (otokorelasyon).



Güven aralıklarını hesaplamak için standart hatalar kullanılabilir. %95 güven aralığı, %95 olasılıkla , aralığın  parametrenin gerçek bilinmeyen değeri içereceğini söyler. $\beta_{1}$ ve $\beta_{0}$ için güven aralığı:

```math
\hat{\beta_{1}} \pm 2. SE(\hat{\beta_{1}})
```
```math
\hat{\beta_{0}} \pm 2. SE(\hat{\beta_{0}})
```

$\beta_{0}$'ın güven aralığı [6.130,7.935] ve $\beta_1$ 'in [0.042, 0.053] olsun.
* Bu durumda X = 0 durumunda çıktı değişkeni ortalama olarak 6.130 ile 7.935 arasında bir değer alacağı sonucuna varırız.
* Ayrıca X teki her 1000 birimlik artış y de ortalama 42ile 53 birimlik bir artış olacaktır.

Standart hatalar, katsayılar üzerinde hipotez testi yapmak içinde kullanılır
* $H_0$: There is no relationship between X and Y ($\beta_1$ = 0)
* $H_a$: There is some relationship between X and Y ($\beta_1$ $\neq$ 0)

* Uygulamada bir t istatistiği hesaplarız

![svg](https://github.com/fuatsezer/Machine-Learning/assets/63423939/0026ed2b-92a2-4d64-9e87-0e0e17fd4700)

| Örnek Tablo        | Coefficient           | Std.error  | t-statistic   | p-value
| ------------- |:-------------:| -----:| -----:| -----:|
| intercept      | $\beta_0$ = 7.0325 | 0.4578 | 15.36 | $${\color{red}<0.0001}$$
| X      | $\beta_1$ = 0.0475 | 0.0027 | 17.67 | $${\color{red}<0.0001}$$

Burada p değeri <0.005'den  küçük olduğu için sıfır hipotezini reddediyoruz ve $\beta_1 \neq 0$ ve $\beta_0 \neq 0$ sonucuna varıyoruz.

Kod tarafında SimpleLinearRegression sınıfımıza beta_validation fonksiyonunu ekliyoruz ve bize katsayılar için Tahminlerinin Doğruluğunu Test Etmemiz için yardımcı olur.

```python
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
```
![image](https://github.com/fuatsezer/Machine-Learning/assets/63423939/228e2117-5df3-4567-8a2f-b24c251fda73)



## Modelin Doğruluğunun değerlendirilmesi
$H_0$'ı reddettikten sonra modelin verilere ne ölçüde uyduğunu bilmektir. Bunun içinde 3 metrik kullanırız. RSE (Residual Standard error), $R^2$ İSTATİSTİĞİ VE F-istatistiği
| Örnek Tablo        | Değer | 
| ------------- |:-------------:|
| RSE      | 3.26 |
| $R^2$      | 0.612 | 
| F-statistic    | 312.1 |

## Residual Standard Error
Modelde her gözlem ile ilişkili bir hata terimi olduğunu unutmayın. RSE gerçek yanıt değişkeni değerlerinin gerçek regresyon çizgisinden sapacağı ortalama miktardır. Aşağıdaki formül ile hesaplanır.

```math
RSE = \sqrt{\frac{RSS}{(n - 2}}
```

Örnek tabloda RSE 3.26'dır. Yeni yanıt değişkeni değerleri gerçek regresyon çizgisinden ortalama olarak yaklaşık 3.260 birim sapmıştır. Bu kabul edilebilir bir değer midir? yanıt değişkeninin ortalaması 14000'dir. Ve dolayısıyla **yüzde hatası 3.260/14000= %23 tür.** RSE,modelin verilere uyumsuzluğunun bir ölçüsüdür.

## $R^2 Statistic$

$R^2$ istatistiği alternatif bir uyum ölçüsü sağlar. Bir oran açıklanan varyans oranı şeklini alır ve bu nedenle her zaman 0 ile 1 arasında bir değer alır ve Y ölçeğinden bağımsızdır $R^2$'nin formülü şe şekildedir:

```math
R^2 = \frac{TSS - RSS}{TSS} = 1 - \frac{RSS}{TSS}
```
TSS yanıt değişkenindeki toplam varyansı ölçer ve regresyon gerçekleşmeden önce yanıt değişkenindeki varolan değişkenlik miktarı olarak düşünülebilir. Tersine RSS, regresyon gerçekleştirildikten sonra açıklanmayan değişkenlık miktarını ölçer. Dolayısıyla TSS - RSS regresyon gerçekleştirilerek yanıt değişkenindeki açıklanan değişkenlik miktarını ölçer. **$R^2$, Y'deki X kullanılarak açıklanabilecek değişkenlik miktarını ölçer.1'e yakın bir $R^2$ değeri yanıttaki değişkenliğin büyük bir kısmının regresyon ile açıklandığını gösterir.** Örnek tabloda $R^2$ değeri 0.61'idi ve bu nedenle yanıt değişkenindeki değişkenliğin üçte ikisi X kullanılarak yapılan doğrusal regresyonla açıklanabiliyor. Basit lineer regresyonda $R^2=r^2$ dir.

Kod tarafında SimpleLinearRegression sınıfımıza model_validation fonksiyonunu ekliyoruz ve bize Modelin Doğruluğunu Test Etmemiz için yardımcı olur.
```python
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

```
![image](https://github.com/fuatsezer/Machine-Learning/assets/63423939/f8ca8b06-277b-4cc8-8ad9-a58021b06424)





