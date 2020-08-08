---
layout: post
title: "Bắt đầu với Java cơ bản (phần 1)"
menutitle: "Bắt đầu với Java cơ bản (phần 1)"
date: 2020-08-08 08:25:00 +0000
tags: Java
category: Java Tutorial
author: am
published: true
redirect_from: "/2020-08-08-bat-dau-voi-java-p1/"
language: VN
comments: true
---

## Contents
{:.no_toc}

* Đây là mục lục.
{:toc}

# Học nhanh Java cơ bản (P1)

## Giới thiệu

Trong bài viết này chúng ta sẽ được tiếp cận nhanh Java, cách trình bày của tôi là cực kỳ ngắn gọn. Nếu bạn là một người mới bắt đầu với Java, bạn không chỉ nên đọc mà còn phải thực hành để kiểm chứng những gì trong tài liệu này liệu có xác thực.

----------
# Tìm hiểu nhanh Java

## Java là gì ?**

**Java**  là một  **một ngôn ngữ lập trình hiện đại, bậc cao, hướng đối tượng, bảo mật và mạnh mẽ.**  và là một  **Platform**.

**Platform:**  Bất cứ môi trường phần cứng hoặc phần mềm nào mà trong đó có một chương trình chạy, thì được hiểu như là một Platform. Với môi trường runtime riêng cho mình (JRE) và API, Java được gọi là Platform.

Ngôn ngữ lập trình Java ban đầu được phát triển bởi  **Sun Microsystems**  do  **James Gosling**  khởi xướng và phát hành vào năm 1995. Phiên bản mới nhất của Java Standard Edition là Java SE 8. Với sự tiến bộ của Java và sự phổ biến rộng rãi của nó, nhiều cấu hình đã được xây dựng để phù hợp với nhiều loại nền tảng khác nhau. Ví dụ: J2EE cho các ứng dụng doanh nghiệp, J2ME cho các ứng dụng di động.

Các phiên bản J2 mới đã được đổi tên thành Java SE, Java EE và Java ME. Phương châm của Java là **"Write Once, Run Anywhere"** - viết một lần chạy nhiều nơi, nghĩa là bạn chỉ cần viết một lần trên window chẳng hạn, sau đó vẫn chương trình đó bạn có thể chạy trên Linux, Android, các thiết bị J2ME...

----------

## Các tính năng của Java

Ngôn ngữ lập trình Java có các tính năng sau:

-   **Hướng đối tượng**  - Trong Java, mọi thứ đều là một Object. Java có thể dễ dàng mở rộng và bảo trì vì nó được xây dựng dựa trên mô hình Object.
-   **Nền tảng độc lập**  - Không giống nhiều ngôn ngữ lập trình khác bao gồm cả C và C ++, khi Java được biên dịch, nó không được biên dịch thành ngôn ngữ máy nền tảng cụ thể, thay vào mã byte - nền tảng độc lập. Mã byte này được thông dịch bởi máy ảo (JVM) trên nền tảng nào đó mà nó đang chạy.
-   **Đơn giản**  - Java được thiết kế để dễ học. Nếu bạn hiểu khái niệm cơ bản về OOP Java, sẽ rất dễ để trở thành master về java.
-   **Bảo mật**  - Với tính năng an toàn của Java, nó cho phép phát triển các hệ thống không có virut, giả mạo. Các kỹ thuật xác thực dựa trên mã hoá khóa công khai.
-   **Kiến trúc - trung lập**  - Trình biên dịch Java tạo ra định dạng tệp đối tượng kiến trúc trung lập, làm cho mã biên dịch được thực thi trên nhiều bộ vi xử lý, với sự hiện diện của hệ điều hành Java.
-   **Portable**  - Là kiến trúc tập trung và không có khía cạnh thực hiện phụ thuộc của đặc tả này làm cho Java khả chuyển. Trình biên dịch trong Java được viết bằng ANSI C, đó là một tập con POSIX.
-   **Mạnh mẽ**  - Java làm nỗ lực để loại trừ các tình huống dễ bị lỗi bằng cách kiểm tra lỗi tại thời gian biên dịch và kiểm tra lỗi tại runtime.
-   **Đa luồng**  - Với tính năng đa luồng của Java có thể viết các chương trình có thể thực hiện nhiều tác vụ đồng thời. Tính năng thiết kế này cho phép các nhà phát triển xây dựng các ứng dụng tương tác có thể chạy trơn tru hơn.
-   **Thông dịch**  - Mã byte Java được dịch trực tiếp tới các máy tính gốc và không được lưu trữ ở bất cứ đâu.
-   **Hiệu năng cao**  - Với việc sử dụng trình biên dịch Just-In-Time, Java cho phép thực hiện hiệu năng cao.
-   **Phân tán**  - Java được thiết kế cho môi trường phân tán của Internet.
-   **Năng động**  - Java là năng động hơn C hoặc C++ vì nó được thiết kế để thích nghi với môi trường đang phát triển. Các chương trình Java có thể mang một lượng lớn thông tin tại runtime mà có thể được sử dụng để xác minh và giải quyết các truy cập vào các đối tượng tại runtime.

