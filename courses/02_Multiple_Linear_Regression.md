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

Çoklu regresyon analizindeki ilk adım, F istatistiğini hesaplamak ve ilgili p değerini incelemektir. Bu p-değerine dayanarak girdilerden en az birinin yanıtlailişkili olduğu sonucuna varırsak, bunun hangisi yada hangileri olduğunu bilmeliyiz.Bireysel p değerlerine bakılabilir. Eğer p büyükse bazı yanlış keşifler yapmamız muhtemeldir.

Tüm girdi değişkenleri yanıt değişkeni ile ilişkili olması mümkündür, ancak yanıt değişkeninin yanlızca girdilerin bir alt kümesi ile ilişkili olduğu durum daha sıktır.Yalnızca bu yordayıcıları içeren tek bir modele uymak için hangi yordayıcıların yanıtla ilişkili olduğunu belirleme görevine değişken seçimi denir.

Girdi değişkenlerinin bütün kombinasyonları için model kurarız. Hangi modelin en iyisi olduğunu bilmek için çeşitli istatistikler kullanırız. Bunlar **Mallow's Cp, Akaike bilgi kriteri (AIC), Bayesian bilgi kriteri (BIC) ve adjusted $R^2$** dir. Ayrıca, kalıpları araştırmak amacıyla artıklar gibi çeşitli model çıktılarının grafiğini çizerek hangi modelin en iyi olduğunu da belirleyebiliriz.

Ne yazık ki, p değişkenin alt kümelerini içeren toplam $2^p$ modeli vardır. Bu, orta düzeyde p için bile, yordayıcıların olası her alt kümesini denemenin olanaksız olduğu anlamına gelir.Bunun için farklı seçim yöntemleri deneriz.

### Forward Selection

Sıfır modeliyle başlıyoruz; bu model, bir kesme noktası içeren ancak girdi içermeyen bir modeldir.Daha sonra p adet basit doğrusal regresyonu yerleştiririz ve boş modele en düşük RSS ile sonuçlanan değişkeni ekleriz.Daha sonra bu modele yeni iki değişkenli model için en düşük RSS ile sonuçlanan değişkeni ekliyoruz. Bu yaklaşıma bazı durdurma kuralları sağlanana kadar devam edilir.
### Backward selection
Modeldeki tüm değişkenlerle başlıyoruz ve en büyük p değerine sahip değişkeni, yani istatistiksel açıdan en az anlamlı olan değişkeni atıyoruz.Yeni (p - 1) değişken modeli uygun hale getirilir ve en büyük p değerine sahip değişken çıkarılır. Bu prosedür bir durdurma kuralına ulaşılana kadar devam eder. Örneğin, geri kalan tüm değişkenlerin p değeri belirli bir eşiğin altında olduğunda durabiliriz.
### Mixed selection
Bu backward ve forward selectionların birleşimidir.Modelde hiçbir değişken olmadan başlıyoruz ve ileri seçim seçiminde olduğu gibi en iyi uyumu sağlayan değişkeni ekliyoruz. Değişkenleri tek tek eklemeye devam ediyoruz. Elbette, Reklam örneğinde de belirttiğimiz gibi, modele yeni tahminciler eklendikçe değişkenlerin p değerleri daha da büyüyebilir.Dolayısıyla herhangi bir noktada modeldeki değişkenlerden birinin p değeri belirli bir eşiğin üzerine çıkarsa o değişkeni modelden çıkarırız. Modeldeki tüm değişkenler yeterince düşük bir p değerine sahip olana ve modelin dışındaki tüm değişkenler, modele eklenirse büyük bir p değerine sahip olana kadar bu ileri ve geri adımları gerçekleştirmeye devam ederiz.

## Model Fit





