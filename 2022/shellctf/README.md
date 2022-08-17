# **S.H.E.L.L CTF**
## **tea** - 268 points 
### *It's tea time. The flag format is shellctf{...}*
[![Foo](/2022/shellctf/images/img_tea.PNG)](https://github.com/LaoDaiDia/CTF/blob/main/2022/shellctf/tea)

*Công cụ: Kali.Linux_x64.v2021.1, IDA Freeware 7.7*

Đầu tiên ta chạy thử tập tin tea trên môi trường Kali linux để có cái nhìn đầu tiên về challenge.

<!-- <p align='center'>
<img  src="/2022/shellctf/images/img_tea_file.PNG" alt="Chương trình tea"></p> -->
![Chạy thử tập tin tea trên Kali linux](/2022/shellctf/images/img_tea_file.PNG)


Nhận thấy ở challenge này yêu cầu người chơi cần truyền vào 1 flag.\
Sử dụng trình xem mã giả *(Pseudocode)* trong IDA để xem và phân tích chi tiết.
<!-- <p align='center'>
<img  src="/2022/shellctf/images/img_ida_pseudocode.PNG" alt="Trình xem mã giả trong IDA" style="width:724px;height:667px;"></p> -->
![Mở tập tin trên IDA](/2022/shellctf/images/img_ida_pseudocode.PNG)

Dễ thấy chương trình sử dụng 5 hàm:
- boilWater(): gán chuỗi nhập vào từ người dùng vào biến **pwd**

![boilWater](/2022/shellctf/images/img_boilWater.PNG)


Sau đó chương trình sẽ kiểm tra chuỗi nhập vào có đúng 32 ký tự hay không.
- addSugar(), addTea(), addMilk(): dùng để "xáo trộn xào nấu" chuỗi **pwd**
- strainAndServe(): so sánh chuỗi **pwd** sau khi xáo trộn với chuỗi có sẵn, nếu đúng thì in ra **"yep, that's right"**

![strainAndServe](/2022/shellctf/images/img_strainAndServe.PNG)

Từ đó suy ra, bài này cần tìm một chuỗi **pwd** nhập vào (cũng chính là *flag*) thoả điều kiện: 
+ Có chiều dài 32 ký tự
+ Có dạng shellctf{...}
+ Sau khi biến đổi qua các hàm thì có kết quả như chuỗi có sẵn

**_Hướng giải quyết bài này là đi từ chuỗi kết quả có sẵn trở ngược lên_** 

1. Phân tích hàm addMilk()

![hàm addMilk()](/2022/shellctf/images/img_addMilk.PNG) 

Hàm này sử dụng 3 biến kiểu *char* là **dest, s** và **v14** để lưu chuỗi tạm và biến đếm **v3**. Hàm *strncat()* dùng để nối chuỗi. 
- Hàm while ở dòng 40: kiểm tra và thực hiện gán từng ký tự từ đầu chuỗi **pwd** đến khi gặp ký tự **5** (có mã ascii là 53) thì dừng, gán chuỗi kết quả vào **dest** 
- Hàm while ở dòng 42: tiếp tục kiểm tra và gán các ký tự tiếp theo của chuỗi **pwd** đến khi gặp ký tự **R** (có mã ascii là 82) thì dừng lại, gán chuỗi kết quả vào **s**
- Hàm while ở dòng 44: gán các ký tự còn lại của chuỗi **pwd** vào **v14**
- Code từ dòng 46 -> 50: nối **v14**, **dest**, **s** theo thứ tự và gán cho **pwd**.

![Phân tích chuỗi pwd ở hàm addMilk()](/2022/shellctf/images/img_pwd-addMilk.PNG)

Từ đó, ta có hàm decode hàm *addMilk()* như sau:

![re-addMilk()](/2022/shellctf/images/img_re-addMilk-f.PNG)

*Biến i trong hàm đóng vai trò là biến "chạy" do lúc này ta không biết điểm đầu và cuối của chuỗi **pwd** ban đầu truyền vào hàm addMilk()*

2. Phân tích hàm addTea()

![hàm addTea()](/2022/shellctf/images/img_addTea.PNG)

Hàm này chia chuỗi **pwd** làm 2 nửa để xử lý:
- Nửa đầu sẽ biến đổi theo công thức ở dòng 26
- Nửa sau sẽ biến đổi theo công thức ở dòng 34
Ta có chương trình hàm decode hàm *addTea()* như sau:

![re-addTea()](/2022/shellctf/images/img_re-addTea-f.PNG)

3. Phân tích hàm addSugar()

![hàm addSugar()](/2022/shellctf/images/img_addSugar.PNG)

Hàm addSugar() này đơn giản là chuyển các ký tự ở vị trí lẻ ra đầu, các ký tự ở vị trí chẳn ra sau, duyệt theo thứ tự từ trái sang phải của chuỗi truyền vào.

Ta có chương trình hàm decode hàm *addSugar()* như sau:

![re-addSugar()](/2022/shellctf/images/img_re-addSugar-f.PNG)

Kết quả của chương trình reverse sẽ thu được nhiều key, những key này đều bypass được các hàm *addSugar(), addTea(), addMilk()* để in ra chuỗi ký tự *"yep, that's right"*. Tuy nhiên, key có dạng **_shellctf{}_** mới chính là *flag* cần tìm.


![Kết quả trả về của chương trình re_tea.py](/2022/shellctf/images/img_result.PNG)




