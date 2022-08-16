# **S.H.E.L.L CTF**
## **tea** - 268 points 
### *It's tea time. The flag format is shellctf{...}*
[![Foo](/2022/shellctf/images/img_tea.PNG)](https://github.com/LaoDaiDia/CTF/blob/main/2022/shellctf/tea)

*Công cụ: Kali.Linux_x64.v2021.1, IDA Freeware 7.7*

Đầu tiên ta chạy thử tập tin tea trên môi trường Kali linux để có cái nhìn đầu tiên về challenge.

<!-- <p align='center'>
<img  src="/2022/shellctf/images/img_tea_file.PNG" alt="Chương trình tea"></p> -->
![](/2022/shellctf/images/img_tea_file.PNG)


Nhận thấy ở challenge này yêu cầu người chơi cần truyền vào 1 flag.\
Sử dụng trình xem mã giả *(Pseudocode)* trong IDA để xem và phân tích chi tiết.
<!-- <p align='center'>
<img  src="/2022/shellctf/images/img_ida_pseudocode.PNG" alt="Trình xem mã giả trong IDA" style="width:724px;height:667px;"></p> -->
![](/2022/shellctf/images/img_ida_pseudocode.PNG)

Dễ thấy chương trình sử dụng 5 hàm:
- boilWater(): gán chuỗi nhập vào từ người dùng vào biến **pwd** \
![](/2022/shellctf/images/img_boilWater.PNG)


Sau đó chương trình sẽ kiểm tra chuỗi nhập vào có đúng 32 ký tự hay không.
- addSugar(), addTea(), addMilk(): dùng để "xáo trộn xào nấu" chuỗi **pwd**
- strainAndServe(): so sánh chuỗi **pwd** sau khi xáo trộn với chuỗi có sẵn, nếu đúng thì in ra **"yep, that's right"**
![](/2022/shellctf/images/img_strainAndServe.PNG)

Từ đó suy ra, bài này cần tìm một chuỗi **pwd** nhập vào (cũng chính là *flag*) thoả điều kiện: 
+ Có chiều dài 32 ký tự
+ Có dạng shellctf{...}
+ Sau khi biến đổi qua các hàm thì có kết quả như chuỗi có sẵn

**_Hướng giải quyết bài này là đi từ chuỗi kết quả có sẵn trở ngược lên_**

1. Phân tích hàm addMilk() 
![](/2022/shellctf/images/img_addMilk.PNG) 

Hàm này sử dụng 3 biến kiểu *char* là **dest, s** và **v14** để lưu chuỗi tạm và biến đếm **v3**. Hàm *strncat()* dùng để nối chuỗi. \
- Hàm while ở dòng 40: kiểm tra và thực hiện gán từng ký tự từ đầu chuỗi **pwd** đến khi gặp ký tự **5** (có mã ascii là 53) thì dừng, gán chuỗi kết quả vào **dest** 
- Hàm while ở dòng 42: tiếp tục kiểm tra và gán các ký tự tiếp theo của chuỗi **pwd** đến khi gặp ký tự **R** (có mã ascii là 82) thì dừng lại, gán chuỗi kết quả vào **s**
- Hàm while ở dòng 44: gán các ký tự còn lại của chuỗi **pwd** vào **v14**
- Code từ dòng 46 -> 50: nối **v14**, **dest**, **s** theo thứ tự và gán cho **pwd**.