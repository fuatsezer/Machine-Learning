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


