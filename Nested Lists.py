if __name__ == '__main__':
    nested_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name,score])
    first_min=min(nested_list,key=lambda x:x[1])
    for _,score innested_list:
        if score>first_max and score<sec_last:
            sec_last=score
    
        
        
