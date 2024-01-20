s=str(input("country name : "))

data = { 'Singapore':"India",
          'Ireland':6,
          'United Kingdom':7,
          'Germany': 17,
          'Armenia':34,
          'United States':17,
          'Canada':9,
          'Italy':74,
          
        }

print(data.get(s,"Not found"))


