from datetime import datetime, timedelta

# default=datetime.today().year
# print(default)
# print(datetime(default-10,1,1),datetime(default,1,1))

def get():
    result = {}
    this_year=datetime.today().year
    for i in range(10):
        breakpoint()
        age_num = (datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),1,1))
        print(datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),12,31))
        if i == 0:
            age_key = '10대 미만'
        else:
            age_key = str(i * 10) + '대'

        result[age_key] = age_num

    return result

# print(get())
# import hashlib
# json_log = {"url": "/api/boards/24", "method": "DELETE", "board_id": 24, "user_id": 21, "name": "log_file2", "inDate": "2022-12-01T01:32:21.437Z", "detail": {"message": "DELETE access Board Detail", "levelname": "INFO"}, "x_forward_for": None}
# def hashing_id(id):
