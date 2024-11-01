#Write a program to merge two dictionaries.
my_info = {'first_name':'john','last_name':'smith','age':22,'height':'1.72m'}
my_favorites = {'fav_music':'bad liars','fav_film':'transformers','fav_lang':'python'}

def merge_dict(dict_1,dict_2):
    """Merge two dictionaries using + operator."""
    dict_1.update(dict_2)
    return dict_1

personal_info = merge_dict(my_info,my_favorites)
print(personal_info)
