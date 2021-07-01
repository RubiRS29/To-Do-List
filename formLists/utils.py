from .models import List

def get_all_list( id_user ):
    lists = List.objects.filter(user=id_user)
    return lists

