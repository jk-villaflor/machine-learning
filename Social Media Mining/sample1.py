import json


# v_list = ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”',
#  '“It is our choices, Harry, that show what we truly are, far more than our abilities.”',
#  '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”',
#  '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”',
#  "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",
#  '“Try not to become a man of success. Rather become a man of value.”',
#  '“It is better to be hated for what you are than to be loved for what you are not.”',
#  "“I have not failed. I've just found 10,000 ways that won't work.”",
#  "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”",
#  '“A day without sunshine is like, you know, night.”']

v_list1 = {
    '0':'zero'
,   '1':'one'
}

with open('data.json', 'w') as outfile:
    outfile.write(json.dumps(v_list1))

print(type(v_list1))