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
Residual \; sum \; of \; square \; RSS = e_{1}^{2}
```
