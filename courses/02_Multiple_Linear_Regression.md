# Multiple Linear Regression
Pratikte çoğu zaman birden fazla girdi değişkenimiz vardır. Birden fazla girdi değişkeni ile kurulan lineer regresyon modeline multiple lineer regresyon denir.
# Her Girdi Değişkeni için Ayrı ayrı Basit Lineer Regresyon Modelleri kurmak yerine niye 1 adet Çoklu Lineer Regresyon?
* Bütün girdi değişkenleri göz önüne alındığında tek bir çıktı değişkeni tahmininin nasıl yapılacağı açık değildir
* Her bir basit lineer regresyon modeli tahmin yaparken diğer girdi değişkenlerini göz ardı eder.
* Çok yanıltıcı sonuçlar elde edebilir.

Bunlardan dolayı tek bir çoklu lineer regresyon modeli iyi bir yaklaşımdır.

p farklı girdi değişkenimizin hepsinin bir eğim katsayısı vardır. Formül şu şekildedir;

```math
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ....... + \beta_p X_p + \epsilon
```
Burada $X_j$ j. girdi değişkenini temsil eder. $\beta_j$, diğer tüm girdi değişkenleri sabit tuttuğumuzda, $X_j$ deki 1 birimlik artışın Y üzerindeki ortalama etkisi olarak yorumlanır.
## Estimating the Regression Coefficients
Burada $\beta_0$ , $\beta_1$ ,...., $\beta_p$ bilinmiyor ve tahmin edilmek isteniyor. Katsayılar için tahminlerde şu şekilde ifade edilir,
```math
\hat{y} = \hat{\beta_0} + \hat{\beta_1} x_1 + \hat{\beta_2} x_2 + ....... + \hat{\beta_p} x_p
```
Parametreler, basit doğrusal regresyon bağlamında gördüğümüz aynı en küçük kareler yaklaşımı kullanılarak tahmin edilmektedir.$\beta_0$ , $\beta_1$ ,...., $\beta_p$'yiresidual sum of squares (RSS)'yi en küçük yapacak şekilde seçilir.
```math
RSS = \sum_{i=1}^{n} (y_i - \hat{y_i})^2
```
 Term | Coefficient | Std. error | t-statistic | p-value 
--- | --- | --- | --- |--- 
Intercept | 2.939 | 0.3119 | 9.42 | <0.0001 
TV | 0.046 | 0.0014 | 32.81 | <0.0001 
radio | 0.189 | 0.0086 | 21.89 | <0.0001 
newspaper | -0.001 | 0.0059 | -0.18 | 0.8599 

* TV katsayısı, gazete ve radyo sabit tutulurken TV harcamalarının 1000$ artmasıyla ilişkili ürün satışlarındaki (çıktı değişkeni) ortalama artışı temsil etmektedir. 

## Is There a Relationship Between the Response and Predictors?

p değişkenli çoklu doğrusal regresyon ortamında, tüm değişkenlerin çıktı değişkeni ile ilişkili olup olmadığını sormamız gereklidir. Bunun için hipotez testi kullanıyoruz. Hipotezler aşağıdaki gibidir.

$H_0: \beta_1 = \beta_2 = ..... = \beta_p = 0$


$H_a$ : at least one $\beta_j$ is non-zero

Hipotez testinin F istatistiği aşağıdaki gibi hesaplanır.
```math
F = \frac{(TSS - RSS) / p}{RSS/ (n - p - 1)}
```

Bu örnekte F istatistiği 570'dir. Bu 1'den çok büyüktür bu yüzden $H_0$'ı reddederiz ve bir ilişkinin olduğunu söyleyebiliriz. Girdi değişkenlerinden en az birinin çıktı değişkeni ile ilişkilidir.

Bu çalışma p'nin n'den küçük olduğu durumlarda işe yarar

## Deciding on Important Variables




