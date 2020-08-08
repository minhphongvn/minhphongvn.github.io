---
layout: post
title: "Bắt đầu với Java cơ bản (phần 2)"
menutitle: "Bắt đầu với Java cơ bản (phần 2)"
date: 2020-08-08 08:25:00 +0000
tags: Java
category: Java Tutorial
author: am
published: true
redirect_from: "/2020-08-08-bat-dau-voi-java-p2/"
language: VN
comments: true
---

## Contents
{:.no_toc}

* Đây là mục lục.
{:toc}

# Học nhanh Java cơ bản (P2)

## Giới thiệu

Trong bài viết này chúng ta sẽ được tiếp cận nhanh Java, cách trình bày của tôi là cực kỳ ngắn gọn. Nếu bạn là một người mới bắt đầu với Java, bạn không chỉ nên đọc mà còn phải thực hành để kiểm chứng những gì trong tài liệu này liệu có xác thực.

## Tạo mới Project

Trước hết chúng ta tạo mới một Project, nó sẽ được sử dụng trong hướng dẫn này.

![](https://o7planning.org/vi/10161/images/12343489.png)

Nhập vào tên project:

-   **BasicJavaTutorial**

![](https://o7planning.org/vi/10161/images/12343499.png)

Đây là hình ảnh Project vừa được tạo ra:

![](https://o7planning.org/vi/10161/images/12343507.png)

Chú ý: Để có thể gõ được các ngôn ngữ khác tiếng Anh trong Project, bạn cần chuyển mã hóa sang  **UTF8**.

Nhấn phải chuột vào Project chọn Properties:

![](https://o7planning.org/vi/10161/images/12343521.png)

![](https://o7planning.org/vi/10161/images/12343523.png)

## 3- Các kiểu dữ liệu nguyên thủy (Primitive Data Types)

Có 8 loại dữ liệu nguyên thủy (**primitive data**) trong JAVA:

-   Dùng cho kiểu số nguyên có 4 loại: **byte**, **short**, **int**, **long**
-   Kiểu số thực ta có: **float**, **double**
-   Kiểu ký tự: **char**
-   Kiểu logic (boolean): trả về giá trị **true** hoặc **false** (đúng hoặc sai)

**Kiểu dữ liệu**


| Kiểu dữ liệu | Ghi chú            | Số bit | Giá trị nhỏ nhất                   | Giá trị lớn nhất                    |
|--------------|--------------------|--------|------------------------------------|-------------------------------------|
| byte         | Số tự nhiên 8 bit  | 8      | -128 (-2^7)                        | 127 (2^7-1)                         |
| short        | Số tự nhiên 16 bit | 16     | -32,768 (-2^15)                    | 32,767 (2^15 -1)                    |
| int          | Số tự nhiên 32 bit | 32     | - 2,147,483,648 (-2^31)            | 2,147,483,647 (2^31 -1)             |
| long         | Số tự nhiên 64 bit | 64     | -9,223,372,036,854,775,808 (-2^63) | 9,223,372,036,854,775,807 (2^63 -1) |
| float        | Số thực 32 bit     | 32     | -3.4028235 x 10^38                 | 3.4028235 x 10^38                   |
| double       | Số thực 64 bit     | 64     | -1.7976931348623157 x 10^308       | 1.7976931348623157 x 10^308         |
| boolean      | Kiểu logic         |        | false                              | true                                |
| char         | Kiểu ký tự         | 16     | '\u0000' (0)                       | '\uffff' (65,535).                  |


## 4- Biến (Variable)

Nhấn phải chuột vào src chọn  **"New/Package"**:

![](https://o7planning.org/vi/10161/images/12343558.png)

Đặt tên package là:

-   **org.o7planning.tutorial.javabasic.variable**

![](https://o7planning.org/vi/10161/images/12343568.png)

![](https://o7planning.org/vi/10161/images/12343570.png)

Nhập vào tên class:

-   **VariableExample1**

![](https://o7planning.org/vi/10161/images/12343580.png)

Class  **VariableExample1**  được tạo ra:

![](https://o7planning.org/vi/10161/images/12343588.png)

Sửa code của lớp  **VariableExample1**:

VariableExample1.java

```java
    
    package org.o7planning.tutorial.javabasic.variable;
    
    public class VariableExample1 {
    
    public static void main(String[] args) {
    
        // Khai báo một biến, có kiểu int (Số tự nguyên 32 bit).
        int firstNumber;
        
        // Gán giá trị cho firstNumber
        firstNumber = 10;
        
        System.out.println("First Number =" + firstNumber);
        // Khai báo một biến kiểu float (Số thực 32 bit)
        // Số này được gán giá trị 10.2
        
        // Ký tự 'f' ở cuối giúp java hiểu đây là kiểu float.
        float secondNumber = 10.2f;
        
        System.out.println("Second Number =" + secondNumber);
        
        // Khai báo một số kiểu double (Số thực 64 bit)
        // Số này được gán giá trị 10.2
        // Ký tự 'd' ở cuối giúp java hiểu đây là kiểu double.
        // Phân biệt với kiểu float 'f'.
        double thirdNumber = 10.2d;
        
        System.out.println("Third Number =" + thirdNumber);
        
        // Khai báo một biến kiểu ký tự.
        char ch = 'a';
        System.out.println("Char ch= " + ch);       
        }
    }
```

Chạy class  **VariableExample1**:

Nhấn phải chuột vào class  **VariableExample1** chọn  **"Run As/Java Application"**:

![](https://o7planning.org/vi/10161/images/12343614.png)

Kết quả chạy class xem trên cửa sổ  **Console**:

![](https://o7planning.org/vi/10161/images/12343622.png)

Bạn cũng có thể khai báo nhiều biến cùng một lúc, ví dụ tiếp theo minh họa điều này:

Tạo mới class  **VariableExample2**

![](https://o7planning.org/vi/10161/images/12343636.png)

VariableExample2.java

```java
package org.o7planning.tutorial.javabasic.variable;
 
public class VariableExample2 {
 
    public static void main(String[] args) {
 
        // Khai báo 3 số kiểu long (Số nguyên 64 bit).
        long firstNumber, secondNumber, thirdNumber;
 
        // Gán giá trị cho firstNumber
        // Ký tự 'L' ở cuối để nói với java đây là kiểu long, 
        // phân biệt với kiểu int.
        firstNumber = 100L;
 
        // Gán giá trị cho secondNumber
        secondNumber = 200L;
 
        // Gán giá trị cho thirdNumber.
        thirdNumber = firstNumber + secondNumber;
 
        System.out.println("First Number = " + firstNumber);
        System.out.println("Second Number = " + secondNumber);
        System.out.println("Third Number = " + thirdNumber);
    }
}
```

Kết quả chạy class  **VariableExample2**:

![](https://o7planning.org/vi/10161/images/12343650.png)

## 5- Điều khiển luồng đi của chương trình (Control flow)

### 5.1- Câu lệnh if - else

Cấu trúc của một câu lệnh  **if - else**  là:

```java
if(condition 1)  {
   // Làm gì đó tại đây    
}else if(condition 2) {
   // Làm gì đó tại đây    
}else if(condition 3) {
   // Làm gì đó tại đây    
}
// Ngược lại
else  { 
   // Làm gì đó tại đây    
}
```

Tạo class  **ElseIfExample1**:

![](https://o7planning.org/vi/10161/images/12343682.png)

ElseIfExample1.java

```java
package org.o7planning.tutorial.javabasic.controlflow;
 
public class ElseIfExample1 {
 
    public static void main(String[] args) {
 
        // Khai báo một số kiểu int (Số nguyên 32 bit)
        // Đại diện cho điểm thi (score) của bạn
        int score = 20;
 
        System.out.println("Your score =" + score);
 
        // Nếu điểm số nhỏ hơn 50
        if (score < 50) {
            System.out.println("You are not pass");
        }
        // Ngược lại nếu score lớn hơn hoặc bằng 50 và nhỏ hơn 80.
        else if (score >= 50 && score < 80) {
            System.out.println("You are pass");
        }
        // Trường hợp còn lại (Nghĩa là lớn hơn hoặc bằng 80)
        else {
            System.out.println("You are pass, good student!");
        }
 
    }
}
```

Kết quả chạy class  **ElseIfExample1**:

![](https://o7planning.org/vi/10161/images/12343696.png)

Thay đổi giá trị của biến  **"score"**  trong ví dụ trên và chạy lại class ElseIfExample1:


```java
int score = 20;
```

![](https://o7planning.org/vi/10161/images/12343706.png)

### 5.2- Các toán tử thông thường

```MATLAB
> Lớn hơn
< Nhỏ hơn
>= Lớn hơn hoặc bằng
<= Nhỏ hơn hặc bằng
&& Và
|| hoặc
== So sánh bằng
!= So sánh khác nhau
! Phủ định
```

Tạo class  **ElseIfExample2**

ElseIfExample2.java


```java
package org.o7planning.tutorial.javabasic.controlflow;
 
public class ElseIfExample2 {
 
    public static void main(String[] args) {
 
        // Khai báo một biến kiểu int, đại diện cho tuổi của bạn.
        int age = 20;
 
        // Kiểm tra tuổi nhỏ hơn hoặc bằng 17
        if (age <= 17) {
            System.out.println("You are 17 or younger");
        }
 
        // Kiểm tra tuổi bằng 18
        else if (age == 18) {
            System.out.println("You are 18 year old");
        }
        // Kiểm tra tuổi lớn hơn 18 và nhỏ hơn 40
        else if (age > 18 && age < 40) {
            System.out.println("You are between 19 and 39");
        }
        // Trường hợp còn lại (Lớn hơn hoặc bằng 40)
        else {
            // Một lệnh 'if' lồng bên trong.
            // Kiểm tra tuổi khác 50.
            if (age != 50) {
                System.out.println("You are not 50 year old");
            }
 
            // Lệnh phủ định tuổi bằng 50, nghĩa là khác 50.
            if (!(age == 50)) {
                System.out.println("You are not 50 year old");
            }
 
            // Nếu tuổi là 60 hoặc 70
            if (age == 60 || age == 70) {
                System.out.println("You are 60 or 70 year old");
            }
 
        }
 
    }
}
```

Bạn có thể thay đổi giá trị của "age" và chạy class ElseIfExample2 và xem các kết quả

### 5.3- Giá trị boolean

**boolean**  là một kiểu dữ liệu, nó chỉ có 2 giá trị  **true**  hoặc  **false**  (Đúng hoặc sai).

Tạo class BooleanExample:

![](https://o7planning.org/vi/10161/images/12343756.png)

BooleanExample.java

```java
package org.o7planning.tutorial.javabasic.controlflow;
 
public class BooleanExample {
 
    public static void main(String[] args) {
 
        // Khai báo một biến kiểu boolean
        boolean value = true;
 
        // Nếu value là true
        if (value == true) {
            System.out.println("It's true");
        }
        // Ngược lại
        else {
            System.out.println("It's false");
        }
 
        // Với kiểu boolean, bạn cũng có thể viết
        // With boolean type, you can also write
        if (value) {
            System.out.println("It's true");
        }
        // Ngược lại
        else {
            System.out.println("It's false");
        }
    }
}
```

### 5.4- Câu lệnh switch- case -default

Đây cũng là một loại câu lệnh rẽ nhánh gần giống với  **if-else**  được giới thiệu ở trên

```java
// variable_to_test: Một biến để kiểm tra.
switch ( variable_to_test ) {
  case value1:
   // Làm gì đó tại đây ...
   break;
  case value2:
   // Làm gì đó tại đây ...
   break;
  default:
   // Làm gì đó tại đây ...
}
```

SwitchExample1.java

```java
package org.o7planning.tutorial.javabasic.controlflow;
 
public class SwitchExample1 {
 
    public static void main(String[] args) {
 
        // Khai báo một biến age (tuổi)
        int age = 20;
 
        // Kiểm tra giá trị của age
        switch (age) {
        // Trường hợp tuổi bằng 18
        case 18:
            System.out.println("You are 18 year old");
            break;
        // Trường hợp tuổi bằng 20
        case 20:
            System.out.println("You are 20 year old");
            break;
        // Các trường hợp còn lại
        default:
            System.out.println("You are not 18 or 20 year old");
        }
 
    }
 
}
```

Kết quả việc chạy class  **SwitchExample1**:

![](https://o7planning.org/vi/10161/images/12343794.png)

Chú ý rằng với câu lệnh  **case**  phải là một giá trị cụ thể bạn không thể làm như sau:

```java
// Điều này không được phép!!
case (age < 18) :
 
// case chỉ chấp nhận một giá trị cụ thể, ví dụ:
case 18:
  // Làm gì đó tại đây ..
  break;
```

Xem một ví dụ khác:

SwitchExample2.java

```java
package org.o7planning.tutorial.javabasic.controlflow;
 
public class SwitchExample2 {
 
    public static void main(String[] args) {
 
        // Khai báo một biến age (tuổi)
        int age = 30;
 
        // Kiểm tra giá trị của age.
        switch (age) {
        // Trường hợp tuổi bằng 18
        case 18:
            System.out.println("You are 18 year old");
            break;
        // Các trường hợp 20, 30, 40 tuổi.
        case 20:
        case 30:
        case 40:
            System.out.println("You are " + age);
            break;
        // Các trường hợp còn lại
        default:
            System.out.println("Other age");
        }
 
    }
 
}
```

Kết quả chạy ví dụ:

![](https://o7planning.org/vi/10161/images/12343826.png)

### 5.5- Vòng lặp for

Đây là cấu trúc của vòng lặp:

```java
// start_value: Giá trị bắt đầu
// end_value: Giá trị kết thúc
// increment_number: Giá trị tăng thêm sau mỗi bước lặp.
for ( start_value; end_value; increment_number ) {
   // Làm gì đó tại đây ...
}
```

Hãy xem một ví dụ minh họa:

![](https://o7planning.org/vi/10161/images/12343852.png)

ForLoopExample1.java

```java
package org.o7planning.tutorial.javabasic.loop;
 
public class ForLoopExample1 {
 
    public static void main(String[] args) {
 
        // Khai báo một biến 'step', mô tả bước của vòng lặp (Vòng lặp thứ mấy)
        int step = 1;
 
        // Khai báo một biến 'value' với giá trị bắt đầu là 0
        // Sau mỗi một bước lặp 'value' lại được công thêm 3
        // Và vòng lặp sẽ kết thúc khi 'value' lớn hơn hoặc bằng 10
        for (int value = 0; value < 10; value = value + 3) {
 
            System.out.println("Step =" + step + "  value = " + value);
 
            // Tăng giá trị 'step' lên 1, sau mỗi bước lặp
            step = step + 1;
 
        }
 
    }
 
}
```

Kết quả chạy class  **ForLoopExample1**:

![](https://o7planning.org/vi/10161/images/12343866.png)

Xem tiếp một ví dụ khác, tính tổng các số từ 1 tới 100:

ForLoopExample2.java

package org.o7planning.tutorial.javabasic.loop;
 
public class ForLoopExample2 {
 
    // Đây là một ví dụ tính tổng các số từ 1 tới 100,
    // và in kết quả ra màn hình.
    public static void main(String[] args) {
 
        // Khai báo một biến
        int total = 0;
 
        // Khai báo một biến 'value'
        // Gán giá trị ban đầu 1
        // Sau mỗi bước lặp giá trị của nó tăng lên 1.
        // Chú ý: value++ tương đương với câu lệnh: value = value + 1;
        // value-- tương đương với câu lệnh: value = value - 1;
        for (int value = 1; value <= 100; value++) {
 
            // Gán giá trị 'total' bằng giá trị cũ cộng thêm 'value'.
            total = total + value;
        }
 
        System.out.println("Total = " + total);
 
    }
 
}

Kết quả

![](https://o7planning.org/vi/10161/images/12343886.png)

### 5.6- Vòng lặp while

Đây là cấu trúc vòng lặp  **while**:

```java
// Trong khi condition (điều kiện) đúng, thì làm gì đó.
while ( condition ) {
   // Làm gì đó tại đây...
}
```

Xem ví dụ minh họa

![](https://o7planning.org/vi/10161/images/12343912.png)

WhileExample1.java

```java
package org.o7planning.tutorial.javabasic.loop;
 
public class WhileExampe1 {
 
    public static void main(String[] args) {
 
        int value = 3;
 
        // Trong khi 'value' vẫn nhỏ hơn 10 thì vòng lặp vẫn làm việc.
        while (value < 10) {
 
            System.out.println("Value = " + value);
 
            // Tăng giá trị của value lên 2 đơn vị
            value = value + 2;
        }
    }
     
}
```

### 5.7- Vòng lặp do-while

Đây là cấu trúc vòng lặp  **do-while**:

```java
// Vòng lặp do-while làm việc ít nhất 1 bước lặp (iteration)
// và trong khi điều kiện còn đúng thì nó còn làm việc tiếp.
do {
   // Làm gì đó tại đây.
}
while (condition);
```
Ví dụ minh họa:

![](https://o7planning.org/vi/10161/images/12343944.png)

DoWhileExample1.java

```java
package org.o7planning.tutorial.javabasic.loop;
 
public class DoWhileExample1 {
 
    public static void main(String[] args) {
 
        int value = 3;
 
        // Vòng lặp do-while luôn được thực thi ít nhất 1 lần.
        do {
 
            System.out.println("Value = " + value);
 
            // Tăng giá trị cho 'value' thêm 3
            value = value + 3;
 
        } while (value < 10);
 
    }
}
```

Kết quả

![](https://o7planning.org/vi/10161/images/12343958.png)

## 6- Mảng trong Java (Array)

### 6.1- Mảng là gì?

Mảng là một danh sách các phần tử được sắp xếp liền nhau trên bộ nhớ.

Hãy xem một hình ảnh mảng 5 phần tử, chứa các số int.

![](https://o7planning.org/vi/10161/images/12343984.png)

### 6.2- Làm việc với mảng

Cách khai báo một mảng trong Java.

```java
// Khai báo một mảng, chưa chỉ rõ số phần tử.
int[] array1;
 
// Khởi tạo mảng với 100 phần tử
// Các phần tử chưa được gán giá trị cụ thể
array1 = new int[100];
 
// Khai báo một mảng chỉ rõ số phần tử
// Các phần tử chưa được gán giá trị cụ thể
double[] array2 = new double[10];
 
// Khai báo một mảng với các phần tử được gán giá trị cụ thể.
// Mảng này có 4 phần tử
long[] array3= {10L, 23L, 30L, 11L};
```

Hãy xem một ví dụ:

![](https://o7planning.org/vi/10161/images/12344010.png)

![](https://o7planning.org/vi/10161/images/12344012.png)

ArrayExample1.java

```java
package org.o7planning.tutorial.javabasic.array;
 
public class ArrayExample1 {
 
    public static void main(String[] args) {
 
        // Khai báo một mảng 5 phần tử
        int[] myArray = new int[5];
 
        // Chú ý: phần tử đầu tiên của mảng có chỉ số là 0:
        // Gán giá trị cho phần tử đầu tiên (Chỉ số 0)
        myArray[0] = 10;
 
        // Gán giá trị cho phần tử thứ hai (Chỉ số 1)
        myArray[1] = 14;
 
        myArray[2] = 36;
        myArray[3] = 27;
 
        // Giá giá trị cho phần tử thứ 5 (Phần tử cuối cùng trong mảng)
        myArray[4] = 18;
 
        // In ra màn hình Console số phần tử của mảng.
        System.out.println("Array Length=" + myArray.length);
 
        // In ra phần tử tại chỉ số 3 (Phần tử thứ 4 trong mảng)
        System.out.println("myArray[3]=" + myArray[3]);
 
        // Sử dụng vòng lặp for để in ra các phần tử trong mảng.
        for (int index = 0; index < myArray.length; index++) {
            System.out.println("Element " + index + " = " + myArray[index]);
        }
    }
 
}
```

Kết quả:

![](https://o7planning.org/vi/10161/images/12344026.png)

Một ví dụ minh họa tiếp sử dụng vòng lặp for để gán giá trị cho các phần tử:

ArrayExample2.java

```java
package org.o7planning.tutorial.javabasic.array;
 
public class ArrayExample2 {
 
    public static void main(String[] args) {
 
        // Khai báo một mảng 5 phần tử
        int[] myArray = new int[5];
 
        // In ra màn hình Console số phần tử của mảng.
        System.out.println("Array Length=" + myArray.length);
 
        // Sử dụng vòng lặp for để gán giá trị cho các phần tử của mảng.
        for (int index = 0; index < myArray.length; index++) {
            myArray[index] = 100 * index * index + 3;
        }
 
        // In ra màn hình Console phần tử tại chỉ số 3
        System.out.println("myArray[3] = " + myArray[3]);
    }
 
}
```

Kết quả

![](https://o7planning.org/vi/10161/images/12344046.png)

## 7- Class, đối tượng và cấu tử (Class, Instance, Constructor)

Bạn cần có sự phân biệt giữa 3 khái niệm:

-   Class
-   Cấu tử (Constructor) (Còn gọi là phương thức khởi tạo).
-   Đối tượng (Instance)

Khi chúng ta nói về Cây, nó là một thứ gì đó trìu tượng, nó là một lớp (class). Nhưng khi chúng ta chỉ thẳng vào một cái cây cụ thể thì lúc đó đã rõ ràng và đó là đối tượng (object) (Cũng được gọi là một thể hiện (instance) )

![](https://o7planning.org/vi/10161/images/12344066.png)

Hoặc khi chúng ta nói về người (Person) thì đó cũng trìu tượng, nó là một lớp. Nhưng khi chỉ thẳng vào bạn hoặc tôi thì đó là 2 đối tượng khác nhau, cùng thuộc lớp người.

![](https://o7planning.org/vi/10161/images/12344074.png)

Person.java

```java
package org.o7planning.tutorial.javabasic.javastructure;
 
public class Person {
 
    // Đây là một trường (Field).
    // Lưu trữ tên người.
    public String name;
 
    // Đây là một Constructor (Phương thức khởi tạo)
    // Dùng nó để khởi tạo đối tượng.
    // Constructor này có một tham số.
    // Constructor luôn có tên giống tên của lớp.
    public Person(String persionName) {
        // Gán giá trị từ tham số vào cho trường name.
        this.name = persionName;
    }
 
    // Đây là một phương thức trả về kiểu String.
    public String getName() {
        return this.name;
    }
 
}
```

Như trên class  **Person**  không có phương thức  _**main**_. Tiếp theo lớp  **TestPerson**  là ví dụ khởi tạo các đối tượng của  **Person**  thông qua các phương thức khởi tạo (Constructor).

PersonTest.java

```java
package org.o7planning.tutorial.javabasic.javastructure;
 
public class PersonTest {
 
    public static void main(String[] args) {
 
        // Tạo một đối tượng từ lớp Person
        // Khởi tạo đối tượng này từ Constructor của lớp Person 
        Person edison = new Person("Edison");
 
        // Lớp Person có phương thức getName()
        // Sử dụng đối tượng để gọi phương thức getName():
        String name = edison.getName();
        System.out.println("Person 1: " + name);
 
        // Tạo một đối tượng từ class Person.
        // Khởi tạo đối tượng này tử cấu tử của class Person 
        Person billGate = new Person("Bill Gates");
 
        // Lớp Person có trường name là công khai (public)
        // Sử dụng đối tượng để tham chiếu tới nó.
        String name2 = billGate.name;
        System.out.println("Person 2: " + name2);
 
    }
 
}
```

Kết quả chạy ví dụ:

![](https://o7planning.org/vi/10161/images/12344098.png)

## 8- Trường (Field)

Trong phần tiếp theo này chúng ta sẽ thảo luận về một số khái niệm:

Trường (Field)

-   Trường thông thường
-   Trường tĩnh (static Field)
-   Trường final (final Field)
-   Trường tĩnh và final (static final Field)

Xem một ví dụ với trường thông thường và trường tĩnh.

![](https://o7planning.org/vi/10161/images/12344124.png)

FieldSample.java

```java
package org.o7planning.tutorial.javabasic.javastructure;
 
public class FieldSample {
 
    // Đây là một trường tĩnh (static field).
    public static int MY_STATIC_FIELD = 100;
 
    // Đây là một trường thông thường.
    public String myValue;
 
    // Constructor để khởi tạo đối tượng FieldSample.
    public FieldSample(String myValue) {
        this.myValue = myValue;
    }
 
}
```

FieldSampleTest.java

```java
package org.o7planning.tutorial.javabasic.javastructure;
 
public class FieldSampleTest {
 
    public static void main(String[] args) {
 
        // Tạo đối tượng thứ nhất.
        FieldSample obj1 = new FieldSample("Value1");
 
        System.out.println("obj1.myValue= " + obj1.myValue);
 
        // In ra giá trị của trường tĩnh MY_STATIC_FIELD.
        // Tham chiếu thông qua đối tượng (Không được khuyến khích).
        System.out.println("obj1.MY_STATIC_FIELD= " + obj1.MY_STATIC_FIELD);
 
        // In ra giá trị của trường tĩnh - MY_STATIC_FIELD.
        // Với các trường tĩnh, có thể truy cập tới nó thông qua lớp.
        // (Cách này được khuyến khích).
        System.out.println("FieldSample.MY_STATIC_FIELD= " + FieldSample.MY_STATIC_FIELD);
 
        // Tạo đối tượng thứ 2:
        FieldSample obj2 = new FieldSample("Value2");
 
        System.out.println("obj2.myValue= " + obj2.myValue);
 
        System.out.println("obj2.MY_STATIC_FIELD= " + obj2.MY_STATIC_FIELD);
 
        System.out.println(" ------------- ");
 
        // Trường tĩnh được sử dụng chung cho mọi đối tượng của cùng một lớp.
        // Gán giá trị mới cho trường tĩnh MY_STATIC_FIELD.
        // (Có thể dùng cách: FieldSample.MY_STATIC_FIELD = 200)
        obj1.MY_STATIC_FIELD = 200;
 
        // Tại đây sẽ in ra giá trị 200.
        System.out.println("obj2.MY_STATIC_FIELD= " + obj2.MY_STATIC_FIELD);
    }
     
}
```

Kết quả chạy ví dụ:

![](https://o7planning.org/vi/10161/images/12344144.png)

Các trường  **final**  là các trường mà không thể gán giá trị mới cho nó, nó giống như một hằng số.

FinalFieldExample.java

```java
package org.o7planning.tutorial.javabasic.javastructure;
 
public class FinalFieldExample {
 
    // Một trường final (Cũng được gọi là trường hằng số).
    // Trường final không cho phép gán giá trị mới.
    public final int myValue = 100;
 
    // Một trường tĩnh và final.
    // Trường final không cho phép gán giá trị mới.
    public static final long MY_LONG_VALUE = 1234L;
 
}
```

## 9- Phương thức (Method)

Phương thức (Method):

-   Phương thức thông thường.
-   Phương thức tĩnh
-   Phương thức  **final**. (Sẽ được đề cập trong phần thừa kế của class).

MethodSample.java

```java
package org.o7planning.tutorial.javabasic.javastructure;
 
public class MethodSample {
 
    public String text = "Some text";
 
    // Constructor mặc định.
    public MethodSample() {
 
    }
 
    // Đây là một phương thức trả về kiểu String.
    // Phương thức này không có tham số
    public String getText() {
        return this.text;
    }
 
    // Đây là một phương thức có 1 tham số String.
    // Phương thức này trả về kiểu void (Hay gọi là không trả về gì)
    public void setText(String text) {
        // this.text tham chiếu tới trường text.
        // phân biệt với tham số text.
        this.text = text;
    }
 
    // Đây là một phương thức tĩnh.
    // Trả về kiểu int, có 3 tham số.
    public static int sum(int a, int b, int c) {
        int d = a + b + c;
        return d;
    }
}
```

MethodSampleTest.java

```java
package org.o7planning.tutorial.javabasic.javastructure;
 
public class MethodSampleTest {
 
    public static void main(String[] args) {
 
        // Tạo đối tượng MethodSample
        MethodSample obj = new MethodSample();
 
        // Gọi phương thức getText()
        String text = obj.getText();
 
        System.out.println("Text = " + text);
 
        // Gọi phương thức setText(String)
        obj.setText("New Text");
 
        System.out.println("Text = " + obj.getText());
 
        // Phương thức tĩnh có thể được gọi thông qua lớp.
        // Cách này được khuyến khích dùng. (**)
        int sum = MethodSample.sum(10, 20, 30);
 
        System.out.println("Sum  10,20,30= " + sum);
 
        // Hoặc gọi thông qua đối tượng.
        // Cách này không được khuyến khích. (**)
        int sum2 = obj.sum(20, 30, 40);
 
        System.out.println("Sum  20,30,40= " + sum2);
    }
 
}
```

![](https://o7planning.org/vi/10161/images/12344182.png)

## 10- Thừa kế trong Java

Java cho phép viết class mở rộng từ một class. Class mở rộng từ một class khác được gọi là class con. Class con có khả năng thừa kế các trường và các method từ class cha.

Animal.java

```java
package org.o7planning.tutorial.javabasic.inheritance;
 
public class Animal {
 
    public Animal() {
 
    }
 
    public void move() {
        System.out.println("Move ...!");
    }
 
    // Tiếng kêu của động vật này.
    public void say() {
        System.out.println("<nothing>");
    }
 
}
```

Cat.java

```java
package org.o7planning.tutorial.javabasic.inheritance;
 
public class Cat extends Animal {
 
    // Ghi đè (override) phương thúc của lớp Animal.
    public void say() {
        System.out.println("Meo");
    }
 
}
```

Dog.java

```java
package org.o7planning.tutorial.javabasic.inheritance;
 
public class Dog extends Animal {
 
    // Ghi đè phương thức của lớp Animal.
    public void say() {
        System.out.println("Go");
    }
 
}
```

Ant.java

```java
package org.o7planning.tutorial.javabasic.inheritance;
 
// Con kiến
public class Ant extends Animal {
 
}
```

AnimalTest.java

```java
package org.o7planning.tutorial.javabasic.inheritance;
 
public class AnimalTest {
 
    public static void main(String[] args) {
 
        // Khai báo một đối tượng Cat.
        Cat cat = new Cat();
 
        // Kiểm tra xem 'cat' có phải là đối tượng của Animal hay không.
        // Kết quả rõ ràng là true.
        boolean isAnimal = cat instanceof Animal;
        System.out.println("cat instanceof Animal?" + isAnimal);
 
        // ==> Meo
        // Gọi tới phương thức say() của Cat.
        cat.say();
 
        // Khai báo một đối tượng Animal.
        // Khởi tạo đối tượng thông qua Constructor của Cat.
        Animal cat2 = new Cat();
 
        // ==> Meo
        // Phương thức say() của Cat được gọi (Chứ không phải của Animal).
        cat2.say();
 
        // Tạo đối tượng Animal.
        // Thông qua constructor của lớp con, Ant.
        Animal ant = new Ant();
 
        // Ant không có phương thức say()
        // ==> Nó gọi vào phương thức say(), thừa kế từ lớp cha (Animal).
        ant.say();
    }
}
```

Kết quả chạy ví dụ:

![](https://o7planning.org/vi/10161/images/12344232.png)

**Nguồn bài viết**: [o7planning](https://o7planning.org)

## #Kết thúc

Vậy là sau khi **học tiếng** Java, chúng ta đã có thể bắt đầu **nói chuyện** với Android được rồi. Ở bài viết kế tiếp mình sẽ hướng dẫn các bạn cài đặt môi trường, làm quen với Android, xây dựng 1 ứng dụng Android cơ bản. Hẹn gặp lại các bạn !