def Mersenne_Twister_Algo_Tester_In_Random_Module():
    """
    This function will test the reliability of the random module's MersenneTwister Algorithm with respect 
    to the degree of efficiency of 'randomness'. Computers are deterministic but there are algorithms that  
    can simulate randomness('simulate' because true randomness is impossible for computers to generate). 
    For example, if input is random.randint(1,100), will it truly give a random number or bias towards a 
    sequence. For more understanding, study the science of PRNGs. 
    """
    from random import randint
    n1 = 1
    n2 = 100
    span = 1000 # Larger span will result in more precise and accurate values as the avg will be based on solid results (How probability flattens with large number of samples)
    def func():
        x = 0
        y = randint(n1,n2)
        x+=1
        while y != 1: # 1 is not specific. Any number between 1 and 100 can be used
            x+=1
            y = randint(n1,n2)
        return x    

    templist = []
    for _ in range(span):
        temp = func()
        templist.append(temp)
    
    avgnumOfTimesTakenToFindn = sum(templist) / len(templist)
    numOfTimesItShouldTake = abs(n1-n2)+1
    accuracy = 100-((abs(avgnumOfTimesTakenToFindn-numOfTimesItShouldTake)/numOfTimesItShouldTake)*100)
    accuracy = round(accuracy)

    return accuracy

# Testing
# print(f"Accuracy : {Mersenne_Twister_Algo_Tester_In_Random_Module()} %")