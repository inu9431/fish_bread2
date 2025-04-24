class BreadShop:
    def __init__(self):
        self.stock = { "팥붕어빵":10,"슈크림붕어빵":8,"초코붕어빵": 5}
        self.sales = {"팥붕어빵":0,"슈크림붕어빵":0,"초코붕어빵":0}
        self.price = {"팥붕어빵" : 1000,"슈크림붕어빵" : 1200,"초코붕어빵" : 1500}

    def order_bread(self):
        while True:
            bread_type = input ("주문할 붕어빵 맛을 선택하세요(팥붕어빵,슈크림붕어빵,초코붕어빵)(뒤로가기입력시종료:")
            if bread_type == "뒤로가기":
                break
            if bread_type in self.stock:
                bread_count = int(input("주문할 개수를 입력하세요:"))
                if  self.stock[bread_type] >= bread_count:
                    self.stock[bread_type] -= bread_count
                    self.sales[bread_type] += bread_count
                    print(f"{bread_type}{bread_count}입니다")
                else:
                    print(f"지금 주문 가능 재고가 없습니다.현재{self.stock[bread_type]}개만 주문 가능합니다")
            else:
                print("정신을 똑바로 차리시고 주문 해주세요👀")


# 붕어빵 admin 기능
    def admin_mode(self):
        while True:
            bread_type =input("주문할 붕어빵 맛을 선택하세요(팥붕어빵,슈크림붕어빵,초코붕어빵)(뒤로가기입력시종료:")
            if bread_type == "뒤로가기":
                break
            if bread_type in self.stock:  # 스톡 안에 드레드타입이 있나요
                bread_count = int(input("창고에 채워넣을 개수를 입력하세요:"))  # 있으면 스톡에 있는 재고를 추가를 하고 인풋으로 개수를 정해주세여
                self.stock[bread_type] += bread_count # stock[bread_type] = stock[bread_type] + bread_count  입니다
                print(f"{bread_type}의 재고가{bread_count}개 추가되어, 현재 {self.stock[bread_type]}개 입니다.")
            else:
                print("정신을 똑바로 차리시고 맛을 다시 선택 해주세요👀")

    def calculate_sales(self):
        # total_sales =  sum(sales[key] * price[key])for key in sales #딕셔너리를 for문에 넣으면 하나씩 데이터를 가져오는데 이 데이터는 key,value
        total = 0
        for key in self.sales:
            total += (self.sales[key] * self.price[key])
        print(f'오늘의 총 매출은{total}원 입니다')
