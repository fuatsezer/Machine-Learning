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

![111](https://github.com/fuatsezer/Machine-Learning/assets/63423939/4075b958-5645-4bca-bb36-44b78a039b39)


Yukarıdaki tabloda $\hat{\beta_{0}}$ = 6.97 ve $\hat{\beta_{1}}$ = 0.055 dir. Bu da şunu ifade eder;
* Girdi değişkenindeki her 1000 birimlik artış çıktı değişkeninin tahmininde 55'lik bir artışa sebep olur.
* Girdi değişkeni 0 değerini aldığında çıktı değişkeni için tahminimiz ortalama 6.97 birimdir.

![111](https://github.com/fuatsezer/Machine-Learning/assets/63423939/aafce224-2a33-42ee-9d0f-7cbb2f36dd2c)

## Katsayı Tahminlerinin Doğruluğunu Test Etme

Eğer f doğrusal bir fonksiyonla yaklaşık olarak hesaplanacaksa, bu ilişki şu şekilde yazılabilir.
 ```math
  Y = \beta_{0} + \beta_{1} X + \epsilon
```
