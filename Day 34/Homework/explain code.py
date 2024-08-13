def find_short(s): 
#ჯერ ვიწყებთ find_short ფუნქციის შექმნით რომელსაც პარამეტრად გადაეცემა s
    list1 = s.split(" ")
    # ეხლა ვქმნით ცვლადს სადაც მნიშვნელობათ იქნება s რომლის სტრინგებს ვხლიჩავთ ისე რომ ცალ ცალკე სტრინგებად დაიყოს ტექსტი


    word_len = len(list1[0])
    # შემდეგ word_len ცვლადს მნიშვნელობად გადაეცემა list1-ის მენულე ინდექსზე მყოფი სტრინგი
    for i in list1:
    # ვუვლით for loop-ით
        if len(i) < word_len:
        # თუ ლისტში სტრინგებიდან რომელიმე word_len-ზე პატარაა მაშინ
            word_len = len(i)
        # აი ეს word_len-ის მნიშვნელობა იქნება ეგ სტრინგი
    
    # word_len = 3
    return word_len
    # ეხლა ვაბრუნებთ word_len-ს

print(find_short("bitcoin take over the world maybe who knows perhaps"))
# და ბოლოს ვიძახებთ ფუნქციას

# ეს ფუნქცია გამოიტანს ყველაზე პატარა სტრინგს სიაში ოღონდ რამდენი ასო აქვს იმას