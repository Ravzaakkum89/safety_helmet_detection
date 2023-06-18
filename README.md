# Safety Helmet Detection Projesi

Bu proje, gerçek zamanlı olarak baret tespiti gerçekleştiren bir uygulamayı içerir. Bu uygulama, bir video akışını analiz eder ve baret takılı olan kişileri tespit ederek ekranda çerçeve içinde gösterir. Ayrıca tespit oranını ve ilgili etiketi gösterir. Eğer kafasında baret olmayan bir kişi tespit edilirse, uygulama çerçeve içinde başlık yazısıyla birlikte kişinin kafasını gösterir ve aynı zamanda bir sesli uyarıyla tehlike olduğunu bildirir.

## Screenshots

| ![confusion_matrix](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/confusion_matrix.png?raw=true)   | ![labels](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/labels.jpg?raw=true)           | ![F1_curve](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/F1_curve.png?raw=true)           | ![P_curve](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/P_curve.png?raw=true)          |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| ![PR_curve](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/PR_curve.png?raw=true)           | ![R_curve](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/R_curve.png?raw=true)          | ![results](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/results.png?raw=true)            | ![train_batch0](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/train_batch0.jpg?raw=true)     |
| ![train_batch1](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/train_batch1.jpg?raw=true)       | ![train_batch2](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/train_batch2.jpg?raw=true)    | ![val_batch0_labels](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/val_batch0_labels.jpg?raw=true) | ![val_batch0_pred](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/val_batch0_pred.jpg?raw=true) |
| ![val_batch1_labels](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/val_batch1_labels.jpg?raw=true) | ![val_batch1_pred](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/val_batch1_pred.jpg?raw=true) | ![val_batch2_labels](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/val_batch2_labels.jpg?raw=true) | ![val_batch2_pred](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/val_batch2_pred.jpg?raw=true) |

## Proje Açıklaması

Bu proje, baret tespiti yapmak için [Kaggle](https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection)'dan temin edilen bir veri kümesi kullanılarak geliştirilmiştir. Veri kümesinde "helmet", "head" ve "person" olmak üzere üç etiket kullanılmıştır. [Kaggle](https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection)'dan alınan veri kümesi, elde edilen veri kümesiyle birleştirilerek kullanılmıştır. Daha sonra Roboflow kullanılarak xml formatındaki etiket dosyaları txt formatına dönüştürülmüştür, çünkü bu formatta etiket dosyaları YOLOv5 ile uyumlu olması gerekmektedir. Uygun veri kümesi, Google Colab üzerinde YOLOv5 kullanılarak eğitilmiş ve elde edilen sonuçlar export edilmiştir. Son olarak, Python'da yazılan tespit kodu PyQt5 kullanılarak geliştirilen bir arayüze entegre edilmiştir.

## Kurulum

Aşağıdaki adımları izleyerek projeyi yerel makinenizde çalıştırabilirsiniz:

- Bu depoyu yerel makinenize klonlayın:

```bash
  git clone https://github.com/haticesaike/safety_helmet_detection.git
```

- Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:

```bash
  pip install -r requirements.txt

```

- Proje klasöründe, Python dosyasını çalıştırın:

```bash
  python main.py

```

## Kullanım

- Uygulamayı başlattığınızda, bir video akışı penceresi açılacaktır.

- Video akışında görüntülenen kişilerin başlarında baret takılıysa, uygulama bunları tespit edecek ve ekranda çerçeve içinde gösterecektir.

- Eğer kafasında baret olmayan bir kişi tespit edilirse, uygulama çerçeve içinde kişinin kafasını gösterecek ve bir sesli uyarı ile tehlike olduğunu bildirecektir.

- Uygulamayı kapatmak için pencereyi kapatmanız yeterlidir.

## Arayüz

| ![App Screenshot 1](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/ss1.png?raw=true) | ![App Screenshot 2](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/ss2.png?raw=true) | ![App Screenshot 3](https://github.com/haticesaike/safety_helmet_detection/raw/master/images/ss3.png?raw=true) |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