----------

## Java dùng để làm gì ?

Java rất phổ biến và đã thống trị lĩnh vực này từ đầu những năm **2000** đến nay **2020**.
Theo tập đoàn SUN, hiện nay có khoảng 3 tỷ thiết bị đang chạy Java giữa dịch Covid19.

Java đã được sử dụng trong các lĩnh vực khác nhau. Ví dụ:

1.  **Desktop App** như Acrobat Reader, Media Player, Antivirus, ...
2.  **Web App** như irctc.co.in, javatpoint.com, ...
3.  **Enterprise App** như các ứng dụng về xử lý nghiệp vụ ngân hàng, ...
4.  Thiết bị **Mobile** như các ứng dụng **Android**.
5.  Hệ thống **nhúng**
6.  **Robot**
7.  **Game App**
8. ...**etc**...

----------

## Các kiểu của Java App

Có 4 kiểu ứng dụng chính của Java App:

### 1. Standalone App

Standalone App cũng được biết đến như Desktop App hoặc Window-based App. Để tạo ra ứng dụng kiểu này người ta thường sử dụng AWT, Swing hoặc JavaFX framework.

### 2. Web App

Web App là ứng dụng chạy trên server và tạo được các trang động. Hiện nay, servlet, jsp, struts, jsf, spring... là những công nghệ được sử dụng để tạo Web App trong java.

### 3. Enterprise App

Một ứng dụng dạng như Banking App, có lợi thế là tính bảo mật cao, cân bằng tải (load balancing) và clustering. Trong java, EJB được sử dụng để tạo các Enterprise App.

### 4. Mobile App

Mobile App là ứng dụng được tạo ra cho các thiết bị di động. Hiện nay Android và Java ME được sử dụng để chạy các ứng dụng này.

----------

## Java Platforms

Có 4 nền tảng Java:

### 1. Java SE (Java Standard Edition)

Java SE là một nền tảng lập trình Java. Nó bao gồm các API lập trình Java như java.lang, java.io, java.net, java.util, java.sql, java.math, v.v. Nó bao gồm các chủ đề cốt lỗi như OOPs, String, Regex, Exception, Inner classes, Multithreading, I/O Stream, Networking, AWT, Swing, Reflection, Collection, v.v.

### 2. Java EE (Java Enterprise Edition)

Đây là một nền tảng doanh nghiệp chủ yếu được sử dụng để phát triển các ứng dụng web và doanh nghiệp. Nó được xây dựng trên nền tảng Java SE. Nó bao gồm các chủ đề như Servlet, JSP, Web Services, EJB, JPA , v.v.

### 3. Java ME (Java Micro Edition)

Đây là một nền tảng vi mô chủ yếu được sử dụng để phát triển các ứng dụng di động.

### 4. JavaFX

JavaFX là một nền tảng phần mềm phát triển các ứng dụng Internet phong phú (Rich Internet Applications – RIAs) có thể chạy trên nhiều loại thiết bị, nhiều hệ điều hành khác nhau. JavaFX là một giải pháp công nghệ cho GUI trên nền tảng Java nhằm tạo giao diện đồ họa người dùng dựa trên Swing và Java2D.

----------

## Cài đặt và cấu hình JDK

### #JDK là gì ?

**JDK** (viết tắt của **Java Development Kit**) là một **tập hợp những công cụ phần mềm** được phát triển bởi Sun Microsystems dành cho các nhà phát triển phần mềm bằng Java.

JDK là một trong ba gói công nghệ cốt lỗi khi lập trình **Java** hay lập trình **Android**. Ba gói công nghệ đó bao gồm:

 - **JVM**: Máy ảo Java – Java Virtual Machine.
 - **JRE**: Java Runtime Environment – Môi trường Java Runtime.
 - **JDK** – Đang đề cập trong bài viết này.

JDK cho phép lập trình viên xây dựng ứng dụng Java. Các ứng dụng có thể được JVM và JRE xử lý và chạy.

Nhiều bạn mới đầu hay nhầm lẫn giữa JDK với JRE. JDK là gói các công cụ phát triển phần mềm, còn JRE là gói công cụ để chạy phần mềm mà bạn tạo bằng JDK.

### #Chi tiết cách cài đặt JDK trên Window

