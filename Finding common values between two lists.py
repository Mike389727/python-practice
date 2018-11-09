"""Mike W - matching values in lists
Takes a two lists and finds values in common using many different methods. uses timeit
to find the fastest method to use"""
import timeit

def common_values_using_set_intersection(alist, blist):
        """compares two lists together using set.intersection """
        items_in_common = set(alist).intersection(blist)
        statement = "Common items between two lists using a set: {}"
        return statement.format(list(items_in_common))


def common_values_usins_loop(alist,blist):
        """compares two lists together using two for loops O(n*2) """
        resultlist = []
        for value in alist:
                for second_value in blist:
                        if value == second_value:
                                resultlist.append(value)
        statement = "Common items between two lists using a two for loops: {}"
        return statement.format(resultlist)

def main():
        a = [2,4,6,8,10,12,14,16,18,20]
        b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        
        start_time = timeit.default_timer()       
        print(common_values_using_set_intersection(a,b))
        print(timeit.default_timer() - start_time)
        
        start_time = timeit.default_timer()  
        print(common_values_usins_loop(a,b))
        print(timeit.default_timer() - start_time)
        
        
        
main()