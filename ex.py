from datetime import datetime, timedelta

# default=datetime.today().year
# print(default)
# print(datetime(default-10,1,1),datetime(default,1,1))

def get():
    result = {}
    this_year=datetime.today().year
    for i in range(10):
        age_num = (datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),1,1))
        print(datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),12,31))
        if i == 0:
            age_key = '10대 미만'
        else:
            age_key = str(i * 10) + '대'

        result[age_key] = age_num

    return result

print(get())