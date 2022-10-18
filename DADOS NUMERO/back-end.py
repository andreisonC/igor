while True:
    import phonenumbers
    from phonenumbers import geocoder
    from phonenumbers import carrier
    a =  input('Digite seu numero: ')
    phone = a
    phone_ajusted = phonenumbers.parse(phone, 'BR')
    print(phone_ajusted)        
    #geocoder       
    local = geocoder.description_for_number(phone_ajusted, 'pt-br')
    print(local)        
    #carrier        
    carrier = carrier.name_for_number(phone_ajusted, 'pt-br')
    print(carrier, 'operadora')
    print(phone_ajusted)
    print('asd')
    print(local)