# Bài 1

Python là ngôn ngữ thông dịch vì nó chạy trực tiếp mã nguồn thông qua trình thông dịch, không cần biên dịch thành mã máy trước. Python thực thi từng dòng mã, nếu gặp lỗi trong chương trình thì sẽ dừng tại dòng xảy ra lỗi


# Bài 2

## Các kiểu dữ liệu

###  Kiểu dữ liệu số

- **int**: số nguyên
- **float**: số thực
- **complex**: số phức

###  Kiểu dữ liệu chuỗi (str)

Chuỗi có thể được đặt trong dấu ngoặc đơn (`' '`) hoặc dấu ngoặc kép (`" "`)

###  Kiểu dữ liệu danh sách (list)

Danh sách là một cấu trúc dữ liệu có thứ tự, có thể chứa nhiều kiểu dữ liệu khác nhau. Các phần tử trong danh sách được đặt trong dấu ngoặc vuông `[]` và phân cách bởi dấu phẩy

###  Kiểu dữ liệu tuple

Tuple tương tự như danh sách nhưng **không thể thay đổi** sau khi được tạo. Các phần tử trong tuple được đặt trong dấu ngoặc đơn `()` và phân cách bởi dấu phẩy

###  Kiểu dữ liệu từ điển (dict)

Từ điển là một cấu trúc dữ liệu lưu trữ các cặp **khóa - giá trị (key - value)**. Các phần tử trong từ điển được đặt trong dấu ngoặc nhọn `{}`

###  Kiểu dữ liệu tập hợp (set)

Tập hợp là một cấu trúc dữ liệu chứa các phần tử **không trùng lặp**. Các phần tử được đặt trong dấu ngoặc nhọn `{}`


## Các toán tử

###  Toán tử số học

- Cộng: `+`
- Trừ: `-`
- Nhân: `*`
- Chia: `/`
- Chia lấy phần nguyên: `//`
- Chia lấy phần dư: `%`
- Lũy thừa: `**`

###  Toán tử so sánh

- Bằng: `==`
- Khác: `!=`
- Lớn hơn: `>`
- Nhỏ hơn: `<`
- Lớn hơn hoặc bằng: `>=`
- Nhỏ hơn hoặc bằng: `<=`

###  Toán tử gán

- Gán: `=`
- Gán cộng: `+=`
- Gán trừ: `-=`
- Gán nhân: `*=`
- Gán chia: `/=`
- Gán chia lấy dư: `%=`
- Gán lũy thừa: `**=`

###  Toán tử logic

- `and`
- `or`
- `not`

### 5. Toán tử Membership

- `in`: Trả về `True` nếu phần tử có trong tập hợp hoặc chuỗi
- `not in`: Trả về `True` nếu phần tử không có trong tập hợp hoặc chuỗi

### 6. Toán tử Identity

- `is`: Trả về `True` nếu hai biến cùng tham chiếu đến một đối tượng
- `is not`: Trả về `True` nếu hai biến không cùng tham chiếu đến một đối tượng


## Mệnh đề điều kiện và vòng lặp

### Điều kiện

- `if`
- `elif`
- `else`

### Vòng lặp

- `for`
- `while`
- `break`: Dừng vòng lặp.
- `continue`: Bỏ qua lần lặp hiện tại và chuyển sang lần lặp tiếp theo.


## Kiểu dữ liệu True, False

`True` và `False` là hai giá trị thuộc kiểu dữ liệu **bool**.

- `True`: Đúng.
- `False`: Sai.