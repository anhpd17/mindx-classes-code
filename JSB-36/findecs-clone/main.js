let buttonCate1 = document.querySelector(".interest-list .cate1");
buttonCate1.onclick = function () {
    buttonCate1.classList.toggle("pink-bg");
};
let buttonCate2 = document.querySelector(".interest-list .cate2");
buttonCate2.onclick = function () {
    buttonCate2.classList.toggle("yellow-bg");
};

Luyện tập onclick

1. Tạo 2 ô nhập liệu cho người dùng nhập 2 số: a và b
Có 1 button khi bấm vào sẽ thông báo tổng của 2 số

2. Tạo 3 ô nhập liệu cho người dùng nhập 3 số: a,b,c
Bấm button sẽ tìm ra số lớn nhất trong 3 số

3. Tạo 3 ô nhập ngày - tháng - năm sinh.
Bấm button sẽ tìm ra số chủ đạo của người đó trong thần số học

(VD: 11/11/2003 => 1 + 1 + 1 + 1 + 2 + 0 + 0 + 3 = 9)