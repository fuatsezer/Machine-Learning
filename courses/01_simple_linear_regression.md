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

```math
RSE = \sqrt{\frac{RSS}{(n - 2}}
```

Güven aralıklarını hesaplamak için standart hatalar kullanılabilir. %95 güven aralığı, %95 olasılıkla , aralığın  parametrenin gerçek bilinmeyen değeri içereceğini söyler. $\beta_{1}$ ve $\bta_{0}$ için güven aralığı:

```math
$\hat{\beta_{1}}$ \pm 2. SE(\hat{\beta_{1}})
```
```math
$\hat{\beta_{0}}$ \pm 2. SE(\hat{\beta_{0}})
```