Trước tiên, chúng ta cần tải JDK về máy tính của mình, các bạn có thể tải JDK  [tại đây](http://www.oracle.com/technetwork/java/javase/downloads/index.html). Mình sẽ hướng dẫn cài đặt JDK cho các bạn chi tiết từng bước một.

Sau đây là hướng dẫn chi tiết cách tải và cài đặt JDK cho Window:

Khi click vào đường link bên trên, danh mục JDK sẽ hiển thị như hình bên dưới:

![tải JDK mới nhất](https://vntalking.com/wp-content/uploads/2018/01/tai-jdk-moi-nhat.png)

Click chọn “JDK Download”

Sau khi chọn “JDK Download”, bạn sẽ được chuyển đến trang chọn phiên bản JDK phù hợp với hệ điều hành bạn đang sử dụng.

![tải JDK cho window](https://vntalking.com/wp-content/uploads/2018/01/tai-jdk-cho-window.png)

Danh sách link tải JDK cho tất cả OS

Bạn chọn phiên bản Window x64 Installer (đây là phiên bản JDK cho Window 64bit). Kết thúc quá trình download, bạn sẽ được file cài đặt JDK như bên dưới.

![download jdk](https://vntalking.com/wp-content/uploads/2018/02/4-1024x527.png)

Để cài đặt, bạn click đúp chuột vào tệp exe bắt đầu cài JDK.

![download jdk](https://vntalking.com/wp-content/uploads/2018/02/5.png)

Nhấn next để tiếp tục.

![cài đặt jdk](https://vntalking.com/wp-content/uploads/2018/02/6.png)

Bạn có thể thay đổi đường dẫn cài đặt jdk -> Nhấn next để tiếp tục cài đặt mặc định

![cài đặt jdk](https://vntalking.com/wp-content/uploads/2018/02/7.png)

Nhấn  **Close**  để hoàn tất -> tiếp bước cài đặt biết môi trường.

### #Cài đặt biến môi trường JAVA

Đây chính là phần mà nhiều bạn gặp khó khăn nhất. Mình sẽ cố gắng hướng dẫn chi tiết nhất có thể để ai cũng thực hiện thành công.

![cài đặt biến môi trường](https://vntalking.com/wp-content/uploads/2018/02/8.png)

Ở ngoài màn hình Desktop, các bạn nhấp phải chuột vào Computer, chọn Properties.

![](https://vntalking.com/wp-content/uploads/2018/02/9-1024x539.png)

![](https://vntalking.com/wp-content/uploads/2018/02/10.png)

Làm theo hướng dẫn trong hình.

![cài đặt biến môi trường](https://vntalking.com/wp-content/uploads/2018/02/111.png)

Nhấn new

![cài đặt biến môi trường](https://vntalking.com/wp-content/uploads/2018/02/121.png)

Trong trường hợp các bạn không thấy đường link, các bạn có thể chọn  **Browse Directory…** để lấy đường link tới Java.

![cài đặt biến môi trường](https://vntalking.com/wp-content/uploads/2018/02/13.png)

![cài đặt biến môi trường](https://vntalking.com/wp-content/uploads/2018/02/14.png)

Click chọn theo hướng dẫn.

![cài đặt biến môi trường](https://vntalking.com/wp-content/uploads/2018/02/15.png)

Nhấn OK để hoàn tất việc cài đặt.

### #Kiểm tra thiết lập biến môi trường cho JAVA

![cài đặt biến môi trường java](https://vntalking.com/wp-content/uploads/2018/02/16-1024x575.png)

Ở cửa sổ làm việc **CMD**, chúng ta nhập vào các câu lệnh kiểm tra:

-   **java -version** : dùng để kiểm tra phiên bản java chúng ta đã cài đặt
-   **javac -version** : dùng để kiểm tra phiên bản javac (nếu hiển thị phiên bản của javac ở đây thì bạn đã cài đặt thành công biến môi trường java)

![cài đặt](https://vntalking.com/wp-content/uploads/2018/02/17.png)

### #Cài đặt Java trên Ubuntu

Việc cài đặt java trên Linux nói chúng rất đơn giản, bạn chỉ cần gõ lệnh theo đúng trình tự sau là xong.

Bài viết này mình sẽ hướng dẫn cài đặt JDK trên Ubuntu, các phiên bản Linux khác làm tương tự.

Đầu tiên, bạn thêm PPA  repository:

    $ sudo add-apt-repository ppa:webupd8team/java

Sau đó gõ lệnh cài đặt java với phiên bản bạn mong muốn.

    $ sudo apt-get install oracle-java8-installer

Bạn có thể thay java8 thành thành  `java6`  hoặc  `java7`  nếu bạn muốn.

Sau khi cài đặt xong, bạn kiểm tra xem đã thành công rồi hay chưa bằng lệnh xem version:

    $ java -version

Nếu kết quả hiện ra như thế này thì đã thành công:

    Java version "1.8.0_111"
    Java(TM) SE Runtime Environment  (build 1.8.0_111-b14)
    Java HotSpot(TM)  64-Bit Server VM  (build 25.111-b14, mixed mode)

Cuối cùng, bạn thêm biến môi trường JAVA_HOME bằng 2 lệnh sau:

    $ export JAVA_HOME="/usr/lib/jvm/java-8-oracle"
    $ export PATH=$JAVA_HOME/bin:$PATH

Có vẻ đơn giản hơn so với Window ấy nhỉ!

## #Tạm kết

Rồi có vẻ hơi dài, hẹn gặp các bạn ở phần 2 của bài viết. Ở phần thứ 2 chúng ta sẽ bắt đầu đến với việc vật lộn với code Java, [phần 2](https://minhphongvn.github.io/blog/java%20tutorial/bat-dau-voi-java-p2).