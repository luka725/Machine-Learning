import pandas as pd
df = pd.read_excel("monitors_sanitized.xlsx")
print("აირჩიეთ რომელი იდენთიფიკატორით გსურთ ანალიტიკური მონაცემების მიღება")
print("<---ბრენდი\n<---სიხშირე\n<---რეზოლუცია\n<---ტიპი")
identifier = input("ჩაწერეთ იდენტიფიკატორი მოცემული მენიუდან:\n")
if identifier in df.columns:
    identifier_list = list(set(df[identifier]))
    for current in sorted(identifier_list):
        print(f"{current}\n")
    id = input("შეიყვანეთ სასურველი იდენტიფიკატორი მოცემული მენიუდან:\n")
    if(id in df[identifier].values):
        info = df[df[identifier] == id]
        average_price = info['ფასი'].mean()
        std_dev_price = info['ფასი'].std()
        percentile_50_price = info['ფასი'].quantile(0.5)
        print(f'{len(info)} პროდუქტიდან')
        print(f'ფასების საშუალო: {average_price}')
        print(f'სტანდარტული გადახრა: {std_dev_price}')
        print(f'50% პროცენტილი: {percentile_50_price}')
    else: 
        print("მსგავსი იდენტიფიკატორი არ მოიძებნა")
else:
    print("მსგავსი იდენტიფიკატორი არ მოიძებნა")
